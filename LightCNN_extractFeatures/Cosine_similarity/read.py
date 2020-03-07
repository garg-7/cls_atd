import numpy as np

fp = open('1.1.feat', 'rb')

features=list()

features = (np.fromfile('1.1.feat', dtype = '<f', count = -1))

print(features)

# print('\n')
# print(features.size)