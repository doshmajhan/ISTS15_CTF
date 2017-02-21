#!/usr/bin/python3

import fbchat
import subprocess
import time
import urllib.parse

#subclass fbchat.Client and override required methods
class ChallengeBot(fbchat.Client):

    seenUsers = []

    def __init__(self,email, password, debug=False, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)


    def playIntro(self, author_id):
        self.seenUsers.append(str(author_id))

        time.sleep(2)
        self.send(author_id, "hey friend")

        time.sleep(4)
        self.send(author_id, "so here's the scoop...")

        time.sleep(6)
        self.send(author_id, "my brother gilgamesh is being a total dick")

        time.sleep(8)
        self.send(author_id, "every night this guy sends his band of misfits over to stock up on our hard earned resources")

        time.sleep(10)
        self.send(author_id, "these assholes drink all our water, eat everything in the fridge, then run up the electric bill cuz they leave the door open")

        time.sleep(4)
        self.send(author_id, "well, not anymore!")

        time.sleep(5)
        self.send(author_id, "this time we're gonna stick it to those sumerian fucks!")

        time.sleep(8)
        self.send(author_id, "ol' gillie's been on the run lately, and I need you to track him down so we can give him a piece of our mind")

        time.sleep(6)
        self.send(author_id, "send me a link to his location on the map at (URL) and I'll be forever in your debt!") #TODO competition URL


    def sendNotMapMsg(self, author_id):
        time.sleep(3)
        self.send(author_id, "dude, the map! send me a link to the map!!")


    def sendNoQueryMsg(self, author_id):
        time.sleep(4)
        self.send(author_id, "you didn't send me a location! just click a country and send me the link")


    def sendLegitMsg(self, author_id):
        time.sleep(4)
        self.send(author_id, "awesome, we'll check there. thanks for your help!")
        time.sleep(15)
        self.send(author_id, "huh, that's funny.. we can't get any signals from his ankle bracelet there. it doesn't look like he's hiding here.. any other ideas?")


    def sendNotEncodedMsg(self, author_id):
        time.sleep(5)
        self.send(author_id, "what's this junk on the end of the link? that ID looks like it has words.. what are you trying to pull?? no way in hell i'm clicking that!")


    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)

        # ignore self messages
        if str(author_id) == str(self.uid):
            return

        # if this is a new person, play intro message
        if str(author_id) not in self.seenUsers:
            self.playIntro(author_id)
            return

        # treat the message as a URL, and parse it
        components = urllib.parse.urlparse(message)
        print(components)

        # check that URL is valid
        # (URL is (http or https) and origin is on challenge site)
        try:
            assert ((components.scheme == 'http') | (components.scheme == 'https'))
            assert (components.netloc == '192.168.132.145') #TODO competition
            assert ((components.path == '/') | (components.path == '/index.php'))
        except AssertionError:
            self.sendNotMapMsg(author_id)
            return

        # check that a map location is specified
        try:
            assert (components.query)
        except AssertionError:
            self.sendNoQueryMsg(author_id)
            return

        # check if the location is legit or a payload
        if (components.query.isnumeric()):
            self.sendLegitMsg(author_id)
            return

        # check that payload is completely URL-encoded
        try:
            unEncoded = urllib.parse.unquote_plus(components.query)
            allEncoded = urlEncodeAllChars(unEncoded)
            assert (components.query == allEncoded)
        except AssertionError:
            self.sendNotEncodedMsg(author_id)
            return

        # open the URL in the browser
        try:
            subprocess.run(['firefox', components.geturl()], shell=False, timeout=10)
        except subprocess.TimeoutExpired:
            pass


def urlEncodeAllChars(string):
    result = ''
    for char in string:
        result += '%' + format(ord(char), 'x')
    return result

with open('fbcreds', 'r') as credfile:
    creds = credfile.read()
    
bot = ChallengeBot("girugamessage@yahoo.com", creds)
bot.listen()
