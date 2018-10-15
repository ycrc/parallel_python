from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size() # new: gives number of ranks in comm
rank = comm.Get_rank()

numDataPerRank = 100000000
data = None
if rank == 0:
#    data = np.linspace(1,size*numDataPerRank,numDataPerRank*size)
    data = np.random.normal(loc=10, scale=5, size=numDataPerRank*size)

partial = np.empty(numDataPerRank, dtype='d')
comm.Scatter(data, partial, root=0)

#partial = np.add(partial, np.ones(numDataPerRank))

#print('rank',rank,'has data:',partial)

reduced = None
if rank == 0:
    reduced = np.empty(size, dtype='d')
#    print(f'Rank: {rank}, reduced: {reduced}')

comm.Gather(np.average(partial), reduced, root=0)

if rank == 0:
   print('Full Average:',np.average(reduced))

