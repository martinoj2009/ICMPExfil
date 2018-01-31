# Packet sniffer in python for Linux
# Sniffs only incoming TCP packet
import signal
import socket
import sys
from datetime import datetime as dTime
from os import getuid
from struct import *

# Before we even start make sure we are running as root
if getuid() != 0:
    print("\nPlease run as root... Exiting\n")
    sys.exit(-1)

communications = dict()

def signal_handler(signal, frame):
    lastTime = None
    first = True
    binary = list()
    # Get timeoffsets
    print("Calculating offsets")
    for com, value in communications.items():
        for date in value:
            if first:
                lastTime = date
                first = False
            else:
                binary.append((lastTime - date).total_seconds())
                lastTime = date

    # Remove every other entry
    on = False
    num = 0
    raw = ""
    ascii = ""
    for entry in binary:
        if not on:
            on = True
        else:
            if num == 7:
                raw += " " + str(round(abs(entry)))
                on = False
                num = 1
            else:
                raw += str(round(abs(entry)))
                on = False
                num = num + 1

    for word in raw.split(" "):
        ascii += chr(int(word[:8], 2)) + " "

    print("\n")
    print(ascii)
    #print(raw)
    sys.exit(0)

# This will listen for the control+c
signal.signal(signal.SIGINT, signal_handler)


# create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
except socket.error as msg:
    print(
    'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# receive a packet
while True:
    packet = s.recvfrom(65565)

    # packet string from tuple
    packet = packet[0]

    # take first 20 characters for the ip header
    ip_header = packet[0:20]

    # now unpack them :)
    iph = unpack('!BBHHHBBH4s4s', ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF

    iph_length = ihl * 4

    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8])
    d_addr = socket.inet_ntoa(iph[9])

    if str(s_addr) in communications:
        communications[str(s_addr)].append(dTime.now())
    else:
        communications[str(s_addr)] = [dTime.now()]

    print(' Source Address : ' + str(s_addr))

    print(communications)




