#iterate the 1D array

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# for x in arr:
#     print(x)

#iterate the 2D array
import numpy as np
arr=np.array([1,2,3,4],[5,6,7,8])
for x in arr:
    for y in x:
        print(y)