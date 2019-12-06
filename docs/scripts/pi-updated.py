#!/usr/bin/env python3
from random import random as r
from math import pow as p
from sys import argv

# Use argparse to take command line options and generate help text
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", help="number of random points (int)", type=int)
args = parser.parse_args()

# Grab number of attempts from command line
attempts = args.number
inside=0
tries=0
ratio=0.

# Try the specified number of random points
while (tries < attempts):
    tries += 1
    if (p(r(),2) + p(r(),2) < 1):
        inside += 1

# Compute and print a final ratio
ratio=4.*(inside/(tries))
print("Final pi estimate from", attempts, "attempts =", ratio)
