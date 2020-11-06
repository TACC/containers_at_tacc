#!/usr/bin/env python3
import mpi4py
mpi4py.rc.recv_mprobe = False
from mpi4py import MPI
from socket import gethostname
from random import random as r
from math import pow as p
from sys import argv
from time import time

# Baseline for PI
PI25DT = 3.141592653589793238462643

# Initialize MPI stuff
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Make sure number of attempts (per rank) is given on command line
assert len(argv) == 2
attempts = int(argv[1])
local_attempts = int(attempts/size)
if rank == 0:
	print("\nComputing %i samples on each of the %i ranks\n"%(local_attempts, size), flush=True)
comm.Barrier()
inside=0.
tries=0
final=0.

start_time = time()
# Each rank tries the same number of times
while (tries < local_attempts):
	tries += 1
	if (p(r(),2) + p(r(),2) < 1):
		inside += 1

# Each rank computes a final ratio (float)
ratio=4.*(inside/float(local_attempts))
print("[%s-%02d] Local Estimate: %.16f   Error: %.16f" % (gethostname(), rank, ratio, abs(ratio-PI25DT)), flush=True)

final_pi = comm.reduce(ratio, op=MPI.SUM, root=0)
total_time = time()-start_time

# Print the final average from rank 0
if rank == 0:
	final_pi = final_pi/float(size)
	print("\nFinished computing %i samples in %.3f secnods"%(size*local_attempts, total_time))
	print("\nFinal Estimate: %.16f   Error: %.16f"%(final_pi, abs(final_pi-PI25DT)))
