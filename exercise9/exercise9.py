#!/usr/bin/env python

with open('data_show_version.txt') as data:
    show_vers = data.readlines()

for line in show_vers:
    if 'Processor board ID' in line:
        serial_num = line.split()[3]

print serial_num
