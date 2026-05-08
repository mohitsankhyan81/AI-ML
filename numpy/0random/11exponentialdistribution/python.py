#Exponential Distribution

#exponential distribution kya karta ki jo 
#event comlete ho jata hai ya to fail ho jata hai bas usi ka time bata hai 
#fail ya fir seccess ka time

#iss me two things hoti hai one is the scale and second one is the size

#jo scale hota hai wo invest ka rate bata hai default 1.0
#or ye size bhi return karta hai

#drow a simple exponental distribution witht hte sacale of 2 and the size is 2*3
# from numpy import random
# x=random.exponential(scale=2,size=(2,3))
# print(x)

#visulalize the exponental distribution 
from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns

sns.displot(random.exponential(size=1000),kind="kde")
plt.show()