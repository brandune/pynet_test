#!/usr/bin/env python

ip = raw_input("IP Address: ")
octets = ip.split('.')
octets[3] = "0"

print '{:<6} {:<8} {:<}'.format('Octet', 'Decimal', 'Binary')
for index, octet in enumerate(octets):
    octet_num = index + 1
    print '{:<6} {:<8} {:<}'.format(octet_num, octet, bin(int(octet)))
