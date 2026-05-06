#permutation is specific the arrangement of the element tis called the permutation

#suffling means changing the arrangment of the array elements



#array ki arrange ment ko shufle kar ke dikhaye ga
# from numpy import random
# import numpy as np

# arr=np.array([1,2,3,4])

# random.shuffle(arr)
# print(arr)


#we can shuffle the array using the permutation formula
from numpy import random
import numpy as np

arr=np.array([1,2,3,4])
print(random.permutation(arr))