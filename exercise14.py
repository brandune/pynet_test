#!/usr/bin/env python

network_device = {}
network_device['ip_address'] = '10.0.0.1'
network_device['username'] = 'brandune'
network_device['password'] = 'flibble'
network_device['vendor'] = 'Junaristcoiquitiulus'
network_device['model'] = 'EX-ChalupaSupreme'

for param, value in network_device.items():
    print '{:<10} is {:<10}'.format(param, value)

network_device['password'] = 'flibble1'

for param, value in network_device.items():
    print '{:<10} is {:<10}'.format(param, value)


print network_device.get('device_type', 'cisco_ios')
