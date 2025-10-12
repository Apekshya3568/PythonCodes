#Tuple
schools = ("Brihaspati Vidyasadan", "Texas International", "DAV","Galaxy")
print(schools)
print(type(schools))
collec = ()
print(type(collec))
collection = (1) # this is class int as it is not tuple for the single element 
print(type(collection))
collect = (1,) # this is the class tuple as if we need to store single element
print(type(collect))

# slicing
print(schools[0])
print(schools[:2])
print(schools[2:])

# tuple object doesnot support item assignment it gives and error as tuple is immutable
"""
schools[0] = "BVS"
print(schools)
"""

# methods 
print(schools.index("Galaxy"))

names = ("Ram", "Sita", "Gita", "Ram")
print(names.count("Ram"))


