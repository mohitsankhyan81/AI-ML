#self perimiter refer to the current instance of the class

# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def greet(self):
#         print(f"Hello, My name is {self.name}")

# p1=myclass("Mohit Sankhyan",45)
# p1.greet()

#create the instance of the object

# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def greet(self):
#         print(f"Hello, My name is {self.name}")

# p1=myclass("mohit sankhyan",45)
# p1.greet()

#why we use self in python

#without self python would not know about the object properties without the self
# class myclass:
#     def __init__(self,name):
#         self.name=name
    
#     def greet(self):
#         print(f"Hello, sir My name is {self.name}")

# p1=myclass("Mohit")
# p2=myclass("Sahil")

# p1.greet()
# p2.greet()

#self ki jagha ham kuch or name bhi likh sakte hai
# class myclass:
#     def __init__(myobj,name):
#         myobj.name=name
#     def greet(abc):
#         print(f"My name is {abc.name}")

# p1=myclass("Mohit")
# p1.greet() #this is working properly means ham slef na leke koi or bhi use kar sakta hu

#access multiple value using self
# class car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def display_info(self):
#         print(f"{self.brand} {self.model} {self.year}")

# car1=car("toyota","sizuki",450)
# car1.display_info()


class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return f"Hello {self.name}"
    def welcome(self):
        message=self.greet()
        print(message+"! welcome to our website")

p1=person("Mohit")
p1.welcome()