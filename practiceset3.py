# #WAP to make the weight conversion calculator
# take the input weight from user
# take the unit i.e take K or L for kgs or pounds
# if the unit is in kg, convert to pound
# if the unit is in pound, convert to kg, also make the program continuos(using while True)
# if ther unit types wrong unit, tell the unit is incorrect
# if the user gives string in weight, destroy the loop
# thank him for using the Calculator         note: 45 kg  = 100 pound
#                                                       0.45kg   =  1 pound


#this is the wring code 
"""while True:
    weight = int(input("Enter the weight: "))
    unit = input("Enter the unit: ").upper()
    if weight is weight.isdigit():
        if weight == " ":
            break
        if unit == 'KG':
            pound = weight/0.45
            print(f"Your weight is {pound} pound")
        elif unit == 'P':
            kg = weight * 0.45
            print(f"Your weight is  {kg} kg")
        else:
            print("The unit is incorrect")
        break
    else:
        print("Please eneter a digit")
        break"""

#correct method
"""while True:
    weight = input('Enter the weight or text to exit: ')
    if not weight.isdigit():
        print("Thankyou for comming but the weight is wring input")
        break
    weight_input = int(weight)
    unit = input("Enter the unit: ").upper()
    if unit == 'KG':
        pound = weight_input/0.45
        print(f"Your weight is {pound} pound")
    elif unit == 'P':
        kg = weight_input * 0.45
        print(f"Your weight is  {kg} kg")
    else:
        print("The unit is incorrect")
        break
else:
    print("byebe")""" # this will not be printed as it is inside the else and after break this will not be printed 
# print("byebye") # this will be printed 


# my_list = [2,3,1,5,7,9,6] this is the list print this list in descending order
"""my_list = [2,3,1,4,5,9,6]
my_list.sort(reverse = True)
print(my_list)"""


"""my_list = [2,3,1,4,5,9,6]
desc_list = []
i = 0
maximum = 0
while i < len(my_list):
    maximum = 0
    for item in my_list:
        if item > maximum:
            if item not in desc_list:
                maximum = item

    desc_list.append(maximum)
    i += 1
print(desc_list)"""


"""def greet():
    return "Hello"
    print(20)
greet() # this doesnot give any output as we did it hello in return 
print(greet())""" # it goves an output hellp as we did print(greet()) and it doesnot print(20) as it comes after return and like break in return it goes out of the function

"""def even(n):
    if n % 2 == 0:
        print("true")
even(5)""" # this doesnot give any output

"""def even_odd(n):
    if n % 2 == 0 :
        return True
    return False
print(even_odd(5))
"""



#WAP to find the list of square of given elements of the list
                              # input = [1,2,3,4]         output = [1,4,9,16]
"""my_list = [1,2,3,4]
square_list = []
i = 0
while i < len(my_list):
    square_list.append(my_list[i] ** 2)
    i += 1
print(square_list)"""

#list comprehension
"""print(i ** 2 for i in my_list)""" # this is not the correct code as we need it in list so below is the correct code including the []
"""print([i **2 for i in my_list]) """# this is the correct code 


# this is the worng ocde 
"""dict_collec = {'a' : 1, 'b' : 3}
for i in dict_collec:
    print(i)
    print(i.keys())
    print(i.values())
    print(i.items()) """

for item in {'a' : 1, 'b': 3}:
    print(item)
for item in {'a': 1 ,'b': 3}.keys():
    print(item)
for item in {'a': 1,'b': 3}.values():
    print(item)
for item in {'a' : 1, 'b':2}.items():
    print(item)


    