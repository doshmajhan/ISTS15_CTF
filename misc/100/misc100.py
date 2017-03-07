#!/usr/bin/python

import socket
import threading
from ipaddress import IPv4Address, IPv4Network, IPv4Interface

bind_ip = ''
bind_port = 9999

net1 = IPv4Network(u'10.2.0.0/16')
net2 = IPv4Network(u'10.3.0.0/16')


def handle_client(client_socket, addr):
    request = client_socket.recv(1024)
    try:
        fields = request.split(":")
        ip = fields[0]
        port = int(fields[1])
        net = IPv4Interface(unicode(addr + "/24"))
    except:
        client_socket.send("Invalid IP, closing connection")
        client_socket.close()
    if (IPv4Address(unicode(ip)) not in net.network):
        client_socket.send("Invalid IP, closing connection")
        client_socket.close()
    else:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip, port))
            client.send("ZmxhZ3tUaDRuazVfMGI0bTR9")
            client_socket.close()
        except:
            client_socket.send("Could not connect")
            client_socket.close()
        
        
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip, bind_port)

while True:
    client, addr = server.accept()
    address = IPv4Address(unicode(addr[0]))
    if (address not in net1 and address not in net2):
        print "[*] Closed connection from %s:%d" % (addr[0], addr[1])
        client.close()
        continue
    print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client,args=(client,addr[0]))
    client_handler.start()
