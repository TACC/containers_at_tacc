#!/usr/bin/env python3
from random import random as r
from math import pow as p
from sys import argv

# Make sure number of attempts is given on command line
assert len(argv) == 2
attempts = int(argv[1])
inside = 0
tries = 0

# Try the specified number of random points
while (tries < attempts):
    tries += 1
    if (p(r(),2) + p(r(),2) < 1):
        inside += 1

# Compute and print a final ratio
print( f'Final pi estimate from {attempts} attempts = {4*(inside/tries)}' )
