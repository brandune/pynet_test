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

output_dict = { 
    'Serial Number': get_serial_num(show_vers),
    'Vendor': get_vendor(show_vers),
    'Model': get_model(show_vers),
    'OS Version': get_os_vers(show_vers),
    'Uptime': get_uptime(show_vers)
}

for key, value in output_dict.items():
    print '{:<14}: {}'.format(key, value)

