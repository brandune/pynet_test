#!/usr/bin/env python

network_device = {}
network_device['ip_address'] = '10.0.0.1'
network_device['username'] = 'brandune'
network_device['password'] = 'flibble'
network_device['vendor'] = 'Junaristcoiquitiulus'
network_device['model'] = 'EX-ChalupaSupreme'

for param, value in network_device.items():
    print '{:<10} is {:<10}'.format(param, value)
else:
    print

network_device['password'] = 'flibble1'
network_device['secret'] = 'keepItSafe'

for param, value in network_device.items():
    print '{:<10} is {:<10}'.format(param, value)
else:
    print


print network_device.get('device_type', 'cisco_ios')
