#!/usr/bin/env python

import netmiko
from ciscoconfparse import CiscoConfParse
cisco_router = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass'
}


cisco_connect = netmiko.ConnectHandler(**cisco_router)
cisco_connect.enable()

raw_conf = cisco_connect.send_command_expect('show runn')
raw_conf_list = raw_conf.splitlines()
trimmed_conf = raw_conf_list[7:-2]

parsed_conf = CiscoConfParse(trimmed_conf)
no_ips = parsed_conf.find_objects_wo_child(r'interface', r'no ip address')

print no_ips

