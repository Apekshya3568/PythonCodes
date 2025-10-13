# Ask the user for their name and print it in:
# all uppercase
# all lowercase
# and reversed order.

"""name = input('Enter your name: ')
print(name.upper())
print(name.lower())
print(name[::-1])"""

# Write a program that checks if a word entered by the user is a palindrome
"""
word = input("Enter a word: ")
if word == word[::-1]:
    print('This word is palindrome')
else:
    print('This word is not palindrome')"""

# Count how many times the letter "a" appears in you fullname.
"""
full_name = input("Enter your full name :")
print(full_name.count("a"))"""

# Create a list of 5 favorite foods.
# Replace the 3rd food with another one
# Add a new food at the end
# Remove one item of your choice
# Finally, print the updated list.
"""
favourite_foods = ["momo","chowmin","chopsey","thupka","kfc chicken","sizzlers"]
favourite_foods.append("french fries")
print(favourite_foods)
favourite_foods.remove("chopsey")
print(favourite_foods)
favourite_foods.insert(3,"panipuri")
print(favourite_foods)
"""

# You have a list of marks = [78, 56, 89, 90, 66]
# Find and print:
# Maximum mark
# Minimum mark
# Average mark
"""marks = [78,56,89,90,66]
print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))"""

# Write a program that reads 5 numbers from the user and stores them in a list.
# Then print all even numbers separately.
"""numbers = int(input('Enter first number :'))
numbers_list = []
numbers_list.append(numbers)
numbers = int(input('Enter second number :'))
numbers_list.append(numbers)
numbers = int(input('Enter third number :'))
numbers_list.append(numbers)
numbers = int(input('Enter fourth number :'))
numbers_list.append(numbers)
numbers = int(input('Enter fifth  number :'))
numbers_list.append(numbers)
print(numbers_list)
for number in numbers_list:
    if number % 2== 0:
        print(number)"""



# Given a tuple:
# colors = ("red", "blue", "green", "red", "yellow", "red")
# Count how many times "red" appears.
"""colors = ("red","blue","green","red","yellow","red")
print(colors.count("red"))
"""

# Create a dictionary for a student Print only the student’s name and marks.
"""student = {
    "name": "Apekshya",
    "id_no": "5",
    "section": "A",
    "marks": 78

}
print(student.get("name"))
print(student.get("marks"))"""

# Add a new key 'subject': 'Python' to the dictionary above.
# Then update 'marks' to 90 and finally delete 'id_no'.
"""student["subject"] = "Python"
print(student)
student.update({"marks":90})
print(student)
student.pop("id_no")
print(student)
"""

# Make a dictionary of your 3 friends’ names and their ages.
# Print:
# All the names (keys)
# All the ages (values)
"""friends = {
    "Dipshikha" : 22,
    "Kusum" : 21,
    "Ashwini" : 23

}
print(friends.keys())
print(friends.values())
print(friends.items())"""

# Create two sets:Find:
# Union of both
# Intersection of both
"""
foods = {"momo","chowmin","pizza","coke"}
drink ={"coke","limewater","sprite","pizza"}
print(foods.union(drink))
print(foods.intersection(drink))"""

# Add "popcorn" to foods, and remove "chowmin".
# Then print the updated set.
"""
foods.add("popcorn")
print(foods)
foods.remove("chowmin")
print(foods)"""

# Ask user to enter a number.
# Check whether it’s:
# positive
# negative
# or zero
"""number = int(input("Enter a number: "))
if number > 0:
    print("This number is positive")
elif number < 0:
    print("This number is negative")
else:
    print("This number is zero")"""

"""student ={
    'name' : "Aapu",
    'marks' : 90,

}
if student['marks'] >= 90 :
    print('grade A')
elif student['marks'] >= 80 and student['marks'] < 90:
    print('grade B')
elif student['marks'] >= 70 and student['marks'] < 80:
    print('grade c')
else:
    print('fail')
"""


# Create a list of fruits Ask the user to enter a fruit name (any case, e.g. “Banana”).
# Convert the input to lowercase using .lower() and
# check if it exists in the list.
# If yes → print "Yes, it's available!"
# else → print "Sorry, not available."
"""
fruits = ['apple' , 'mango','banana','pineapple','grapes']
fruit = input("Enter the fruit:")
print(fruit.lower())
if fruit or fruits.lower()  in fruits:
    print("Yes- it is available")
else:
    print("No- It is not available")
"""

# You have a list with duplicate items:Convert it into a set to remove duplicates.
# Print how many unique elements are there using len().
"""subjects = ['python','java','php','html','python','css','java','js','c++','c','python','html']
subjects_set = set(subjects)
print(subjects_set)
print(len(subjects_set))
"""

# You have the following dictionary:Task:
# Use .get() to access the marks of "science".
# If marks ≥ 90 → print "Excellent",
# elif marks ≥ 75 → print "Very Good",
# else → print "Keep Improving".

student = {
    'name' : "Aakanchhya",
    'marks' :{
        'science': 92,
        'math' : 89,
        'english': 78,
        'sociology' : 88
    }
}
print(student['marks']['science'])
print(student.get('marks').get('science'))
student_science = student.get('marks').get('science')
print(student_science)
 
"""if student['marks'] >= 90 : # this is not possible in sict 
    print("Excellent")
elif student['marks'] >= 75:
    print("Very Good")
else:
    print("Keep Improving")"""
if student_science >= 90 :
    print("Excellent")
elif student_science >= 75:
    print("Very Good")
else:
    print('Keep Improving')

# Tuple + Dictionary Combination Given:
# student_info = ("Aakanchhya", 21, "Kathmandu")
# keys = ("name", "age", "city")
# Create a dictionary by combining these two tuples using dict(zip(keys, student_info)).
# hen print:
# "Aakanchhya is 21 years old and lives in Kathmandu."
"""
student_info = ("Aakanchhya","21","Kathmandu")
keys = ("name","age","location")
student_dict = dict(zip(keys,student_info))
print(student_dict)
print(f"{student_dict['name']} is {student_dict['age']} years old and lives in {student_dict['location']}.")"""

# String + if–else + Set
# Ask the user to enter a word.
# Convert the word into a set (to get unique letters).
# If the number of unique letters > 5 → print "Interesting word!"
# else → print "Simple word!"

"""word = input("Enter a word : ")
word_set = set(word)
print(word_set)
if len(word_set) >= 5:
    print("Interesting word!")
else:
    print("Simple word")"""


"""number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number")"""

num = int(input("Enter the number: "))
if num >= 0:
    if num == 0:
        print(f"{num} is zero")
    else:
        print(f"{num} is positive number")
else:
    print(f"{num} is negative number")
 

marks = 40
result = "pass"if marks >= 40 else "fail"
print(result)
