#!/usr/bin/env python3
import mpi4py
mpi4py.rc.recv_mprobe = False
from mpi4py import MPI
from socket import gethostname
from random import random as r
from math import pow as p
from sys import argv

# Initialize MPI stuff
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Make sure number of attempts (per rank) is given on command line
assert len(argv) == 2
attempts = int(argv[1])
inside=0.
tries=0
final=0.

# Each rank tries the same number of times
while (tries < attempts):
        tries += 1
        if (p(r(),2) + p(r(),2) < 1):
                inside += 1

# Each rank computes a final ratio (float)
ratio=4.*(inside/(tries))
print("[rank %02d of %d on host %s]: %.12f" % (rank, size, gethostname(), ratio))

# The 0 rank collects from all others and computes an average
if rank == 0:
        total = ratio
        for i in range(1, size):
                other = comm.recv(source=i)
                total += other
        final = total/size

# All other ranks just send the ratio to rank 0
else:
        comm.send(ratio, dest=0)

# Print the final average from rank 0
if rank == 0:
        print("")
        print("Final pi estimate from", size*attempts, "attempts =", final)
