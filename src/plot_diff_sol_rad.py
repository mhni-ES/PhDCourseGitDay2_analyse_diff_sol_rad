import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
num_measurements = 24
filename = 'r20210601-20210630-UTC'
## Make a reader module that can read file given names easier and give the data back
# read data from file r20210601-20210630-UTC.csv
#data = pd.read_csv('../data/diffuse_sol_rad/r20210601-20210630-UTC.csv', nrows=num_measurements)
#diff_sol_rad = data['Diffuse radiation (W/m2)']

def load_data(filename,num_meas):
     data = pd.read_csv('../data/diffuse_sol_rad/'+filename, nrows=num_meas)
     if  '-' in data.values:
        data = data.replace('-', np.nan)

     return data['Diffuse radiation (W/m2)']

# make a function that makes the mean easier.
# compute statistics
#mean = sum(diff_sol_rad)/num_measurements

def mean(x,n):
    if np.isnan(x.astype(float)).any() == True:
        mean_out = np.nansum(x.astype(float))/n
    else :
        mean_out = sum(x)/n
    return mean_out

# make a plotter script that can plot multiple scripts.


if __name__ == "__main__":
    for filename in os.listdir('../data/diffuse_sol_rad/'):
        #print(filename)
        diff_sol_rad = load_data(filename,num_measurements)
        mean_out = mean(diff_sol_rad,num_measurements)
        # plot results
        savename = filename.split("-")
        plt.plot(diff_sol_rad)
        plt.axhline(y=mean_out, color='b', linestyle='--')
        plt.savefig('../processed_data/'+savename[0]+'.png')
        plt.clf()