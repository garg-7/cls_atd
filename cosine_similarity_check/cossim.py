from numpy import dot
from numpy.linalg import norm

import numpy as np


fday = open('listday.txt','r')
for k in fday:
    day = k
    day = day.replace('.jpg\n', '.feat')
    # print(day)
    fp1 = open('day/'+(day), 'rb')
    feat1 = np.fromfile('day/'+(day), dtype = '<f', count = -1)
    #sprint(day.replace('.feat',''))
    maxsim = 0
    maxsim_name = 'NULL'
    fstd = open('liststd.txt','r')
    for j in fstd:
        std = j
        std = std.replace('.jpg\n','.feat')
        fp2 = open('standard_features/'+(std),'rb')
        feat2 = np.fromfile('standard_features/'+(std), dtype = '<f', count = -1)
        cos_sim = abs(dot(feat1, feat2) / (norm(feat1) * norm(feat2)))
        #print(cos_sim)
        if (cos_sim)>(maxsim):
            maxsim = cos_sim
            maxsim_name = std
    fstd.close()
    print(day.replace('.feat','')+" - " + maxsim_name.replace('f.feat',''))
    print(maxsim)
