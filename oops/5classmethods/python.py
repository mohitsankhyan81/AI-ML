#methods are function  that belong to the class
#that define the behaviur created for the class

# class person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         print(f"Hello, {self.name}")

# p1=person("Mohit")
# p1.greet()

#method with property
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def mul(self,a,b):
#         return a*b

# c1=Calculator()
# print(c1.add(3,4))
# print(c1.mul(3,4))

#method access property
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_info(self):
#         return f"Name is {self.name} Age is {self.age}"
# p1=person("Mohit",45)
# print(p1.get_info())

#Method Modify property
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def celibrate_birday(self):
#         self.age+=1
#         print(f"Happy birthday {self.name} You are now {self.age}")
# p1=person("Linux",40)
# p1.celibrate_birday()
# p1.celibrate_birday()

#__str__ method
# __str__ method is the special method that control the return when the object is print

#without str
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("Mohit",45)
# print(p1) // print is not possible using this

# with __str__
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name} ({self.age})"

# p1=person("Mohit",45)
# print(p1)

#delete method in python opps
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print(f"Name is {self.name} , Age is {self.age}")

# p1=person("Mohit",45)
# p1.greet()
# del person.greet
# p1.greet() # p1 is deleted so this time it show the error of the module not found
