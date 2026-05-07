# jo multinomial distribution hai wo kuch had tak binomial distribution hi hai 

#binomial distribution
#jo ki kise kaam ke hone hi probibulity bata hai
#isme 3 perimiter hote the
# n -> number or trials
# p -> like ki kis chij ke aane ki kitni probibulity ho sakti hai
# size -> size is like the return size of the elements

#defult size bhi one hi hota hai


# bas ham binomial me probibulity ka use karte the iss mme ham probibulity value ka use kare ge

#pvals-> like 1/6 ,1/6 ,1/6 ,1/6,1/6,1/6 
# matlab dice me 6 sides hoti hai 
# or 6 me se koi bhi outcome aa sakti hai
# to wo 6 times 1/6 hi hoga

from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)