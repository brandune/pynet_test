#!/usr/bin/env python

import netmiko

arista_switch = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.74',
    'username': 'eapi',
    'password': 'ZZteslaX'
}

arista_connect = netmiko.ConnectHandler(**arista_switch)
arista_connect.enable()

vlan_conf = [
    'configure terminal',
    'vlan 783',
    'name brandons_vlan',
    'end',
]

output_783 = arista_connect.send_config_set(vlan_conf)
output_784 = arista_connect.send_config_from_file('vlan784.txt')

print output_783
print output_784
