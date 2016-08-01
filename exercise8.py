#!/usr/bin/env python

base_list = [1, 2, 3, 4, 5]
print 'Base list:'
print str(base_list) + '\n'


base_list.append(6)
base_list.append(7)
print 'Appended list:'
print str(base_list) + '\n' 

base_list.pop(0)
print 'Popped list:'
print str(base_list) + '\n' 

length = len(base_list)
print 'List length:'
print length
