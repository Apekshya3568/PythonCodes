# list
"""
fruits = ["mango" , "kiwi" , "avacado","banana"]
print(fruits)
"""

# Accessing and modifying
"""
print(fruits[0]) # accesing
fruits[0] = "pineapple"
print(fruits) # modifying
"""

# list slicing

"""fruits[:3]
print(fruits)
print(fruits[1:])
print(fruits[-2:-1])"""

# methods
# adding and removing elements
"""
print(fruits)
fruits.append("mango") # dont write print(fruits.append)) it will return none as append method doesnot return anythig
print(fruits)
fruits.insert(3,"grapes")
print(fruits)
fruits.remove("avacado")
print(fruits)
fruits.pop() # this will remove the last element 
print(fruits)
fruits.pop(2) # this will remove the element at the index 2
print(fruits) """

# other methods 
"""
fruits.sort() # this will sort in ascednig order
print(fruits)
fruits.sort(reverse = True) # this will sort in descending order
print(fruits)
fruits.reverse() # this will reverse the list
print(fruits)"""
collection = [1,2,3,4,5,6,2,3,2]
print(collection.count(2))





# palindrome practice
"""
collection = input("Enter a string")
if collection == collection[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")"""

# palindrome in list
"""collection_list = [1,2,1]
collection_copy = collection_list.copy()
collection_reverse = collection_copy.reverse() # here this is wrong as if we assign it in collection_reverse it will return none 
if collection_list == collection_reverse:
    print("Palindrome")
else:
    print("Not a Palindromer")

print(collection_list)"""


# the correct method
"""collection_list = [1,2,1]
collection_copy = collection_list.copy()
collection_copy.reverse()
if collection_list == collection_copy:
    print("Palindrome")
else:
    print("Not a Palindromer")"""


list = [(1,2,3,4,5) ,{2,3,4,5,5,6}, {'name' : "Apekshya" , 'location' : "Hadigaun"},[1,2,3,4,5],24,25,26, "Karan", 4.5]
print(list) # in list we can store tuple , set, dictionary , list itself , integer , string, float


