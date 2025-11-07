#del keyword which is used to delete the attribute of the object or delete the object itself
"""class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
c1 = Car("white","mercedes")
print(c1.color,c1.model)
del c1.color
print(c1.model)
#print(c1.color) # it says "Car" object has no attribute 'color' as it is del
del c1
print(c1.model)""" # this gives name "c1" is not defined 


#private attribute and privatmethod
"""class Account:
    def __init__(self, acc_no, acc_pwd):
        self.acc_no = acc_no
        self.__acc_pwd = acc_pwd # the is the private attribute which cannot ne used outside the class but can be used inside the class
    def reset_pwd(self,new_pwd):
        self.__acc_pwd = new_pwd # this private variable can be used inside the class
    def display_pwd(self):
        print("The pwd is", self.__acc_pwd)


acc1 = Account(12345,"abcde")
print(acc1.acc_no) # this can be done as this is public
# print(acc1.__acc_pwd) # this gives an error as it is private AttributeError: 'Account' object has no attribute '__acc_pwd'
print(acc1.reset_pwd("hello"))
print(acc1.display_pwd())""" # this gives the password

#imp 
#Private attributes are only inaccessible directly outside the class.
# Methods inside the class can freely read or modify them.
# That’s why your display_pwd() can show the password.

# private method and mosltly why private method is used it it is not allowed outside the class the reason is that it can be acces by other inside the class
"""class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def __hello(self):
        print("Hello",self.name)
    def welcome(self):
        self.__hello()
s1 = Student("Shilno",5)
s1.welcome()"""


#class method 
# it is bound inside the class and receives the class as implicit first argument
#as jun kam @static emthod cant do to change the attribute of the class we can do it by class method
"""class Person:
    name = "Anonymous"
    @staticmethod
    def change_name(name): # the statci method doesnot change the class attribute name inot its arguments
        name = name 
        print(name)

p1 = Person()
print(p1.name)
p1.change_name("Aapu")
print(p1.name) """

"""class Person:
    name = "Anonymous"
    def __init__(self,name):
        self.name = name
    def change_name(self,name): # this change the name of the object only not the name of the class
        self.name = name 
        print(self.name)
        print(name)

p1 = Person("Aapu")
print(p1.name)
p1.change_name("Aaku")
print(p1.name)""" 


#one method is wothout clallin the class method to change the attribut of the class as Class.attribute to changea as Person.name = name
"""class Person:
    name = "Anonymous"
    def __init__(self,name):
        self.name = name
    def class_change_name(self,name):
        Person.name = name
        print(name)
        print(Person.name)
        print(self.name)
    def obj_name(self,name):
        self.name = name
        print(name)
        print(self.name)
        print(Person.name)
p1 = Person("Aapu")
p1.change_name("Aakanchhhya")
p1.obj_name("Apekshya")"""


#next method is self.__init__.attribute to change
"""class Person:
    name = "Anonymous"
    def __init__(self, name , address):
        self.name = name
        self.address = address
    def class_change_name(self,name):
        self.__class__.name = name
        print(name)
        print(Person.name)
        print(self.name)
p1 = Person("AAkanchhya","hadigaun")
p1.class_change_name("Aaku")"""

#class method 
"""class Person:
    name = "Anonymous"
    def __init__(self,name): #this is the obj attribute name
        self.name = name
    @classmethod
    def change_class_attribute_name(cls,name):
        cls.name = name
    def change_obj_attribute_name(self,name):
        self.name = name

p1 = Person("Ram")
print(p1.name)
print(Person.name)
p1.change_class_attribute_name("Aaku")
print(Person.name)
print(p1.name)
p1.change_obj_attribute_name("Sita")
print(Person.name)
print(p1.name)"""


#property decorator 
#we use @property decorator on any method in the class use the method as a property 

# for eg
"""class Student:
    def __init__(self,math,phy,chem):
        self.math = math
        self.phy = phy
        self.chem = chem
        self.percentage = str((self.math + self.phy + self.chem) / 3) + "%"
s1 = Student(98,88,91)
print(s1.math)
print(s1.percentage)
#if we change the value of math as we did a mistake it is not 98 it is 86 then now 
s1.math = 86
print(s1.math) # it change the math marks from 98 to 86 but
print(s1.percentage) # it doesnot change the percentage so we need to solve this
"""
# we have a case to solve this as making a funciton 
"""class Studnet:
    def __init__(self, math, phy, chem):
        self.math = math 
        self.phy = phy
        self.chem = chem 
    def clacPercentage(self):
        self.percentage = str((self.math + self.phy +self.chem) / 3) + "%" # this works it chnage the percentage after the math marks is change 
s1 = Studnet(98,91,92)
s1.clacPercentage()
print(s1.math)
print(s1.percentage)

s1.math = 86
print(s1.math)
s1.clacPercentage()
print(s1.percentage)"""

#property decorator method
class Student:
    def __init__(self, math , phy , chem):
        self.math = math
        self.chem = chem
        self.phy = phy
    @property
    def percentage(self):
        return str((self.math + self.chem + self.phy) / 3) + "%"
        
    
s1 = Student( 98,91,92)
print(s1.math)
print(s1.percentage)
s1.math = 86
#s1.percentage() # this gave an error as you used @property above the method, Python converts this method into a read-only attribute — not a normal function anymore.
print(s1.percentage)