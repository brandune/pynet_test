#!/usr/bin/env python

with open('data_exercise5.txt') as first_data:
    first_data_contents = first_data.readlines()

for line in first_data_contents:
    print line,

with open('data_exercise5_out.txt', 'w') as second_data:
    line1 = 'this is the first output line\n'
    line2 = 'this is the second output line\n'
    second_data.write(line1)
    second_data.write(line2)

with open('data_exercise5_out.txt', 'a') as second_data:
    line3 = 'this is the third output line\n'
    second_data.write(line3)

