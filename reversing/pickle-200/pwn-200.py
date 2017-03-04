import pickle
import socketserver
import base64
import binascii

class DontHackMeBro(socketserver.BaseRequestHandler):
    def handle(self):
        s = self.request
        s.send(b"ohai! Send me some data!\n")
        data = s.recv(1024)
        try:
            out = pickle.loads(base64.b64decode(data))
        except binascii.Error as e:
            s.send(b"this isnt base64 data!")
            return
        s.send(b"What am I supposed to do with " + out)
        s.close()

def main():
    host = '0.0.0.0'
    port = 14623
    server = socketserver.ForkingTCPServer((host, port), DontHackMeBro)
    print("Running on {} port {}".format(host, port))
    server.serve_forever()

if __name__ == '__main__':
    main()

