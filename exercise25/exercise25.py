#!/usr/bin/env python

import netmiko

def get_show_version(handler):
    output = handler.send_command("show version")
    return output

def get_show_run(handler):
    output = handler.send_command_expect("show run")
    return output

cisco_router = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass'
}

arista_switch = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.74',
    'username': 'eapi',
    'password': 'ZZteslaX'
}

cisco_connect = netmiko.ConnectHandler(**cisco_router)
cisco_connect.enable()

arista_connect = netmiko.ConnectHandler(**arista_switch)
arista_connect.enable()

cisco_version = get_show_version(cisco_connect)
cisco_run = get_show_run(cisco_connect)

arista_version = get_show_version(arista_connect)
arista_run = get_show_run(arista_connect)

print 'Cisco Version:\n{}\n'.format(cisco_version)
print 'Arista Version:\n{}\n'.format(arista_version)


with open('cisco_conf.txt', 'w') as file_out:
    file_out.write(cisco_run)

with open('arista_conf.txt', 'w') as file_out:
    file_out.write(arista_run)
