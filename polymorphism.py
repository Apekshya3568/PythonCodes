#jaba yeuta kura lai nai alag alag tarika le use garna sakine lai polymorphishms
#operater overloading is a type of polymorphism that is asjaba same operator is allowed to have different meaning according to the context
print(1 + 2)
print(type(1))
#python ma already class int bhane cha and if we write any no then that is the object of that class as 1 is the object of class int
#ans in class int + is to add the interger and provide the result
print("Apekshya" + "Lamichhane")
print(type(str))
#here in python we have already class str and + means to concatenate and "Apekshya" and "Lamichhane" are the object of this class str
print([1,2,3,4] + [5,6,7,8])
# this is  in python class list and in this class as well + mens to merge two object here obj1 is [1,2,3,4] and obj2 is [5,6,7,8]

#so the same operator "+" is used differently in different context

#dunder function
# eg : complex no as 3i + 7j here 3i is real and 7j is imaginary
"""class Complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")


    def add(self,num):
        newReal = self.real + num.real
        newImg = self.img + num.img
        # print(f"{newReal}i + {newImg}j")
        #we can also do 
        return Complex(newReal,newImg)
  



c1 = Complex(3,5)      # Expression	What it means	Value
# self.real	c1.real	3
# num.real	c2.real	4
# self.img	c1.img	5
# num.img	c2.img	8
c1.showNumber()

c2 = Complex(4,8)
c2.showNumber()
c1.add(c2)
c3 = c1.add(c2)
c3.showNumber()"""


# When you call:
# c1.add(c2)
# # Python runs:
# Complex.add(c1, c2)
# # Which means:
# self = c1
# other = c2


"""class Complex:
    def __init__(self,real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")

    def add(self ,num2):#here self is obj 1 and num2 is obj2
        newReal = self.real +num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
c1 = Complex(5,8)
c1.showNumber()
c2 = Complex(2,5)
c2.showNumber()

c3 = c1.add(c2) #7i + 13j this gives the result as 5+2 = 7 and 8 + 5 = 13 so it works well but
c3.showNumber()"""

#but when we do c3 = c1 + c2 then it gaves an error so to solve this we need a dunder funciton as
"""class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    def __add__(self,num2): # this is the dunder function so now we can do a + b we sont need to call add function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
c1 = Complex(7,11)
c1.showNumber()
c2 = Complex(3,6)
c2.showNumber()

c3 = c1 + c2
c3.showNumber()"""

#we can do as well for substraction
"""class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    def __sub__(self,num2): # this is the dunder function so now we can do a + b we sont need to call add function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
c1 = Complex(7,11)
c1.showNumber()
c2 = Complex(3,6)
c2.showNumber()

c3 = c1 - c2
c3.showNumber()"""

#multiplication
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    def __mul__(self,num2): # this is the dunder function so now we can do a + b we sont need to call add function
        newReal = self.real * num2.real
        newImg = self.img * num2.img
        return Complex(newReal,newImg)
c1 = Complex(7,11)
c1.showNumber()
c2 = Complex(3,6)
c2.showNumber()

c3 = c1 * c2
c3.showNumber()