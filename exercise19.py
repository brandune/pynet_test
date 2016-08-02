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

def get_vendor(show_vers):
    list_show_vers = show_vers.split('\n')
    info_string = list_show_vers[0]
    vendor = info_string.split()[0]
    return vendor

def get_model(show_vers):
    list_show_vers = show_vers.split('\n')
    info_string = list_show_vers[0]
    model = info_string.split()[3]
    return model

def get_os_vers(show_vers):
    list_show_vers = show_vers.split('\n')
    info_string = list_show_vers[0]
    os_vers = info_string.split()[7]
    os_vers = os_vers.rstrip(',')
    return os_vers

def get_uptime(show_vers):
    list_show_vers = show_vers.split('\n')
    for line in list_show_vers:
        if 'uptime' in line:
            uptime = line.split('uptime is ')[1]
            return uptime
filename = 'data_show_version.txt'
show_vers = get_show_vers(filename)
serial_num = get_serial_num(show_vers)
vendor = get_vendor(show_vers)
model = get_model(show_vers)
os_vers = get_os_vers(show_vers)
uptime = get_uptime(show_vers)

print serial_num
print vendor
print model
print os_vers
print uptime
