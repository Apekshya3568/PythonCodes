#wap to print hellp 5 times while loops
"""
greeting = "hello"
i = 1
while i <= 5:
    print(greeting)
    i += 1"""

"""i = 1
while i <= 100:
    print("Welcome, Apekshya" , i)
    i += 1"""

#wap to print numbers from 1 to 10
"""i = 1
while i <= 10:
    print(i)
    i += 1
print("Loop ended")"""

#for loop 
"""for i in range(1,11):  # for loop doesnot need to do i += 1 like while loop as in range we have range(start, stop, step) and when we dont initialize step it is += 1
    print(i)
    
print("Loop ended ")"""

#WAP TO PRINT NUMBERS IN REVERS AS FROM10 TO 1 
"""i = 10 
while i >= 1:
    print(i)
    i -= 1
print("Loop ended")"""

# for loop 
"""for i in range (10,0,-1):
    print(i)
    
print("Loop ended")"""

"""i = 5
while i >= 1:
    print(i * "*")
    i -= 1
print("Loop ended")"""

# practice set 
#print numbers from 1 to 100 using while loop
# while loop
"""i = 1
while i <= 100 : # this is our stopping condiitons
    print("while loop ",i)
    i += 1"""


# for loop
"""for i in range( 1, 101):
    print("for loop ",i)"""


# print numbers from 100 to 1. 
# while loop
"""i = 100
while i >= 1:
    print("While loop", i)
    i -= 1"""

# for loop
"""for i in range(100, 1, -1):
    print("for loop", i)
"""

# print the multiplication table of a number n
#while loop
"""number = int(input("Enter a number for the multiplicaiton table: "))
i = 1
while i <= 10:
    print(f"{number } * {i} = {number*i}")
    i += 1"""
# for loop
"""num = int(input("Enter the number for the multiplication table : "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")"""

# print the elements of the following list using a loop
# while loop
"""list_elements = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(list_elements): # when we did while i <= len(list_elements) then it give an error as listelements ois 0- 9 but  len = 10 and we did i <= len() so it is list out of range when i = 10
    print(list_elements[i])
    i += 1"""

 # for loop
"""list_elements = [1,4,9,16,25,36,49,64,81,100]
for i in range(0,len(list_elements)):
    print(list_elements[i])"""

# search for a number x in this tuple using a loop
# while loop
"""tuple_elements = (1,4,9,16,25,36,49,64,81,100)
search_elements = int(input("Enter the searching element: "))
i = 0
while i < len(tuple_elements):
    if tuple_elements[i] == search_elements:
        print(f"'search element is found at index' {i} {search_elements}")
    
    i += 1"""

#for looop
"""tuple_elements = (1,4,9,16,25,36,49,64,81,100)
search_elements = int(input("Enter the element you want to search: "))
for i in range(0,len(tuple_elements)):
    if(search_elements == tuple_elements[i]):
        print("search eleemt found at index", i)
"""
# other method
"""tuple_elements = (1,4,9,16,25,36,49,64,81,100)
search_elements = int(input("Enter the element you want to search: "))
for i in tuple_elements:
    if i == search_elements:
        print("Found")"""



# break keyword
"""i = 0
while i <= 5:
    print(i)
    if (i == 3):
        break
    i += 1
    print("This will not be print")
print("This break key word terminate the loop")"""

#continue
"""i = 0
while i <= 5:
    
    if(i == 3):
        i += 1
        continue # it act as skip continue pachi ko all will be skip for that iteration
    print(i)
    i += 1"""

#print the odd nu from1 to 10 using continue
"""i = 1
while i <= 10:
    if(i %2 == 0):
        i += 1
        continue
    print(i)
    i += 1"""

#print the even numbers from 1 to 10 using continue
"""i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1"""

#for loop 
#LIST
"""vegetables = ["spanish","brocooli","cabage","bitter guard","crowliflower"]
for veggi in vegetables:
    print(veggi)"""
 
# TUPLE
"""meat = ("chicken","prawn","red meat","pork","fish meat")
for eat in meat:
    print(eat)"""

#string
"""name = "Apekshya"
for char in name:# it traverse in each letters
    print(char) # 
else:
    print('end')"""


"""name = "Aakanchhya"
for char in name:
    if char == "c":
        print("c found")
        break
    print(char)
else: # in this case end will not get print
    print("End")"""

"""name ="karan"
for char in name:
    if char == "r":
        continue

    print(char)
else:
    print("end")"""


# search for the element in the tuple
"""elements = (1,4,16,36,49,64)
idx = 0
search_elements = int(input("enter the elements you want to search: "))
for ele in elements:
    if (ele == search_elements):
        print("search element found",idx)
    idx += 1"""

# even numbers
"""for i in range(2,100,2):
    print(i)"""

#odd numbers 
"""for i in range(1,100,2):
    print(i)
"""

#print numbers from 1 to 100 using for loop
"""for i in range(1,101):
    print(i)
"""
# print numbers from 100 to 1
"""for i in range (100, 0,-1):
    print(i)"""

#print the multiplication table of a number n
"""number = int(input("Enter the number for the multiplication number: "))
for i in range(1,11):
    
    print(f"{number} * {i} =  {number* i}")"""

# pass statement can be used in if else and loop case
"""for i in range(1,10): # this will also work only if we give in for loop inside pass 
    pass

print("hello")
"""


# wap tp find the sum of first n number (using while and for loop)
# while loop
"""number = int(input("Enter the first n number to be sum: "))
sum = 0 
i = 1
while i <= number:
    sum = sum + i
    print(sum)
    i += 1"""

#for loop
"""number = int(input("Enter a number: "))
sum = 0
for i in range(1,number +1):
    sum = sum + i
    print(sum)
print("total sum is",sum)
"""

# wap ro find the factiorial of fist n number .(using while and for loop)
#for loop
"""number = int(input("Enter the number to find the factorial: "))
fact = 1
for i in range(1,number+1):
    fact = fact * i
    print(fact)
print("factorial number is ",fact)"""
"""
number = int(input("Enter the number to find the factorial: "))
fact = 1
i = 1
while i <= number:
    fact = fact * i
    print(fact)
    i += 1
print("factorial number is",fact)"""

"""fruits = ["apple","banana","mango","pineapple"]
for i in fruits:
    if i == "mango":
        continue
    print(i)"""


#nested loop
foods = ("momo","chowmin",'garlic bread',"noodles")
fruits = ["apple","mango","banana","pineapple"]
for i in foods:
    for j in fruits:
        print(i,j)

        









