#!/usr/bin/env python

import socket
import paramiko
import threading
import time
from ipaddress import IPv4Address, IPv4Network, IPv4Interface

bind_ip = ''
bind_port = 9999

net1 = IPv4Network(u'10.2.0.0/16')
net2 = IPv4Network(u'10.3.0.0/16')

banner1 = "NEVER GONNA GIVE YOU UP"
banner2 = "NEVER GONNA LET YOU DOWN"
banner3 = "NEVER GONNA RUN AROUND"
banner4 = "AND DESERT YOU"


def ftp_banner(addr):
    s = socket.socket()
    s.settimeout(5)
    try:
        s.connect((addr,21))
        banner = s.recv(1024)
    except:
        return False
    if (banner1 in banner):
        return True
    return False

    
def ssh_banner(addr):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(addr, port=22, username='username', password='bad-password-on-purpose')
    except:
        try:
            banner = client._transport.get_banner()
        except:
            return False
        if (banner2 in banner):
            return True
        return False

        
def pop_banner(addr):
    s = socket.socket()
    s.settimeout(5)
    try:
        s.connect((addr,110))
        banner = s.recv(1024)
    except:
        return False
    if (banner3 in banner):
        return True
    return False

    
def qotd_banner(addr):
    s = socket.socket()
    s.settimeout(5)
    try:
        s.connect((addr,17))
        banner = s.recv(1024)
    except:
        return False
    if (banner4 in banner):
        return True
    return False

    
def handle_client(client_socket, addr):
    network = addr[:addr.rindex('.')]
    addr1 = network + ".20"
    addr2 = network + ".30"
    addr3 = network + ".40"
    addr4 = network + ".50"

    client_socket.send("It's time to play...")
    time.sleep(2)
    client_socket.send("...BANNER KARAOKE!!!\n")
    time.sleep(2)

    client_socket.send("[*] Checking {} for ftp service banner \"{}\"\n".format(addr1, banner1))
    b1 = ftp_banner(addr1)
    if b1:
        client_socket.send("[*] Success\n")
    else:
        client_socket.send("[*] Failure\n")

    client_socket.send("[*] Checking {} for ssh service banner \"{}\"\n".format(addr2, banner2))
    b2 = ssh_banner(addr2)
    if b2:
        client_socket.send("[*] Success\n")
    else:
        client_socket.send("[*] Failure\n")

    client_socket.send("[*] Checking {} for POP service banner \"{}\"\n".format(addr3, banner3))
    b3 = pop_banner(addr3)
    if b3:
        client_socket.send("[*] Success\n")
    else:
        client_socket.send("[*] Failure\n")

    client_socket.send("[*] Checking {} for QOTD service banner \"{}\"\n".format(addr4, banner4))
    b4 = qotd_banner(addr4)
    if b4:
        client_socket.send("[*] Success\n")
    else:
        client_socket.send("[*] Failure\n")

    if b1 and b2 and b3 and b4:
        client_socket.send("flag{R1CK_45TLY_4EVR}")
    else:
        client_socket.send("No flag for you.")
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

while True:
    client, addr = server.accept()
    address = IPv4Address(unicode(addr[0]))
    if (address not in net1 and address not in net2):
        continue
    print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client,args=(client,str(address),))
    client_handler.start()
