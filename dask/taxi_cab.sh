#!/bin/bash

#SBATCH -J dask
#SBATCH -c1 -p admintest

module load dask

python taxi_cab.py  

