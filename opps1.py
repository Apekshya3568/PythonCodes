#object oriented programming
"""class Student:
    name = "Apekshya"
s1 = Student()
print(s1.name)
s2 = Student()
print(s2.name)"""


"""class Car:
    color = "blue"
    model = "mercedes"
car1 = Car()
print(car1.color)
print(car1.model)"""

#constructor 
#when an object is created then the constructor is automatically call
"""class Student:
    def __init__(self): # if we have not written __init__ funciton then python automatically call an init funciton as wehen the construcotr is call then init funcion is also call
        print("Hello")
s1 = Student()""" # here the parenthesist call the constructor and it automatically the __init__ function 


"""class Car:
    def __init__(self):
        print(self)
car1 = Car()
print(car1)""" # this and print(self) gives the same output and self mean this object only 


"""class Car:
    def __init__(self):
        print(self)
c1 = Car()
print(c1)
c2 = Car()
print(c2)"""
# Output
# <__main__.Car object at 0x000001F3D02A74D0> call the Car() constructor the goes to __init__ function the print(self)
# <__main__.Car object at 0x000001F3D02A74D0>then now in this print(c1)
# <__main__.Car object at 0x000001F3D0568CD0>this again call the constructor Car() as it creates object c2 and call thedef __init__ fucntion the print(self)
# <__main__.Car object at 0x000001F3D0568CD0>this print(c2)


"""class Student:
    def __init__(self,fullname):
        self.name = fullname
s1 = Student("Aapu")
print(s1.name) # here self.name is the attribute of the object of student which is s1 
#when we did print(s1.fullname) the it says 'Studnet object has no attribute 'fullname'""
s2 = Student(23) # this also works
print(s2.name)"""
# s3 = Student() TypeError: Student.__init__() missing 1 required positional argument: 'fullname'
"""class Student:
    def __init__(self,fullname,subject_marks):
        self.name = fullname
        self.marks = subject_marks
# s1 = Student()TypeError: Student.__init__() missing 2 required positional arguments: 'fullname' and 'subject_marks'
s1 = Student("Aaku",90)
print(s1.name, s1.marks)"""


"""class Student:
    def __init__(self, fullname):
        self.name = fullname
s1 = Student("Aapu")
# print(s1.self) # Student object has no attribute 'self' 
#actually self is also an object so its attribute is name as self.name 
print(s1.name)"""

"""class Car:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        print(self.name)
        print(self.marks)
c1 = Car("Karan",77)
print(c1.name)
print(c1.marks)"""


#This gave an error
"""class Student:
    def __init__(self): # this is the default constructor 
        print("Hello")
    # def __init__(self,name): # this is the parameterized constructor
    #     self.name = name
s1 = Student()
# s2 = Student("Karan")
# print(s2.name)"""



"""class Student:
    def __init__(self, fullname, location):
        self.name = fullname
        self.location = location
    def full_info(self):
        print(f"Hello {self.name} and lives in {self.location}")

s1 = Student("Karan","Patan")
s1.full_info()"""


#class arrtribute and object arrtribute
# class arrtribute is comman for all the objects 
#object arrtribute is different for each object
"""class Student:
    #class attribute
    college_name = "ABC" # same for all the objects
    def __init__(self, name, marks):
        #object attribute
        self.name = name # as this is store with object so it is different for each object  
        self.marks = marks
s1 = Student("Aaku",98)
print(s1.name, s1.marks)
print(s1.college_name)"""

# if we have the same attribute name for class attribute and object attribute then it will come as output as object attribite as obj.attr > class.attri
#object attribute precendence is greater then class attribute 
"""class Student:
    college_name = "ABC"

    def __init__(self, name):
        self.name = name
        
        return
s1 = Student("krishna")
print(s1.college_name)
print(s1.name)
# we can do this nut in thsi case it doesnot make a lot of sense"""


#methods 
#atrribute(properties) and methods (behavourie) and this is the collection of a class
"""class Student:
    def __init__(self, name):
        self.name = name
    def hello(self): # THIS IS THE METHOD and self always when you create a method it should  always the first parameter in it 
        print("hello", s1.name)
        print("Hello", self.name)
s1 = Student("Karan")
s1.hello()"""


"""class Student:
    def __init__(self , name, marks):
        self.name = name
        self.marks = marks
    
    # def welcome() this will give an error as we need to have self as first parameter if we use or dont use self in the below
    def welcome(self):
        print("Welcome Student ",self.name)
    def get_marks(self):
        return self.marks
    def get_address(self, address):
        print(f"{self.name} lives in {address}") # instead if we did self.address then its error is 'Student' object has no attribute 'address'

s1 = Student("Shiva", 88)
s1.welcome()
print(s1.get_marks())
s1.get_address("Patan")"""


#we can also change the attribute value
"""class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Aapu")
print(s1.name)
s1.name = "Apekshya"
print(s1.name)"""


#Static method they are the method which doesnot need a self parameter  and this method is at class level and for a funciton to be a static method we need to have a decorator as @static method
#the problem
"""class Student:
    def __init__(self,name):
        self.name = name
    def hello(): # this needs to take self as its parameter 
        print("Hello")
s1 = Student("katan")
print(s1.name)
s1.hello()"""# this gives an error as it foest have self parameter

#the solution is
"""class Student:
    def __init__ (self, name):
        self.name = name
    def hello_student(self):
        print(f"Hello {self.name}") # this works perfectly
    @staticmethod
    def hello(): # after writting the above decorator as @staticmethod we dont need to have self parameter
        print("Hello")
      #  print(f"Hello {name}") #name is not defined error
       # print(f"Hello {self.name}") # this also have self is not defined
s1 = Student("Bob")
print(s1.name)
s1.hello_student()
s1.hello() """# this gets printed without any error


"""class addition:
    @staticmethod
    def add(a,b):
        sum = a + b 
        print(sum)
addition.add(2,3)
a1 = addition()
a1.add(4,5)"""


#instance method / object method
"""class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def change_name(self , new_name): # this way as well you can change the name
        self.name = new_name
    def display_info(self):
        print(f"Welcome {self.name}. Your score is {self.marks}")
s1 = Student("Krishna" ,88)
s1.display_info()
s1.name = "Bhola" # this way we can also change it
s1.display_info()
s1.change_name("Gopal")
s1.display_info()"""

#class method
class Shooping:
    shooping_center = "City Center"
    def __init__(self,number, color):
        self.num = number
        self.color = color
    def display_shooping(self):
        print(f"You want to buy {self.num} of clothes and main {self.color} clothes.")
    @classmethod
    def change_center(cls,new_center):
        cls.shooping_center = new_center
s1 = Shooping(3,"white")
print(s1.num)
print(s1.color)
print(Shooping.shooping_center)
Shooping.change_center("Bhatbhateni")
s1.display_shooping()
print(Shooping.shooping_center)




#abstraction
#hiding the implementation details and showing only the essential details 
"""class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started...")
car1 = Car()
car1.start()""" #this print car started 
#so this code hides how the car is started it just show the start method 

    




