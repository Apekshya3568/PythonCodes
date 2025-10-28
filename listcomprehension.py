"""collection = ["HELLO","WHAT IS UP","welcome","thankyou"]
print([x for x in collection])
"""
"""numbers = [1,2,3,4,5,6]
squares = []
for i in numbers:
    squares.append(i ** 2)
print(squares)"""

"""numbers = [1,2,3,4,5,6]
squares = [i ** 2 for i in numbers]
print(squares)"""


"""fruits = ["apple","banana","pineapple","mango"]
upper_fruits =[]
for i in fruits:
    upper_fruits.append(i.upper())
print(upper_fruits)"""

"""fruits = ["apple","banana","pineapple","mango"]
upper_fruits =[i.upper() for i in fruits]
print(upper_fruits)"""

#add 10 to the each item in the list
"""collection = [5,10,15,20,25,30]
new_collection =[]
for i in collection:
    new_collection.append(i +10)
print(new_collection)
"""
"""collection = [5,10,15,20,25,30]
new_collection = [i + 10 for i in collection]
print(new_collection)"""


# if filter in list comprehension
"""number = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [i for i in number if i % 2 == 0]
print(even_numbers)  """  

"""number = [1,2,3,4,5,6,7,8,9]
even_number = []
for i in number:
    if i % 2 == 0 :
        even_number.append(i)
print(even_number)"""

"""number = [1,12,13,14,15,11,17,16,22,25,24]
even_number = [(i if i % 2 == 0 else i + 1)for i in number]
print(even_number)"""


# number dicisible by 2 and 3 
"""numbers = [i for i in range(50) if i % 2 == 0 if i % 3 == 0]
print(numbers)"""

"""number = [i for i in range(2,14) if i % 2 == 0 if i % 4 == 0]
print(number)"""


"""collection = {x % 3 for x in range(10)} # this is in set as the output 
print(collection)"""

"""list_collection = [x % 3 for x in range(10)] # this is in the list
print(list_collection)"""

"""dict_collection = {x : x*x for x in range(10)} # this is the dict comprehension
print(dict_collection)"""

"""num = [1,2,3]
print({x : x * x for x in num})"""


"""num = [1,2,3]
print([(i *2 if i % 2 == 0 else i *3) for i in num])
"""

"""my_list = [2,3,4,5,6,9]
print(max(num for num in my_list))"""


#dictionary comprehension
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
new_dict = {}
for item in my_dict.items():
    key , value = item
    if value % 2 == 0:
        new_dict.update({key:value ** 2})
print(new_dict)

my_dict = {'a' : 1, 'b': 2,'c':3,'d':4}
print({key :value **2 if value % 2 == 0 else value for key , value in my_dict.items()})
print({key :value **2 for key, value in my_dict.items() if value % 2 == 0})


my_dict = {'a' : 2, 'b' : 3, 'c' : 5,'d':6}
new_dict = {}
for key , value in my_dict.items():
    if value % 2== 0 :
        new_dict.update({key:value**2})
    else:
        new_dict.update({key:value})
print(new_dict)
