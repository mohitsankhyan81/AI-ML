#binomal distribution is discreate distribution 

#in the binomial distribution there are 3 types
#n number of trails
#p probability of accouranpce of each trial
#size the shape of return array

# from numpy import random
# x=random.binomial(n=10,p=0.5,size=10)
# print(x)

#visulize using the matplot lib
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.binomal(n=10,p=0.5,size=10))
# plt.show()

#Difference between the normal and binomial distribtion
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(loc=50, scale=5, size=1000),
    "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data)
plt.show()