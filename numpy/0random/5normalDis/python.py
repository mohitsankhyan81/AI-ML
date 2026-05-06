#Normal Disribution

#Normal disribution is one of the important distribution

#We use the normal distribution like 
#random.normal()

#there are three types of the normal distribution like
# loc -> Mean
# scale -> Standard Devision
# size -> return the size of the array

#create the random distribution of the 2*3 size
# from numpy import random
# x=random.normal(size=(2,3)) #normaly distributioon create kar dega 2*3 size ki
# print(x)

#create the random distribution with the size 2*3 and the mean 1 and standard divistion of 2
# from numpy import random
# x=random.normal(loc=1,scale=2,size=(2,3))
# print(x)

#visulize the normal disribution 
# import matplotlib.pyplot as plt
# import seaborn as sns
# from numpy import random
# sns.displot(random.normal(size=1000),kind="kde") # ye bell shape me hota hai iss liye isse bell shaped curve bhi bol dete hai
# plt.show()

