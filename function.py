# def is the function definition
"""def cal_sum(a,b): # here a and b are the parameters
    sum = a + b
    print(sum)
cal_sum(2,3)""" # this is the funcition call and 2 , 3 are the arguments

"""def cal_mul(a,b):
    mul = a*b
    return mul

cal_mul(3,5)
print(cal_mul(3,5))"""


"""def sub_num(a,b):
    return a -b
substraction = sub_num(101,100)
print(substraction)"""

# print hello Apekshya when a fucniton is call
def print_hello(): # this funciton has no parameter 
    print("Hello Apekshya") # this funciton has no return 
print_hello()
result = print_hello()
print(result) # the output of this function is none as it doesnot return anything 


# average number
"""def avg_num(a,b):
    average = (a+ b ) / 2
    print(average)
avg_num(3,3)
print(avg_num(4,9))"""

"""def cal_marks(marks1,marks2,marks3):
    sum = marks1+marks2+marks3
    average = sum / 3
    print(average)
    return average

cal_marks(92,89,97)"""

# default argument
"""def calc_prod(a = 2, b =2): # default id we didnot pass any argument when we call the function then this works 
    print(a * b)
    return a * b
calc_prod(2,3)"""

#wap to print the length of a list (list is the parameter)
my_list = [1,2,"hello",2,3]
def cal_list(my_list):

    print(len(my_list))
    return len(my_list)
cal_list([1,2,"hello",2,3])



#wap to print the elements of a list in the single line(list is a parameter)
"""def single_line(my_list):
    my_list = [1,2,3,"hello",4,5]
    for i in my_list:
        print(i,end=" ")
        
single_line(my_list)"""

#wap to find the factorial of n (n is the parameter)
"""n = int(input("Enter the number to find the facotrial: "))
def factorial(n):
    
    i = 1
    fact = 1
    while i <= n:
        fact = fact * i
        print(fact)
        i += 1

factorial(n)"""


#WAP to convert usb into npr
"""usb = int(input("Enter the usb to convert to nrp: "))
def usb_npr(usb):
    npr = usb * 139.89
    print(npr)

usb_npr(usb)"""


"""euro = int(input("Enter the euro to convert to npr: "))
def euro_npr(euro):
    npr = euro * 163.84
    print(f"{euro} Euro = {npr} Npr")
euro_npr(euro)"""


"""kuwaiti_Dinar = int(input("Enter value to convert to npr"))
def ku_npr(kuwaiti_Dinar):
    npr = kuwaiti_Dinar * 459.82
    print(f"{kuwaiti_Dinar} ku = {npr} npr")

ku_npr(kuwaiti_Dinar)"""

"""pound = int(input("Enter the value to conevrt into npr: "))
def pound_npr(pound):
    npr = pound * 189.60
    print(f"{pound} Pound = {npr} npr")

pound_npr(pound)"""


# wap to take a number and funciton to fins wheather it is even or odd
n = int(input("Enter the number: "))
def even_odd(n):
    if n % 2 == 0:
        print("EVEN")
    else:
        print("Odd")
even_odd(n)