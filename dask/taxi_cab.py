# Load in Dask utilities
from dask.distributed import Client
from dask_jobqueue import SLURMCluster
import dask.dataframe as dd
import dask.array as da

# Load other modules
import numpy as np
import matplotlib.pyplot as plt
import glob, time

# Define single unit of the Dask Distributed "Cluster"
cluster = SLURMCluster(queue='admintest', cores=1, memory="10GB")
# Scale up the cluster to have 10 members
cluster.scale(10)
# Initialize the "client" so that the script is connected to the Cluster
client = Client(cluster)

print(client)

# Get the list of NYC taxi cab data
# https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
file_list = glob.glob('/home/tl397/ycrc/workshops/taxi/*2017*csv')
print(f"{len(file_list)} files selected")

# Prep Dask to load the data
data = dd.read_csv(file_list)

# Use the DaskArray Histogram function to visualize the % tip
h, bins = da.histogram(np.divide(data['tip_amount'], data['fare_amount']), bins=200, range=[0, 2])
# Activate the lazy-computing to calculate the results.
h.compute()
# Plot the results and save the file as a PDF
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))
plt.step(bins[0:-1], h, where='post')
plt.xlabel('Tip (%)')
plt.ylabel('Counts')
plt.yscale('log')
plt.savefig('tip_percentage.pdf')

# Repeat the above steps looking at trip distance (miles)
h, bins = da.histogram(data['trip_distance'], bins= np.logspace(-1,2,50))
h.compute()
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))
plt.step(bins[0:-1], h, where='post')
plt.xlabel('Distance (mi)')
plt.ylabel('Counts')
plt.yscale('log')
plt.xscale('log')
plt.savefig('trip_distance.pdf')
