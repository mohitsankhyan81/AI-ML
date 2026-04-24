#propertry are the variables that belog to the class
# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=myclass("mohit",34)
# print(p1.name)
# print(p1.age)


#access property the dot notation
# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# car1=car("maruti","sizuki")
# print(car1.brand)
# print(car1.model)

#modify property in the class
# class data:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=data("Mohit",45)
# print(p1.age)
# p1.age=34
# print(p1.age)

#delete property in the class
# class student:
#     def __init__(self,name,age,university):
#         self.name=name
#         self.age=age
#         self.university=university
    
# s1=student("Mohit",45,"Chitkara Univeristy")
# print(s1.name)
# del s1.age
# #now if we try to print the age it cause an error
# # print(s1.age)
# print(s1.university)

#share things out of the class
# class student:
#     token="User Token"
#     def __init__(self,name):
#         self.name=name
    
# s1=student("mohit")
# print(s1.name)
# print(s1.token)
# s2=student("ankit")
# print(s2.name)
# print(s2.token)


#modify the class property it effect all the object
# class person:
#     lastname=""
#     def __init__(self,name):
#         self.name=name

# p1=person("mohit")
# print(p1.name)
# print(p1.lastname)
# p1.lastname="Sankhyan"
# print(p1.lastname)

#add new property in the existing object
class person:
    def __init__(self,name,age,university):
        self.name=name
        self.age=age
        self.university=university

p1=person("mohit",34,"Chitkara")
p1.batch="Science"

print(f"""Student name is {p1.name} age is {p1.age} university is {p1.university} batch is {p1.batch}""")