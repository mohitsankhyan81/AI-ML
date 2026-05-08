#chi sqare distribution is basic to verify the hypothisis

# it is use for the possible solutions

#it have perimiter like
#df Degree of the freedome
#size is that size that the array return

# ek chi square distribution create karo jo ki degree of freedom 2 with size 2*3 ho
# from numpy import random
# x=random.chisquare(df=2,size=(2,3)) # ye chi square jo hai wo possible pridiction bata hai
# print(X)

# make the visul repersentation of the chi square of the distribution where i give the freedome of only 1
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.chisquare(df=1,size=(2,3)))
plt.show()