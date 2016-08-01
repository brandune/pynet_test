#!/usr/bin/env python

ip = raw_input("IP Address: ")
octets = ip.split('.')

print '{:<3} {:<3} {:<3} {:<3}'.format(*octets)
