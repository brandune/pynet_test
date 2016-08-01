#!/usr/bin/env python

with open('data_show_bgp.txt') as data_file:
    show_bgp = data_file.readlines()

starting_index = 0
for index, line in enumerate(show_bgp):
    if 'LocPrf' in line:
        starting_index = index + 1
        break

route_table = show_bgp[starting_index:]

print '{:<14} {:<}'.format('Route', 'AS Path')
for route in route_table:
    parted_line = route.split()
    route = parted_line[1]
    as_path = ' '.join(parted_line[5:-1])
    print '{:<14} {:<}'.format(route, as_path)
