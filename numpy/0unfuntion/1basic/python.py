#ufuncs stand for the universel function the operate the ndarray object

#unfuncs is use for the vectorization in num by which is very fact of the iterative  and over element

#that offer more multiple featuer like the reduce accumulate and that is very helpfull computation

#some operations
#where bool array define the condition where the operation will take  place
#dtype define the return type of the lement
# out output array should be copied

#what is vectorization
#convert the iterative statement into the vector

#add the elment of two list
#list 1 : 1,2,3,4
#list 2 : 5,6,7,8

# x=[1,2,3,4,5]
# y=[5,6,7,8,9]
# z=[]

# for i,j in zip(x,y):
#     z.append(i+j)
# print(z)

#this is the some of two lists
# x=[1,2,3,4,5]
# y=[6,7,8,9,10]
# z=[]

# for i,j in zip(x,y):
#     z.append(i+j)
# print(z)

#we have the add function
# import numpy as np
# x=[1,2,3,4]
# y=[2,3,4,5]
# z=np.add(x,y)
# print(z)

# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# x=np.array([1,2,3,4])
# y=np.array([3,4,5,6])
# z=add(x,y) // this is the function of the ufunc
# print(z)
# sns.displot(z,kind="kte")
# plt.show()


#add two list
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x=np.array([1,2,3,4,5])
y=np.array([14,5,6,7,22])
z=[]

for i,j in zip(x,y):
    z.append(i+j)
print(z)

sns.displot(z,kind="Kde")
plt.show()