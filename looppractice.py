"""str = "I am learning python"
copy_str = str[:] # this is for the copy of the string
print(copy_str)"""

#list
"""fruits = ["apple" , "banana","mango","pineapple"]
copy_list = fruits[:]
print(copy_list)
reverse_list = fruits[::-1]
print(reverse_list)
"""
#tuple
"""fruits = ("apple" , "banana","mango","pineapple")
copy_tuple = fruits[:]
print(copy_tuple)
reverse_tuple = fruits[::-1]
print(reverse_tuple)"""

"""student ={
    'name' : "Apekshya",
    'age': 21,
    'location': 'Hadigaun',
    'name' : "Aakanchhhya"
}
print(student)
student['name'] = 'Apekshya' # this will change the name from Aakanchhya to Apekshya
print(student)
student.update({'name':"Aakanchhay"}) # this will update the name from Apekshya to Aakanchhay
print(student)
student.update({'marks' : 90}) # this will add new key value pair that is marks : 90
print(student)
student['grade'] = "Bachelor" # this also will add new key value pair thatis grade : Bachelor
print(student)
"""

"""first_name = "Apekshya"
last_name = "Lamichhane"
print(f"This is {first_name} {last_name} presenting the slides")"""


"""is_cold = False
is_rainy = False
if is_cold and is_rainy:
    print("Wear warm clothes and take umbrella")
elif is_cold or is_rainy:
    print("Wear warm clothes or take an umbrella")
else:
    print("you are good to go")
"""

# if else
"""has_money = False
has_credit = False
if has_money:
    if has_credit:
        print("You have both the choices money or credit")
    else:
        print("You have only money choice")
elif has_credit:
        print("You have only credit choice")
else:
     print("You dont have any choice")"""


# weight converter
"""weight = int(input("Enter your weight:"))
unit = input("Enter the unit: (kg) for kilogram and (p) for pounds ").lower()
if unit == "kg":
    pound = weight/0.45
    print(f"Your{weight} {unit}  weight is converted to {pound} pound")
elif unit == 'p':
    kilogram = weight * 0.45
    print(f"Your {weight} {unit} weight is converted to {kilogram} kilogram")
else:
    print('You have enterd an wrong input')"""



#assign a list to one variable
#if the list has odd length and the middle element is 7
#print this is the list i have been searching
#else print this is not the list i have been searching
#if the list has even length, tell the middle element does not exists
"""
elements = [1,2,3,5,5,6,8]
mid = len(elements) // 2
middle_element = elements[mid]

if len(elements) % 2 != 0:
    if middle_element == 7:
        print("This is the list i have been searching ")
    else:
        print("This is not the list i have been searching")
else:
    print("The middle element doestnot exit")"""



#wap to find the maximum value of the list 
"""list_elements = [2,3,4,5,6,7]
i = 0
maximum = 0
while i < len(list_elements):
    print(list_elements[i])
    if maximum < list_elements[i]:
        maximum = list_elements[i]
    i += 1
print(maximum)"""

"""list_elements = [1,2,3,4,12,13,16]
maximum = 0
for i in list_elements:
    if i % 2 == 0:
        if maximum < i:
            maximum = i
print(maximum)
"""
"""
list_elements = [2,3,4,5,6,7]
print(max(list_elements))"""

#
#WAP to find the maximum even value of the list
              # [1,2,3,12,14,10, 19, 21]             --> 14

# even values, maximum of that even
"""collection = [1,2,3,12,14,10,19,21]
i = 0
maximum = 0
while i < len(collection):
    if collection[i] % 2 == 0:
        if maximum < collection[i]:
            maximum = collection[i]
    i += 1
print(maximum)
"""


# make a new list append the even numbers and then find the maximum
"""marks = [45,48,80,90,98,73,42,35,46,40,58]
new_marks = []
i = 0
while i < len(marks):
    if marks[i] % 2 == 0:
        new_marks.append(marks[i])
    
    
    i += 1
    
print(new_marks)

i = 0
maximum = 0
while i < len(new_marks):
    
    if maximum < new_marks[i]:
        maximum = new_marks[i]
    i += 1
    
print(maximum)"""



#for loop
"""marks = [12,34,45,56,55,66,67,89,87,67,98]
new_marks = []
for i in marks:
    if i % 2 == 0:
        new_marks.append(i)
print(new_marks)

maximum = 0
for i in new_marks:
    if maximum < i:
        maximum = i
print(maximum)
"""


# senior level code
"""marks = [12,23,32,34,45,56,67,78,89,90]
new_marks = []
for i in marks:
    if i % 2 == 0:
        new_marks.append(i)
print(new_marks)
print(max(new_marks))"""


"""marks = [-1,-2,-3,-4,-5]
print(max(marks))"""


"""h_list = [-2,-3,-6,-7,-8]
i = float('-inf') #float('-inf') produces negative infinity as a floating-point value. every real number is greater than negative infinity ordinary integer x, x > float('-inf') is True
for item in h_list:
    if item%2==0:
        if item>i:
            i=item
print("The Greatest Even Item in List is",i)
"""

"""h_list = [-2,-3,-4,-5,-6]
i = None
for item in h_list:
    if item % 2 == 0:
        if i ==  None or  i < item:
            i = item 
print(i)
"""

"""numbers = [-3,-3,-2,-5,-6,-7,-8]
even_num = [i for i in numbers if i % 2 == 0 ]
print(even_num)
maximum = even_num[0]
for i in even_num:
    if maximum < i:
        maximum = i
print(maximum)"""

"""numbers = [-3,3,-5,6,7,-1,9]
odd_num =[i for i in numbers if i % 2 == 1] # list comprehension is only used for for loop it cannot be done for while loop
maximum = odd_num[0]
for i in odd_num:
    if maximum < i:
        maximum = i
print(maximum)
"""

#for loop
"""number = [1,2,3,4,5,6,7,8]
even_num =[]
for i in number:
    if i % 2 == 0:
        even_num.append(i)
print(even_num)"""

#while loop
"""number = [1,2,3,4,5,6,7,8]
even_num = []
i = 0
print(len(number))
while i <len(number):
    if number[i] % 2 == 0:
        even_num.append(number[i])
    i += 1
print(even_num)"""


"""max_num = [1,2,3,4,5,6,7,8,9]
print(max(num for num in max_num if num % 2 == 0))
print(max(max_num))
print(max(num for num in max_num if num % 2 == 1))"""



#CAR game:
#take the input command from user in a command variable
# if the command is start, print car started
# elif the command is stop, print car stopped
# elif the command is help, print start - to start
#                                 stop - to stop
# sorry i dont understand the command, in case of other commands.
# Note: the program should run on all cases, ie start, START, Start, STart are all start

# make the program Continuous
# if the user types the quit command then end the game
# also give thankyou msg after the user finished playing

'''while True:
    command = input("Enter the command: ").lower()

    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command =="help":
        print(""" start - to start
        
              stop - to stop""" )
    elif command == "quit":
        print("thankYou for playing")
        break
    else:
        print("Sorry i dont understand the command")'''


# for loop
"""no_loops = int(input("Enter the no of times you want to run the loop"))

for _ in range(no_loops):
   command = input("Enter the command: ").lower()
   if command == "start":
       print("Car started")
   elif command == 'stop':
       print("Car stopped")
   elif command == "help":
       print('''start - to start
        stop - to stop''')
   elif command == 'quit':
       print("Thankyou for playing this game")
       break
   else:
       print("You have enterd the wrong command")"""


#advance version game 
'''started = True
while True:
    command = input ("Enter the command: ").lower()
    if command == 'start':
        if started:
            print('Car is already started')
        else:
            print("Car starts")
            started = True
    elif command == "stop":
        if not started:
            print("Car is in stopped state")
        else:
            print("Car is stop")
            started = False
    elif command == "help":
        print(""" start - to start the car
    stop - to stop the car""")
    elif command == 'quit':
        print("Thankyou for playing this game")
        break
    else:
        print("You have entered the wrong command")
'''

## WAP using for loop to remove duplicates    [2,2,3,3,4,5,6] 
#making a new list
"""collection = [2,2,3,3,4,5,6]
new_collection = []
for i in collection:
     if not i in new_collection:
          new_collection.append(i)
print(new_collection)"""

# not making the new list removing tin the same list without using loop
"""collection = [2,2,3,3,3,4,5,6]
print(list(set(collection)))"""


# while loop
"""collection = [2,2,3,3,3,4,5,5,6,7]
i = 0 
new_collect = []
while i < len(collection):
    if collection[i] not in new_collect:
        new_collect.append(collection[i])
    i += 1
print(new_collect)"""

#WAP to recognize the duplicate elements  using for loop       [2,2,3,3,3,3,4,5,6]        [2,3]
"""collection = [2,2,3,3,3,3,3,4,5,6]
collect = []
dup_collect = []

for i in collection:
   print(f"The count of collection {i} is {collection.count(i)}")
   if collection.count(i) > 1:
      if i not in dup_collect:
        dup_collect.append(i)
  
print(dup_collect)"""


# do while loop in python is the loop which is actually the while loop with the break statement

while True:
   number = int(input("Enter the number greater than 10: "))
   if number > 10:
      print(number)
      break
   else:
      print("Enter valid number")
      






  





        







    
