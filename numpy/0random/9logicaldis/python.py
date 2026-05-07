#logical distributin is use for describe the growth

#ye bahut hi jada use hota hai mechine lerning ke logical regression me or newral network me
#isme bhi 3 perimiter hote hai 
# size -> jo rray ka return size hoga
# loc -> loc describe the peak defult zero
# scale -> scale define the faltness and that is defult one

# from numpy import random
# x=random.logistics(loc=1,scale=2,size=1000) # aise use hota hai
# print(x)

# from numpy import random #this is use to discribe the growth of the data
# x=random.logistics(loc=0,scale=33,size=1000) # isme maine peak 0 diya hai
# print(x)

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.logistic(loc=0,scale=35,size=1000)) the default peak of the loc is 0 and the defult peak of the scale is 1
# plt.show()

#diffrent between the normal distribution and the logistic distribution
#normal distributioon define the contigus behaviur of the data what the game perimeter like loc scale and size
#where the logistic distrbution is use for the described growth of the clss
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# data={
#     "normal":random.normal(loc=1,scale=5,size=1000),
#     "logistic":random.logistic(loc=1,scale=5,size=1000)
# } #we used both the normal and logistic but the graph of the normal distribution look more balanced

# sns.displot(data)
# plt.show()