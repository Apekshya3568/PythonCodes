"""numbers = []
for i in range(1,6):
    number = int(input("Enter a list of numbers: "))
    numbers.append(number)
    print(numbers)
square_number = [(x * x if x % 2 == 0 else x) for x in numbers]
even_number = [j for j in numbers if j % 2 == 0]
print(numbers)
print(square_number)
print(even_number)"""        


"""count  = int(input("Enter how many times yiu want to check for the numbers: "))
for i in range(count):
    number = int(input(f"Enter a number {i +1}")) # as in range it starts with 0 but in this there is {i + 1} which is 1 so it went up to 5
    if number >= 0 :
        if number == 0:
            print("It's a zero")
        else:
            print("It is a positive number")
    else:
        print("It is a negative number")"""


#Even or Odd from 1 to N:
#Take an integer n and print all even numbers from 1 to n using a loop.
"""n = int(input("Enter a number n "))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i)"""

# Count Vowels in a String:
# Input a string and count how many vowels it has (a, e, i, o, u).
# one way
"""str = input("Enter a string: ") #ApekshyaLamichhane
vowels = 0
vowels_str ="a","i","e","o","u"
for x in str:
    for y in vowels_str:
        if x == y:
            vowels += 1
print(vowels)
"""
#next way
"""str = input("Enter a string: ")
vowels_letters = "aeiouAEIOU"
vowels = 0
for i in str:
    if i in vowels_letters:
        vowels += 1
print(vowels)"""


# Sum of Digits:
# Ask for a number and calculate the sum of its digits using a while loop.
# Example: 123 → 6

"""
num = input("Enter a number: ")

sum_of_digits = 0
for digit in num:
    sum_of_digits += int(digit)

print("Sum of digits:", sum_of_digits)
"""

"""numbers = int(input("Enter a number: "))
sum = 0
while i >0:
    sum = sum + i
    i += 1
print(sum)"""


"""n = 123
sum = 0
digit = n % 10
sum += digit 
n = n // 10
print(digit)
print(sum)
print(n)"""


"""num = int(input("Enter a  three number: "))
sum = 0
while num  > 0:
    digit = num % 10
    sum += digit 
    num = num // 10 
print(sum)"""

"""number = input("Enter a number: ")
sum_digit = 0
for i in number:
    sum_digit += int(i)
print(sum_digit)"""

# Reverse a String:
# Input a string and print its reverse using a loop (don’t use slicing).
#while_loop
"""str = input("Enter a string: ")
reversed_string = ""
i = len(str) -1
print(i)
while i >= 0:
    print(str[i])
    reversed_string += str[i]
    i -= 1
print(reversed_string)"""

#for loop
"""str = input("Enter a string: ")
reversed_str = ""
for i in str:
    reversed_str = i + reversed_str
print(reversed_str)"""

# Find Maximum Number in a List (without max()):
# Use a for loop to find the largest number in a list.
#for loop
"""number = [1,2,3,4,5,6]
maximum = 0
for i in number:
    if maximum < i:
        maximum = i
print(maximum)"""


#while loop
"""count = int(input("How many no you want to add in the list: "))
maximum = 0
collection = []
j = 0
for i in range(count):
    number = int(input(f"Enter the number:{i + 1}  "))
    collection.append(number)
print(collection)
while j < len(collection):
    if maximum < collection[j]:
        maximum = collection[j]
    j += 1
print(maximum)"""


# Remove Duplicates from a List:
# Given [1,2,2,3,4,4,5], remove duplicates and print the unique elements.
"""number = [1,2,2,3,4,4,5]
unique_number = []
for i in number:
    if i not in unique_number:
        unique_number.append(i)
print(unique_number)"""

# duplicates no 
"""number = [1,2,2,3,4,4,5]
duplicate_number = []
for i in number:
    if number.count(i) > 1:
        if i not in duplicate_number:
            duplicate_number.append(i)
print(duplicate_number)"""

# Count Occurrences:
# Given a list of numbers, count how many times each number appears using a dictionary.
"""numbers = [1,2,2,3,4,5,6,7]
dict_occur = [{x:numbers.count(x) for x in numbers}]
print(dict_occur)"""


"""numbers = [1,2,2,3,4,5,6,7]
count = {}
for i in numbers:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
"""

# Set Operations:
# Given two sets:
# A = {1,2,3,4,5}
# B = {4,5,6,7,8}
# Print:
# Union
# Intersection
# Difference (A−B)

"""A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))"""


# Tuple to Dictionary Conversion:
# You have:
# student_info = ("Aakanchhya", 21, "Kathmandu")
# keys = ("name", "age", "city")
# Convert them into a dictionary and print:
# "Aakanchhya is 21 years old and lives in Kathmandu."
"""student_info = ("Aakanchhya",21,"Kathmandu")
keys = ("name","age","city")
student_dict = dict(zip(keys,student_info))
print(student_dict)
print(f"{student_dict["name"]} is {student_dict["age"]} years old and lives in {student_dict["city"]}. ")"""

# Multiplication Table:
# Input a number and print its multiplication table up to 10.
"""number = int(input("Enter the number for multiplication: "))
for i in range(1,11):
    print(f'{number} * {i} = {number * i}')"""


# Prime Number Check:
# Ask for a number and check whether it is prime or not.


"""n = int(input("Enter a number to check wheather it is prime or composite: "))
number = ''
for i in range(1,n): # here loops runs only for i = 1 as i is between 1, 2 and in range(1,2) 2 will not include
    if n % i == 0 and i != 1:
       print(f"{i} = {number}")
       number = "composite"
       break
    else:
        number = "prime"
print(number)
        """

    
"""n = int(input("Enter a number: "))
for i in range(2,n):
    if n % i == 0:
        print(f"Composite number{n}")
        break
    else:
        print(f"Prime {n}")"""
    
# Sum of Even Numbers in a List:
# Input a list and find the sum of all even numbers.
"""numbers = []
count = int(input("Enter hoe many times you want to input the number: "))
for i in range(count):
    num = int(input("Enter the number in the list: "))
    numbers.append(num)
print(numbers)
sum = 0
even_numbers = []
for j in numbers:
    if j % 2 == 0:
        even_numbers.append(j)
        sum += j
print(even_numbers)
print(sum)"""


# find the prime from 1 to n
#composite no from 1 to n
"""n = int(input("Enter n: "))
i = 2 
while i <= n:
    flag = 0
    for j in range(2,i):
        if  i % j == 0:
            flag = 1
            break
    if flag == 1:
        print(i )
    i += 1"""

#prime no from 1 to n
"""n = int(input("Enter a number: "))
i = 2
while i <= n:
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag =1
            break
    if flag == 0:
        #print(i)
        # if we want output in same line seperated by space
        print(i,end=' ')
    print("hello")
    i += 1"""


# you have three integers - l , r and k . find how many numbers between l and r (both inclusive)( this means including that no as well) are divisible by k.
#you do not need to print these no, you just have to find their count
"""l = int(input("Enter a number: "))
r = int(input("Enter a number: "))
k = int(input("Enter a number: "))
count_no = 0
for i in range(l,r+1):
    if i % k == 0:
        count_no += 1
print(count_no)"""

# we can also 
"""else:
        print(count_no)
"""

#talking the input in one line and then splitting according to the value
"""l,r,k = input().split()
print(l)
print(type(l))""" # this will provide an type str as it is a string
# we know we need to put int in fron of input but
# if we do this l,r,k = int(input().split()) this provides an error
#so we need to do it seperatly
"""l = int(l)
r = int(r)
k = int(k)
print(l)
print(type(l))
print(r)
print(type(r))
print(k)
print(type(k))"""


#photos dimension questions
"""n_photos = int(input("Enter the no of phtos: "))
length_photos = int(input("Enter a length of photos: "))
i = 1
while i <= n_photos:
    weight_photos = int(input('Enter the weight of photos: '))
    height_photos = int(input("Enter the height of photo: "))
    if weight_photos < length_photos or height_photos < length_photos:
        print("UPLOAD ANOTHER")
    elif weight_photos > length_photos and height_photos > length_photos:
        if weight_photos == height_photos:
            print("ACCEPTED")
        else:
            print("CROP IT")
    i += 1"""

#star dimension
"""for i in range(1,6):
    print(" " * (5-2), end = '' )
    print(i * "*")"""
# for i in range(5,0,-1):
#     print(i * "*")


"""n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""
    
#pyramid stars 
''''n = int(input("Enter the number: "))
for i in range(1,n+1): # loop for the no rows
    print(" " * (n-i) , end = '')  # spaces to center the stars
    print("*" * (2 * i -1))''' #print stars
# 2n-1 = 1,3,5,7,9

# write a program to find the factorial of given number 
"""n = int(input("Enter the number to find factorail "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i += 1
print(fact)"""


# vowels to count
my_string = "I am learning python"
vowels_string = "aeiouAEIOU"
count_vowels = 0
for i in my_string:
    for j in vowels_string:
        if i == j:
            count_vowels += 1
print(count_vowels)

#next method to count vowels
"""my_strings = "I am very happy learning python"
vowels = "aeiou"
count = 0
for i in my_strings:
    if i.lower() in vowels:
        count += 1
print(count)"""




# find the longest word in the string
sentence = "I am happy learning python"
longest_word = ''
words = sentence.split()
for i in words:
    if len(i) > len(longest_word):
        longest_word = i
    
print(longest_word)


# fibonnacic number 
# each number is equal to the sum of the preceding two numbers. eg: 0112358
n = int(input("Enter the number: ")) # 5
count = 0
a,b = 0,1
while count < n: #count = 0, 1,2 ,3 ,4
    print(a) # 0 ,1 ,1 ,2,3
    a,b = b , a+b # 1 1, 1 2,2 3,3 5,5 8
    count += 1






















