#make the array filtered

import numpy as np
arr1=np.array([1,2,3,4,5,6])
x=arr1[[True,False,True,False,True,False]]
print(x)






import numpy as np
arr1=np.array([1,2,3,4])
x=arr1[[True,False,False,True]]
print(x)