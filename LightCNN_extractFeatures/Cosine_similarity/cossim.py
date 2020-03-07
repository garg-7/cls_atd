from numpy import dot
from numpy.linalg import norm

import numpy as np

fp1 = open('1.feat','rb')

fp2 = open('1.1.feat','rb')

feat1 = np.fromfile('1.1.feat', dtype = '<f', count = -1)
feat2 = np.fromfile('1.feat', dtype = '<f', count = -1)

cos_sim = cosine_similarity( feat1, feat2 )

print(cos_sim)