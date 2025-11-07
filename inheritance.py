#when one classie child or derived derives the property or method of another class ie paren / base class
"""class Car:
    color = "black"
    @staticmethod
    def start(): # we make the static method as it is not need to take self as a parameter and we need to create object to call it we can use class name
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

print(Car.color)
car1 = Car()
print(car1.color)

Car.start() #static method is call with class name
Car.stop()

#now inheritance  ans this is the single inheritance as it have single parent and single child class
class ToyataCar(Car):
    def __init__(self,name):
        self.name = name
Tcar1 = ToyataCar("Fortuner")
Tcar2 = ToyataCar("prius")
Tcar1.start()
print(Tcar1.color)
Tcar2.stop()
print(Tcar2.color)"""


#multi-level inheritance as we have one parent class which is inherit by one derived class and again this derived class is inherit by another derived class
#as p -> d -> d
"""class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")

class Toyata(Car):
    def __init__(self, brand):
        self.brand = brand
class Fortunor(Toyata):
    def __init__(self, type):
        self.type = type
car1 = Fortunor("diesel")
car1.start()
car1.stop()
print(car1.brand)""" # this gave an error as AttributeError: 'Fortunor' object has no attribute 'brand'
#due to 
# Python runs only the Fortunor constructor (__init__ of Fortunor).

# It does not automatically call the parent (Toyata) constructor.

# That means self.brand from Toyata is never created, because Toyata.__init__() never ran.



#to solve that we have super() 
#but in this the fortuner derived class again create its oun attribute in the constructor ans doesnot link to the parent or reuse it 
"""class Car:
    @staticmethod
    def start():
        print("Car is started...")
    @staticmethod
    def stop():
        print("Car is stopped...")
class Toyata(Car):
    def __init__(self,brand):
        self.brand = brand
class Fortunor(Toyata):
    def __init__(self,brand,type): # in this it happens to create brand attributw again that the parent has it doesnot link it or reuse the parent constructor
        self.brand = brand
        self.type = type
c1 = Fortunor("Toyata","disel")
c1.start()
c1.stop()
print(c1.brand)
print(c1.type)"""

#ow Fortunor inherits and reuses its parent’s initialization properly.using super()
"""class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")
class Toyata(Car):
    def __init__(self,brand):
        self.brand = brand
class Fortunor(Toyata):
    def __init__(self,brand,type):
        super().__init__(brand) #This line creates self.brand.
        self.type = type
c1 = Fortunor("Toyata","Diseal")
c1.start()
c1.stop()
print(c1.brand)
print(c1.type)"""


#3 multiple inheritance in this inheritance one derived class can inherit form tow or more(multiple)parent class
"""class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)"""


#super() method case
"""class House:
    houe_no = 6
    def __init__(self,ward_no,house_name):
        self.ward_no = ward_no
        self.house_name = house_name
class Address:
    def __init__(self,city):
        self.city = city
class Flat(House,Address):
    def __init__(self,cost,house_name,ward_no,city):
        super().__init__(ward_no,house_name,city)
        self.cost = cost
flatA = Flat(1000000,"Triveni",5,"Kathmandu")
print(flatA.houe_no)
print(flatA.cost)
print(flatA.house_name)
print(flatA.ward_no)
print(flatA.city)"""
# When you write super().__init__(ward_no, house_name, city),
# Python only calls the first parent’s constructor (because of the Method Resolution Order — MRO).
# MRO for Flat
# Flat → House → Address → object
# So super() calls House.__init__(), which expects 2 arguments,
# but you gave 3 (ward_no, house_name, city) → 💥 TypeError.



#2 solution
#1 is call both paren construcotr manually
"""class House:
    hous_no = 6
    def __init__(self,house_name,ward_no):
        self.house_name = house_name
        self.ward_no = ward_no

class Address:
    def __init__(self,city):
        self.city = city
class Flat(House,Address):
    def __init__(self,house_name,ward_no,city,cost):
        House.__init__(self,house_name,ward_no)
        Address.__init__(self,city)
        self.cost = cost

flatA = Flat("triveni",5,"Kathmandu",100000)
print(flatA.hous_no)
print(flatA.house_name)
print(flatA.ward_no)
print(flatA.city)
print(flatA.cost)"""


"""def even(*num1):
    for num in num1:
        if num% 2 == 0:
            print(num ,'even')
        else:
            print(num ,'odd')
even(1,2,3,4,5)"""


"""class House:
    def __init__(self ,house_name , ward_no,**kwargs):
        super().__init__(**kwargs)
        self.house_name = house_name
        self.ward_no = ward_no
class Address:
    def __init__(self,city,**kwargs):
        super().__init__(**kwargs)
        self.city = city

class Flat(House,Address):
    def __init__(self,house_name,ward_no,city,cost):
        super().__init__(house_name = house_name , ward_no = ward_no , city = city)
        self.cost = cost

flatA = Flat("Triveni",5,"Kathmandu",1000000)
print(flatA.house_name)
print(flatA.ward_no)
print(flatA.city)
print(flatA.cost)"""


#super method is used to access methods of the parentclass and as wll the parameters
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start() # we can also use super with the parent method to inheritant the parent method
        super().stop()
c1 = Toyota("Prius","electric")
print(c1.type)