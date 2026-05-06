#Uniform distribution 

#Uniform distribution wo distribution hoti hai jis me har ek event to occor karna ka equal chance milta hai 
#genration of the random values

#low  lower bond 0.0
#high upper bond 1.0
#size retur size of the array


#create 2*3 distribution
# from numpy import random
# x= random.uniform(size=(2,3)) #what is t
# print(x)

#visulize the uniform using the graph
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=1000),kind="kde")
plt.show()