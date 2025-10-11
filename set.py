# set are immutable doesnt change and they are unordered and dont have duplicates value
"""
mySet = { 1,2,3,4,5,6,2,"Hello","bye",5,6 } 
print(mySet) # when we print it came in unordered and the duplicates is also remove 
print(type(mySet))
print(len(mySet))
"""

# empty set 
"""
city = {} # but this is not the empty set this is the empty dictionary 
location = set() # this is the empty set
print(type(city))
print(type(location))
"""

# Methods
""""
score = { 1,2,3,4,5,6,7,8,2,3,4}
print(score)
# print(score[2]) # it will give an error as set are unordered we cannot access it by index
"""

#note
"""
mylist = ['hello' ,'welcome' ,'home']
mylist[1] = 'goodbye' # as it is possible in list to change the value but in set it is not possible as it is immutable the elements
print(mylist)
"""

# 1 method to add the elements as myset.add('elements')
""""
score.add(13)
print(score)
# as we cna add the tule in the set but not the lsit 
paper = {(1,2,3,4), "hello", 2.4,4,5}
print(paper)
paper.add((4,5,6,7))
print(paper)
# paper.add([1,2,3,4]) this will give an error as list cannot be added into the set

# paper.add({1,2,3,4}) this will work as we are adding a tuple
"""



# 2 method as to remove the elemnts myset.remove('elements')
"""
score.remove(8)
print(score)
"""

#3 method is the clear method as myset.clear() it will clear all the elements in the set 
"""
collection ={ 1,2,3,4,5,"hello", (1,2,3,4)}
print(collection)
collection.clear()
print(collection)"""

#4 method is the pop to pop the random element from the set as myset.pop()
"""
collection = { 1,2,3,5,7," hello", ( 1,2,3)}
print(collection)
collection.pop()
print(collection)
"""

# 5 method is union that combines the values from both the set and return the new in old set is doesnt make ansy changes as myset.union(set1)
"""
set1 = { 1,2,3,4}
set2 = { 3,4,5,6}
print(set1.union(set2)) # this creates a new set and then combine the values it doesnot change in set 1 and set 2 like  
print(set1)
print(set2)
"""
# 6 method is the intersection that return the common values from the both the set into the new one myset.intersection(set1)
"""
set1 = { 1,2,3,4}
set2 = { 3,4,5,6}
print(set1.intersection(set2)) # this alos same as union it return the new set and doesnot change in the old set 
print(set1)
print(set2)
"""


# practice questions 
# store following word meaning in a python dictionary
word = {
    'table' : ["a piece of furniture", "list of facts and figures"],
    'cat' : " a small animal"

}

print(word)


# you are given a list of subjects for students . assume one classroom is required for 1 sunject . how many classrooms are needed by all the students
classroom = [ "python" , "java" , "c++", "python" , "javascript", "java", "python","java" ,"c++","c"]
print(len(classroom))
print(set(classroom))
print(len(set(classroom)))

# or store first everything in the set
classrooms = {
    "python" , "java" , "c++", "python" , "javascript", "java", "python","java" ,"c++","c"
}
print(len(classrooms))

# wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one . use subject name as key and marks as value,
subjects ={}
print(subjects)
print(type(subjects))
subjects.update({'maths' : 90})
print(subjects)
subjects.update({"science": 85})
subjects.update({'english' : 98, 'social' : 89})
print(subjects)


# or 
"""
studentMarks = {}
marks = int(input("Enter the marks of maths:"))
studentMarks.update({"maths" : marks})

marks = int(input("Enter the marks of physics:"))
studentMarks.update({"physics": marks})

marks = int(input("Enter the marks of biology :"))
studentMarks.update({"biology" : marks})
print(studentMarks)
"""
# figure out a way to store 9 and 9.0 as sperate values in the set (you can take help of built in data types)
setValues = {9, 9.0, 8 , 8.0}
print(setValues) # but this treat 9 and 9.0 as same so 
# by puttinf one as string 
setValues = { 9 , "9.0" , 8 , "8.0"}
print(setValues)

# by putting in different tuple and storing
setValues = {
    ("int", 9 ), ("float" , 9.0)}
print(setValues)