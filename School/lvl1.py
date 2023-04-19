#!/usr/bin/env python3

def get_num_of_cells():
    with open('lvl1/level1_1.in', 'r') as f:
        return f.read().count('O')

print(get_num_of_cells())
