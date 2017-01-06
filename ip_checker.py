#!/usr/bin/env python

'''
Python for Network Engineers
https://pynet.twb-tech.com
Instructor Kirk Byers
Script by mattatwork 01-02-2016
Week 4, Exercise I: Valid IP Checker part II, Looping User Input Prompt
	-Prompt user for IP address
	-Continue prompting until the following conditions are met:
		-IP has four octets
		-First octet is between 1 - 223
		-First octet != 127
		-IP address cannot be in 169.254.X.X range
		-Last three octets are in the 0 - 255 range
	-If IP is valid:
		-output print IP address and valid statement
'''

# intialize while loop
while True:

    # Prompt user for IP address
    ip_addr = raw_input("Enter an IP address: ")
    octets = ip_addr.split(".")

    # len(octets) is four
    if len(octets) != 4:
        print "A valip IP requires four octets. "
        continue

    # convert octet list to integers
    i = 0
    for octet in octets:
        octets[i] = int(octet)
        i += 1

    # evaluate octets[0] in 1 - 223 range
    if octets[0] < 1 or octets[0] > 223:
        print "First octet not in 1 - 223 range."
        continue
    
    # evaluate octets[0] != 127
    if octets[0] == 127:
        print "First octet cannot be 127."
        continue

    # evaluate octets[0] != 169 and octets[1] != 254    
    if octets[0] == 169 and octets[1] == 254:
        print "169.254.X.X range is invalid."
        continue

    # evaluate octets[1] in 0 - 255 range
    if octets[1] < 0 or octets[1] > 255:
        print "Second octet not in 0 - 255 range."
        continue

    # evaluate octets[2] in 0 - 255 range
    if octets[2] < 0 or octets[2] > 255:
        print "Third octet not in 0 - 255 range."
        continue

    # evaluate octets[3] in 0 - 255 range
    if octets[3] < 0 or octets[3] > 255:
        print "Fourth octet not in 0 - 255 range."
        continue

    break

print "IP %s is valid!" % ip_addr
