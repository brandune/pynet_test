#!/usr/bin/env python

import pyeapi
from pprint import pprint

pyeapi.load_config("nodes.conf")
switch = pyeapi.connect_to('pynet-sw3')

data_returned = switch.enable('show ip route')

routes = data_returned[0]['result']['vrfs']['default']['routes']

print '{:<16} {:<13} {:<12}'.format('Prefixes', 'Egress Intf.', 'Next Hop IP')
for route in routes:
    prefix = route
    egress_int = routes[route]['vias'][0].get('interface')
    next_hop = routes[route]['vias'][0].get('nexthopAddr')
    print '{:<16} {:<13} {:<12}'.format(prefix, egress_int, next_hop)
