#Poisson Distribution

#Poission Distribution is the discrete Distribution

# It estimate how many time one event occors in a specific time
# if one person eat twice at a day what is the probibulity

#lam rale of number of occurance eg two for above problem
#size that the array return 

#genrate the random occurance 1*10 distribution of accurence 2
# from numpy import random
# x=random.poisson(lam=2,size=10)# in this occurence of the number is 2 in the 2 occor the most
# print(x)

#visulize the potion Distribution
# import matplotlib.pyplot as plt
# import seaborn as sns
# from numpy import random

# x=random.poisson(lam=2,size=10)
# sns.displot(x)
# plt.show()

#Difference between the Normal and the Poisson

#there the normal is contigus and the poisson is discret

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data={
    "normal":random.normal(loc=50,scale=7,size=1000),
    "poisson":random.poisson(lam=5o,size=1000)
}

sns.displot(data,kind="kde")
plt.show()