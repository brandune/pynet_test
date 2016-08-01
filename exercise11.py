#!/usr/bin/env python

the_list = range(1,50)

for number in the_list:
    if number == 13:
        continue
    elif number == 39:
        break
    else:
        print number
