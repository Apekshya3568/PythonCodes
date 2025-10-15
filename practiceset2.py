"""numbers = []
for i in range(1,6):
    number = int(input("Enter a list of numbers: "))
    numbers.append(number)
    print(numbers)
square_number = [(x * x if x % 2 == 0 else x) for x in numbers]
even_number = [j for j in numbers if j % 2 == 0]
print(numbers)
print(square_number)
print(even_number)        
"""

"""count  = int(input("Enter how many times yiu want to check for the numbers: "))
for i in range(count):
    number = int(input(f"Enter a number {i +1}")) # as in range it starts with 0 but in this there is {i + 1} which is 1 so it went up to 5
    if number >= 0 :
        if number == 0:
            print("It's a zero")
        else:
            print("It is a positive number")
    else:
        print("It is a negative number")
"""

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
student_info = ("Aakanchhya",21,"Kathmandu")
keys = ("name","age","city")
student_dict = dict(zip(keys,student_info))
print(student_dict)
print(f"{student_dict["name"]} is {student_dict["age"]} years old and lives in {student_dict["city"]}. ")

# Multiplication Table:
# Input a number and print its multiplication table up to 10.
number = int(input("Enter the number for multiplication: "))
for i in range(1,11):
    print(f'{number} * {i} = {number * i}')


# Prime Number Check:
# Ask for a number and check whether it is prime or not.
number = int(input("Enter number: "))

for i in range(2,number):
    if number % i != 0 :
        print("prime")
    else:
        print("composite")
         



    



















