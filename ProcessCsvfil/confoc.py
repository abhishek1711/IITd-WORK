import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(threshold=np.nan)
from scipy import stats
results = []
resi = []

with open("Raw_confocal_data_standard_sample.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats

    for row in reader: # each row is a list
         results.append(row)

for i in results:
   resi.append(i[0])

X = np.arange(1,10001)

X = np.array(X)

resi = np.array(resi)

plt.plot(X,resi)

n = len(resi)
print(n)

m = ((n*(np.sum(X*resi))) - ((np.sum(X)) * (np.sum(resi)))) / ((n * (np.sum(X*X))) - ((np.sum(X)) * (np.sum(X))))

c = (resi) - np.multiply(m,X)

c=abs(c)
print(c)

plt.plot(X,c)

sumabs = (np.sum(c) / n)

avgofc = c - sumabs
print(len(c))

avgofc = abs(avgofc)

k = np.sum(avgofc)
