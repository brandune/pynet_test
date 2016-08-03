#!/usr/bin/env python

def get_show_vers(filename):
    with open(filename) as data:
        return data.read()

def get_serial_num(show_vers):
    list_show_vers = show_vers.split('\n')
    for line in list_show_vers:
        if 'Processor board ID' in line:
            serial_num = line.split()[3]
            return serial_num

filename = 'data_show_version.txt'
show_vers = get_show_vers(filename)
serial_num = get_serial_num(show_vers)

print serial_num
