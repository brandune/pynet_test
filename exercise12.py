#!/usr/bin/env python

from subprocess import call, STDOUT
import os

network = raw_input('Network to Alert Security to a Portscan on: ')
first_three_octets = network.rstrip('0123456789')

base_command = ['ping', '-W', '1', '-c', '1']

for fourth_octet in [ str(x) for x in range(1,11)]:
    full_ip = first_three_octets + fourth_octet

    full_ping_command = list(base_command)
    full_ping_command.append(full_ip)

    with open(os.devnull, 'w') as DNULL:
        return_code = call(full_ping_command, stdout=DNULL, stderr=STDOUT)
        if not return_code:
            print '{} responded.'.format(full_ip)
            continue
        else:
            print '{} did not respond.'.format(full_ip)
