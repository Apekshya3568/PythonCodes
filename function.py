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
"""def print_hello(): # this funciton has no parameter 
    print("Hello Apekshya") # this funciton has no return 
print_hello()
result = print_hello()"""
# print(result) # the output of this function is none as it doesnot return anything 


# average number
"""def avg_num(a,b):
    average = (a+ b ) / 2
    print(average)
avg_num(3,3)
print(avg_num(4,9))""" # in this as print is there and inside it there is avg_num(4,9) so this call id function call so it runs the inside funciton code and give result 6.5 but there is print so it agian gives none

"""def cal_marks(marks1,marks2,marks3):
    sum = marks1+marks2+marks3
    average = sum / 3
    print(average)
    return average

cal_marks(92,89,97)
total_marks = cal_marks(83,84,85) # this will definitly gives an result as therweis callinf of the function
print(total_marks) # but this will also give an output as numbers as it doesnit give none as there is return average
print(cal_marks)""" # this will also give an output not none it give numvers as there is the return type

"""def sum(a,b):
    return a+b
sum(4,4) # this will not give any output as inside the function there is no print it even doesnot give none
print(sum(10,10))""" # so to get an output we need to print it 

def sum(a,b):
    print(a*b)
    return a *b
sum(3,10)
sum_no = sum(4,10)
print(sum_no)
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



# my_list = [2,2,3,3,3,3,4,5,6] this is the question and this is the output #[4,5,6]
"""my_list = [2,2,3,3,3,4,5,6]
def new_elements(my_list):
    elements = []
    for i in my_list:
        if my_list.count(i) == 1:
            elements.append(i)
    print(elements)
new_elements(my_list)"""


#next method
"""my_list = [2,2,3,3,3,4,5,6]
def remove_duplicates(my_list):
    print(list(set(my_list)))
remove_duplicates(my_list)"""


#practice question 
"""state = "start"
while True:
    command = input("Enter a command start , stop , help: ").lower()
    if command == state:
        if command == "start":
            print("Car is already in start state")
        elif command == "stop":
            print("Car is already in stop state")
        elif command == "help":
            print("start to start /n stop to stop")
    else:
        if command == "start":
            print('Car started')
        elif command == "stop":
            print("Car stopped")
        elif command == "help":
            print("start to start /n stop to stop")
        else:
            print("Sorry , you entered the wrong command")
    state == command
    is_continue = input("Y for yes and N for no: ").upper()
    if is_continue == "N":
        break
print('Thankyou for playing')"""


#Guessing game
# take the secret_number, guess_count, guess_limit varible..
# secret_number would have one integer value from 0-9
# you give 3 chance to guess the number
# if the guess is correct print you won else try again
# and print sorry you failed after 3 tries
"""secret_number = int(input('Enter the secret no: '))
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_count += 1
    # print(guess_count)
    guess_number = int(input("Enter the no to guess: "))
    if guess_number == secret_number:
        print("You won")
        break
    
    else:
        if guess_count == guess_limit:
            print("You failed")
        else:
            print("Try again")
    
else:
    print("Sorry you failed after 3 tries ")"""


# print the elements of list in descending order 
my_list = [1,2,3,4,5,6,7,8,9]
desc_list = []
maximum = 0
j = 0
while j <= len(my_list):
    for i in my_list:
        if maximum <= i:
            maximum = i
    j += 1




