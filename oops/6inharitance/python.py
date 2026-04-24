# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname ,self.lastname)

# class student(person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
    
#     def printdata(self):
#         print(f"My name is {self.firstname}")
# x=student("Mohit","Sankhyan")
# x.printdata()






# make the class name for the student and the second class for the course that the student enrole ini the that student class
# class student:
#     def __init__(self,name,email,password):
#         self.name=name
#         self.email=email
#         self.password=password

# class course(student):
#     def __init__(self,name,email,password,courses):
#         super().__init__(name,email,password)
#         self.courses=courses
#     def showdata(self):
#         print(f"Name is {self.name} Email is {self.email} Password is {self.password} Courses is {self.courses}")

# c1=course("Mohit","mohit@gmail.com","dflkjrt","c++")
# c1.showdata()
