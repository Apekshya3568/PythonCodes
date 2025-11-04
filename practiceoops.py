#this is the practice question for oops
#create student class that tkaes name amd marks of 3 student as arguments in constructor. then create a methid to print the average
"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        average = (s1.marks + s2.marks +s3.marks) / 3
        print(f"Average marks of student {s1.name} , {s2.name} and {s3.name} is {average}")
s1 = Student("Karan", 88)
s2 = Student("Teja", 90)
s3 = Student("Siddhart", 97)
s1.average()
s2.average()
s3.average()"""


#next method when funciton is taken not the class inside the method not approperote this code but for practice
"""class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
def average(students):
    total = 0
    for student in students:
        total += student.marks
    avg = total / len(students)
    print(f"The average marks of  {[student.name for student in students]} is {avg}")
s1 = Student("Karan", 88)
s2 = Student("Teja", 90)
s3 = Student("Siddhart", 97)
average([s1,s2,s3])"""



#The actual question is 
#create student class that take name and marks of 3 subjects as arguments in constructor.Then create a method to prin the average
"""class Student:
    def __init__(self, name, eng_marks, math_marks, phy_marks):
        self.name = name
        self.eng_marks = eng_marks
        self.math_marks = math_marks
        self.phy_marks = phy_marks
    def average(self):
        avg = (self.eng_marks + self.math_marks + self.phy_marks) / 3
        print(f"Student {self.name} has got average is {avg}")
s1 = Student("Kripa" , 85,90,78)
s1.average()"""


#next method 
"""class Student:
    def __init__(self,name,marks):# here we take marks as a list
        self.name = name
        self.marks = marks
    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
            avg = sum / len(self.marks)
        print(f"Hello {self.name} your average score is {avg}")
s1 = Student("Karan", [78,88,98])
s1.get_average()"""

# to change the attribute value directly as 
"""s1.name = "Gopal"
s1.get_average()"""

"""s2 = Student("Jack" , [88,76,78])
s2.get_average()
s3 = Student("Bob", [67,78,89])
s3.get_average()
s3.name = "Payal"
s3.get_average()"""



#create Account class with 2 attributes - balance and account no.
#create methods for debit , credit and printing the balance
"""class Account:
    def __init__(self, balance , account_no):
        self.balance = balance
        self.account_no = account_no
    def debit(self):
        debit_amount = 1000
        self.balance -= debit_amount
        print(f"Your balance in this account no {self.account_no} is {self.balance}")
    def credit(self):
        credit_amount = 200
        self.balance += credit_amount
        print(f"Your balance in this account no {self.account_no} is {self.balance}")
    def print_balance(self):
        print(f"The total balance after credit and debit in your {self.account_no} is {self.balance}")

acc1 = Account(2000, 11234567)
acc1.debit()
acc1.credit()
acc1.print_balance()"""

#next method
class Account:
    def __init__(self ,acc_no , bal):
        self.account_no = acc_no
        self.balance = bal
    def debit(self ,amount):
        self.balance -= amount
        print(f"Rs {amount} was debited")
        print("Total balance present is" , self.get_balance())
    def credit(self,amount):
        self.balance += amount
        print(f"Rs {amount} was credited")
        print("Total balance present is " , self.get_balance())
    def get_balance(self):

        print(f"Total balance present is {self.balance}")
        return self.balance
acc1 = Account(12345,10000)
acc1.debit(2000)
acc1.credit(40000)
acc1.get_balance()



