#!/usr/bin/env python

def three_params(x, y, z=20):
    return x + y + z

three_pos_args = str(three_params(1, 2, 3))
print 'Three Pos Args: {}'.format(three_pos_args)

three_named_args = str(three_params(x=1, y=2, z=4))
print 'Three Named Args: {}'.format(three_named_args)

one_pos_two_name = str(three_params(1, 3, z=14))
print 'One Pos, Two Named Args: {}'.format(one_pos_two_name)

three_strings = three_params(x='flibble', y='de', z='bits')
print 'Three String Args: {}'.format(three_strings)

three_lists = str(three_params(x=['item1'], y=['item2'], z=['item3']))
print 'Three List Args: {}'.format(three_lists)
