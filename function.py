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
"""n = int(input("Enter the number: "))
def even_odd(n):
    if n % 2 == 0:
        print("EVEN")
    else:
        print("Odd")
even_odd(n)"""


#Wap to make a function called submit-form, and take the parameters as fname, sname and
#print(your form has been submmited {name}) and print(thanyou {name})
"""def submit_form(fname, sname):
    name = fname + " " + sname 
    print(f"Your form has been submited {name}")
    print(f"Thankyou {name}")
submit_form("Apekshya","Lamichhane")
"""
#wap to write a funtion who has citizenshp print your form has been submitted and the print thankyou with the fullname
"""def submit_form(fname,sname,has_citizenship):
    full_name = fname +" " +sname
    if has_citizenship:
        print(f"Your form has been submitted {full_name}")
        print(f"Thankyou {full_name}")
submit_form("Apekshya" ,"Lamichhane",True)
"""

"""def submit_form(fname, sname , has_citizenship = False):
    full_name = fname + " " +sname
    if has_citizenship:
        print(f"Your form has been submitted {full_name}")
        print(f"Thankyou {full_name}")
submit_form("Apekshya","Lamichhane")
submit_form("Aaku","Lamichhane",True)
"""

#positional argument
"""def submit_form(fname,sname):
    print(f"You form has been sumbitted {fname} {sname}")
submit_form('Lamichhane','Apekshya')""" #arguments not in posiiton so not expected output

#keyword argument
"""def submited_form(fname,sname):
    print(f"Your form has been submitted {fname} {sname}")
submited_form(sname = "Lamichhane" ,fname= "Aapu")""" # argument not in position but gives expected output
#this is keyword argument



#WAP to find the maxium even num from the given list
# [1,2,3,4,12,12,14,15,19, 5]                      14
         #even numbers        #max of those evens
def even_numbers(my_list, maximum = 0):
    for i in my_list:
        if i % 2 == 0:
           if maximum < i:
               maximum = i
    print(maximum)
my_list = [1,2,3,4,12,12,14,15,19,5]
even_numbers(my_list)

#second methos
"""def max_even():
    numbers = [1,2,3,4,12,12,14,15,19,5]
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    print(max(even_list))
max_even()"""


# list comprehension 
print(max([item for item in my_list if item % 2 == 0])) # this gives 14 as output
print(min(i for i in my_list if i % 2 == 0)) # this also works and it gives 2 as output



