#Binomial Distrbution

#Binomial distribution is the discrete distribution
#ye binory sceniros ko describe karta hai like 
#agar ham coin ko toss karte hai to us me ya to head aaye ga ya to tail

#insme 3 perimeter hote hai 
# n-> number of trails
# p-> kis ke aane ke kitne chance hai
# size-> shape ka return array size

#iske liye binomia function use hota hai


#10 tails for the coin generate the 10 data points
# from numpy import random
# x=random.Binomial(n=10,p=0.5,size=10)
# print(x)

#visulaize the binomial disribution
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.binomial(n=10,p=0.5,size=1000))
# plt.show()

#diffrence between normal and binomil
#norml distribution is contigous
#where binomial distribution is discret 
# but he normal and binomial distribution is quite similar
#normal distribution with romal log and scale

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns


# data={
#     "normal":random.normal(loc=50,scale=5,size=1000),
#     "binomial":random.binomial(n=100,p=0.5,size=1000)
# } #compare both of the distributions

# sns.displot(data,kind="kde")
# plt.show()