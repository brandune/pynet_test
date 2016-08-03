#!/usr/bin/env python

import pyeapi
from pprint import pprint

pyeapi.load_config("nodes.conf")
switch = pyeapi.connect_to('pynet-sw3')

data_returned = switch.enable('show interfaces')

interfaces = data_returned[0].get("result").get('interfaces')

for interface, data in interfaces.items():
    if not data.get('interfaceCounters'):
        del interfaces[interface]

print '{:<12} {:<9} {:<9}'.format('Interface','inOctets','outOctets')
for interface, data in interfaces.items():
    in_octets = data['interfaceCounters']['inOctets']
    out_octets = data['interfaceCounters']['outOctets']
    print '{:<12} {:<9} {:<9}'.format(interface, in_octets, out_octets)
