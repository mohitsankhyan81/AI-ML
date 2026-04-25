#encapsulation is about protecting the data inside the class
#control how the data will we access outside the classs 
#it privent exidental changes hide the internal details


# __ is use for the private values

# class data:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

# p1=data("mohit",34)
# print(p1.name)
# print(p1.age) #this line will we prevent the error 


# class data:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
    
#     def get_name(self):
#         return self.__name  #jab ham access kare ge to bhi hame __ likhna pade ga
#     def get_age(self):
#         return self.__age #jab ham access kare ge to hame __ likhna pade ga

# p1=data("Mohit",45)
# print(p1.get_name())
# print(p1.get_age())


# in the encapsulateion we get the data we set the data 
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

#     def get_name(self):
#         return self.name
#     def set_age(self,age):
#         if(age>0):
#             self.__age=age
#         else:
#             print("Age must be possitve")
#     def get_age(self):
#         return self.__age
    
# p1=person("mohit",43)
# print(p1.get_age())

# p1.set_age(33)
# print(p1.get_age())

# encapsulte is use to protect data 
# give the flaxibulity to the code
# give validation to the code and set the controlls

#for the protected property 
#we use the _

# class user:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age

# p1=user("mohit","klsdf")
# print(p1.name)
# print(p1.age) #this will show the error because age is protected


class user:
    def __init__(self,name,age):
        self.name=name
        self._age=age

    def get_age(self):
        return self._age
    
    def set_age(self,age):
        if(age>0):
            self._age=age
        else:
            print("age is not geted")

p1=user("mohit",34)
print(p1.name)
print(p1.get_age())
p1.set_age(56 )
print(p1.get_age())
