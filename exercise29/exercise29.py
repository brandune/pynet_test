#!/usr/bin/env python

import netmiko
import yaml
import sys

device_data_filename = 'device.yml'
with open(device_data_filename) as device_data:
    device_data_contents = device_data.read()

device_data_yaml = yaml.load(device_data_contents)
switch_info = device_data_yaml['pynet-sw3']

arista_connect = netmiko.ConnectHandler(**switch_info)

show_arp = arista_connect.send_command("show arp")

print show_arp
