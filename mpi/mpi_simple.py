from mpi4py import MPI
import os

# instantize the communication world
comm = MPI.COMM_WORLD

# get the size of the communication world 
size = comm.Get_size()

# get this particular processes' `rank` ID
rank = comm.Get_rank()

PID = os.getpid()

print(f'rank: {rank} has PID: {PID}')


