import numpy as np
mlist = [[1, 2 , 3], [3, 3 , 3]]

print(np.zeros((10, 10, 3), dtype=np.uint8))
x = np.zeros((10, 10, 3))

print(np.array(x).reshape(-1, *x))
print(np.reshape(-1, *mlist))

