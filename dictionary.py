#  Dictionary
# data = {
#     'name': ['Aapu','priti'],
#     'age': [22,23],
#     'location':['hadigaun','kapan']
# }
# print(data)

#  we can also store the list , tuple in dictinary
"""
info = {
    'name' : 'youtubefam',
   'subjects' : [ 'python ', 'java', 'c++'],
    'topics'  : ('dict' , 'list'),
    'is_adult' : False,
    'rating' : 3.9
    }
print(info)
print(type(info))
print(len(info))"""



#  to get the values from the key
"""
print(info['subjects'])
print(info.get('is_adult'))
print(info.get('name','rating'))"""


#  to assign or add new key value pair
""" info['playlist'] = ['python', 'java', 'c++', 'js' , 'html']
print(info)
"""

#  you can also chage the value of the key 
"""info["is_adult"] = "is_younger" # as you chage the value of is_adult  which was true to is_younger 
print(info)
"""


#  fist create a null dict and then add key and valuesin it 
"""
school = {}
print(type(school))
print(len(school))
print(school)
school['name'] = "Bidhya"
school['location'] = "Patan"
print(school)
"""

#  nested dictionary
"""
classroom = {
    'name' : " Gopal",
    'marks' : {
        'maths' : 90,
        'science' : 76,
        'social' : 89,
        'english' : 78
    },
    'section' : 'A',
    'attendence' : 90
    }

print(classroom)
print(classroom['marks']['maths'])
print(classroom['marks']['social'])
print(classroom['name'], classroom['section'])"""



#mehods
#1 to take out all the keys  mydict.heys()
classroom = {
    'name' : " Gopal",
    'marks' : {
        'maths' : 90,
        'science' : 76,
        'social' : 89,
        'english' : 78
    },
    'section' : 'A',
    'attendence' : 90
    }
"""
print(classroom.keys()) # nesteded keys doesnot return 
print(list(classroom.keys())) # we can ao convert it into the list 
print(tuple(classroom.keys())) # we can also convert it into the tuple 
print(len(list(classroom.keys()))) 
print(set(classroom.keys())) # we can also convert it into dict

#2 method to take out all the values mydict.values()
print(classroom.values()) # it also return the nested values""" 

#3 methos to take out key value pair mydict.items()
print(classroom.items())
print(list(classroom.items()))
pairs = list(classroom.items())
print(pairs[2])

# 4 method which returns the key according to the value mydict.get('key')
print(classroom['name']) # we have this as well to get the value of the key but this is not preferred as when we give the key anme wrong then it will give error' \
print(classroom.get('name')) # this is perferred as it odesnot give eroor if the name in the key is not correct it will give none


# 5 method to update the dictionay or if we want to chage the values of the key which is already in the dict as to overwrite 
new_dict = { 'age' :22 , 'grade' : 5}
classroom.update(new_dict)
print(classroom)
# overwrite the values of the dict as in the name we have Gopal now we chage it tinto the shiva
classroom.update({'name' : 'Shiva'})
print(classroom)


#  note we can store dictionayr inside the list as well list inside the dictionary
"""
mydict = {
    'name' :['Ram' ,'Sita','Gita'],
    'location' :['kapan','Patan','Thamel']

}
print(mydict)

mylist = [
    {'name' : 'Ram', 'age' : 22, 'location' :'Chabil'},

    {'name' : 'Sita' , 'age' : 23 , 'location' : 'Kapan'}
]
print(mylist)

mytuple = ([1,2,3],{
    'name' : 'Ram','age': 22 , 'location' : 'Kapan'},
    {'name' : 'Sita' , 'age' :23 , 'location' : 'Patan'},{1,2,3,4,5},(5,6,7)

)
print(mytuple)
"""

word = {
    'table' : ["a piece of furniture", "list of facts and figures"],
    'cat' : " a small animal"

}

print(word)