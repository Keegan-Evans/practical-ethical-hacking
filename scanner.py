#!/bin/python

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4A
else:
    print("invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")


#Add banner
print("-"*50)
print("scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) #returns error indicator-a 1
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("couldn't connect ot server.")
    sys.exit()
