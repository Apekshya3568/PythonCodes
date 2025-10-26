# string 
"""
name = "Apekshya"
print(name)
"""

# indexing and slicing 
"""
print(name[0])
print(name[:4])
print(name[0:])
print(name[-4:-1]),
"""

# striing methods
color = "this is the red color which is my fav color"
color.upper()
print(color) # this doesnot change the original string as the upper method is only for temperary str 
print(color.upper())
"""style = " THis is Very Good Style"
print(style.lower())
print(style.replace("Good", "Perfect"))
print(color.startswith("this"))
print(style.endswith("yye"))
print(color.find("the"))
print(color.count("is"))"""

# additional method 
"""location = " I live in hadigaun"
optional_location = location.copy() # string object has no attribute copy
print(optional_location)"""

location = "I live in hadigarun"
optional_location = location[:] # incase you want to copy the str then you can do this 
print(optional_location)

# reverse string as str has no something.reverse() so we use str[::-1]
reverse_location = location[::-1]
print(reverse_location)