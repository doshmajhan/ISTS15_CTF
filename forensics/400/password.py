#!/usr/bin/python

from scapy.all import *

password = ['p','d','f','s','a','r','e','h','a','r','d','1','2','3','4']

for c in password:
	send(IP(src="10.1.99.100", dst="10.1.99.2", ttl=128)/ICMP()/c)