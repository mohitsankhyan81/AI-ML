    
# s1=student("Mohit",45,"Chitkara Univeristy")
# print(s1.name)
# del s1.age
# #now if we try to print the age it cause an error
# # print(s1.age)
# print(s1.university)

#share things out of the class
class student:
    token="User Token"
    def __init__(self,name):
        self.name=name
    
s1=student("mohit")
print(s1.name)
print(s1.token)
s2=student("ankit")
print(s2.name)
