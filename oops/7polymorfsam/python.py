#one pre builded function that is len() is called polymofisam
#we use the len funtion in string, in tuple , in list,int dicionry

# class polymorphism
#polymorfisam often the methods that is created by the same name multiple classes but the c lass has the same name

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("Show")
# class boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("Boalt")
# class plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("Plane")
# car1=car("rohit","rohan")
# boat1=boat("data","name")
# plane1=plane("hello","data")

# for x in (car1,boat1,plane1):
#     x.move()





#make the pololymorfisam that has similar fuction now 
#now the problem is that how you handle the same type of the function

# class car:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def save(self):
#         print("hello")
# class data:
#     def save(self):
#         print("Dear sir")

# class tempo:
#     def save(self):
#         print("temp")

# car1=car("mohit",45)
# data1=data()
# tempo1=tempo()

# for x in (car1,data1,tempo1):
#     x.save()

# do the polymorfisam in the inhartance of the classes

class car:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def move(self):
        print("cars show")

class show(car):
    pass

class wify(car):
    def move(self):
        print("on wify")

car1=car("mohit",45)
wify1=wify("ankit",45)

for x in (car1,wify1):
    print(x.name)
    print(x.age)
    x.move()