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

first_name = "Apekshya"
last_name = "Lamichhane"
print(f"This is {first_name} {last_name} presenting the slides")


is_cold = False
is_rainy = False
if is_cold and is_rainy:
    print("Wear warm clothes and take umbrella")
elif is_cold or is_rainy:
    print("Wear warm clothes or take an umbrella")
else:
    print("you are good to go")
