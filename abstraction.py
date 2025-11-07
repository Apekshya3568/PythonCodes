#abstraction is hiding the implementation details and showing the essentail 
# abstract class blueprint for other subclass you cant make the object of abstract class
#abstract class is defined using the ABC module (ABC stands for Abstract Base Class)
#abstract method is a mrthod declared in abstract class but not implemeted it odesnot have a body so we use pass
"""from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
c1 = Circle(3)
print(c1.radius)
print(c1.area())"""

"""from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self, length , breadth):
        pass
    @abstractmethod
    def perimeter(self, length , breadth):
        pass
class Rectangle(Shape):
    def area(self,length,breadth):
        return length * breadth
    def perimeter(self, length , breadth):
        return 2 * (length * breadth)
    
rec1 = Rectangle() # as init there is no 
print("Area :", rec1.area(3,5))
print("Perimeter:",rec1.perimeter(5,8))"""

"""from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 *(self.length + self.breadth)
    
rec1 =Rectangle(5,6)
print("Area:", rec1.area())
print("Perimeter:", rec1.perimeter())"""


from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self,length,breadth):
        return self.length * self.breadth
    def perimeter(self,length,breadth):
        return 2 *(self.length + self.breadth)
    
rec1 =Rectangle(5,6)
print("Area:", rec1.area(4,5))
print("Perimeter:", rec1.perimeter(7,8))