from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size() # new: gives number of ranks in comm
rank = comm.Get_rank()

numData = 100000000
data = None
if rank == 0:
    data = np.random.normal(loc=10, scale=5, size=numData)

partial = np.empty(int(numData/size), dtype='d')
comm.Scatter(data, partial, root=0)

reduced = None
if rank == 0:
    reduced = np.empty(size, dtype='d')

comm.Gather(np.average(partial), reduced, root=0)

if rank == 0:
   print('Full Average:',np.average(reduced))

