#join two array

# import numpy as np
# arr1=np.array([1,2,3]);
# arr2=np.array([4,5,6]);
# arr=np.concatenate((arr1,arr2));
# print(arr);

#join array with axis

# import numpy as np
# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# arr=np.concatenate((arr1,arr2),axis=1)
# print(arr)

#join array with axis
#stack is also like the concat but it is concat the 1D array and we give the axis where the data is done
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.stack((arr1,arr2),axis=1)
# print(arr)

#stacking along the line and horigontal line 
#hstack is use for the horigonty add
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.hstack((arr1,arr2))
# print(arr)

#vstack we use for verticle stacking
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([2,4,5])
# arr=np.vstack((arr1,arr2))
# print(arr)

#dstack do along the hight
# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.dstack((arr1,arr2))
# print(arr)