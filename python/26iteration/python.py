#there are two things one is iter and second is next

# mytuble=("mohit","sahil","ankit")
# myit=iter(mytuble)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mytuple=("mohit","ankit","sahil","rohit","rohan")
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


#on the string

# prstr="banana"
# myit=iter(prstr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

#iteratino using loop on the tuple
# mytuple=("ankit","sahil","sohan","sangam")
# for x in mytuple:
#     print(x)

#iteration on the string
# mystr="mohitsankhyan"
# for x in mystr:
#     print(x)

#create the object class literals
# __iter__()
# __next__()

#create an iterator

# class mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x

# myclass=mynumber()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


#create a new iterator

# class mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x

# myclass=mynumber()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



# class mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x

# myclass=mynumber()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x

# myclass=mynumber()
# myiter=iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#stop iterator
# class mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
# myclass=mynumber()
# myiter=iter(myclass)

# for x in myiter:
#     print(x)

#stop iterator

class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=mynumber()
myiter=iter(myclass)
for x in myiter:
    print(x)