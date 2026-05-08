#create the normal fucntion 
#createt the normal fucntion is also like the default fucntion that we create in the py
# using the def keyword 

#numpy also give a fcution that is like 
#frompyfunc()

#there are some specific attributie of the fuction 
# fuction The name of the fuction 
# imput the number of impout arguments
# #output nubmer of the  output arrays

# import numpy as np

# def mysum(x+y):
#     return x+y

# x=np.frompyfunc(mysum,2,1)
# print(x([1,2,3,4,5],[6,7,8,9,3]))


# check the unfunc or not
# here add is the pre defined fuction
# import numpy as np
# if type(np.add)==np.ufunc: #ufunc stand for the universel fucntion
#     print("add is ufunc")
# else:
#     print("Not the ufunc")

# import numpy as np

# def myfunc(x,y):
#     return x + y

# x=np.frompyfunc(myfunc,2,1)
# print(x([1,2,3,4,5],[3,4,5,3,3]))