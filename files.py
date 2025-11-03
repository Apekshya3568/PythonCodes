# reading to the file
# # """file = open("demo.txt",'r') # demo.txt is in smae folder so it is file other wise you need to copy the path as well as C:\Users\PC\OneDrive\Desktop\pythonn\demo.txt
# data = file.read()


# print(data)
# print(type(data))
# file.close()"""

# """file = open("demo.txt", "r") """# here t is the text file incase if it was binary we use b inary

"""file = open("demo.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(line1) # the output is i am apekshya then we dont see it itn txt but after theat there is /n so 
#      thi is due to /n
#then i am currently .....
print(line2)
file.close()"""

#once we have read a sile the we cannot redline that same file as it gives empty as we need to close that file and then again do read 
"""file = open("demo.txt",'r')
data = file.read()
print(data)

line1 = file.readline() # this gives empty as file is already at the end
print(line1)
file.close()"""


#writing to the file 

"""file = open("demo.txt", "w")
file.write("I am enjoyng my life everyday.") #this overwite and remove the previsouly everyhing and thne write this to it 
file.close()"""

#appending to the file
"""file = open("demo.txt","a")
file.write("I am happy and living a peacefull lifestyle.") # this will append it it the same line ad it is written as the end
file.write("\n Good news is commming") # this will append at the last but in next line as \n
file.close()"""

# the file which doesnot exit but if we go to the mode w and a then it will create that file 
"""file = open("study.txt" , "w") # it creates a study.txt and the write bolw things
file.write("Studying is the part of life.")
file.close()"""


"""file = open("people.txt","a") # this also creates a new file people.txt and add the content to it 
file.write("People are the intelligent living things")
file.close()
"""


#reading and wriing to the file r+ ( doesnot truncate)
"""file = open("study.txt" , "r+")
data = file.read()
file.write("Hello i am Apekshya") # this doesnot truncate as it doesnot delete the content which was already there it just add to the file
print(data)
file.close()"""


"""file = open("demo.txt" , "r+") # this r + add then conten t at the begonong of the file as if it wasd i am then reolace by hellp am 
file.write("Hello")
data = file.read() 
print(data) # here ponter is after hellp so after that the content willl be printed 

file.close() """

# reading and writing to the file w+ (truncate)
"""file = open("study.txt","w+")
data = file.read()
file.write("Welcome to the country. \n Hope you enjoy your journet")
print(data)
data1 = file.read()
print(data1)
file.close()"""

"""file = open("peopele.txt" ,"w+")
file.write("Hello how its going i hop everything is file")
data = file.read()
print(data) # this print empty as w+ there is no data left it is already trincate
file.close()"""


#a+  for appending at the last
"""file = open("demo.txt" ,"a+")
print(file.read()) # this will give empty output as the cursor will be at the end so empty
file.write("Great work") # it goes at the ened
print(file.read())
"""

#with syntax ans inside with we donot need to do f.close() as it doest it automatically by itself
"""with open("study.txt", "r") as f:
    data = f.read()
    print(data)
"""

"""with open("study.txt" ,"w") as file:
    file.write("Lets go")"""



#deleting a file you need a module as os to delete
"""import os
os.remove("peopele.txt") """# this file is remove form the folder


#practice questions
#create anewfile "practice.txt" using python Add the following data in it :
# ....
#waf that replace all the occurance of "java " with python in above file
"""
with open("practice.txt","w") as file:
    file.write("Hi everyone \n we are learning File I/O using java \n Ilike programming in java")"""

"""with open("practice.txt" ,"r") as file:
    data = file.read()
    new_data = data.replace("java","python")
    print(new_data)
    finding_word = data.find("learning")
    print(finding_word)
    if "learning" in data:
        print("Learnign is in data")"""

#NOW CHANGES TO THE file practice.txt inside
"""with open("practice.txt" , "w") as file:
    file.write(new_data)"""

# next method 
"""def check_word():
    word ="learning"
    with open("practice.txt","r") as file:
        data = file.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

check_word()"""

"""def line_check():
    word = "learning"
    with open("practice.txt","r") as file:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        print(line1)
        print(line2)
        print(line3)
        if word in line1:
            print("Word learning found in line1")
        elif word in line2:
            print("Word learning found in line2")
        else:
            print("Word learning found in line3")
line_check()"""

#next method 
"""def check_for_line():
    word = "learnings"
    data =  True # jaba samma data is not empty the loop will run
    line_no = 1
    with open("practice.txt","r") as file:
        while data:
            data = file.readline()
            if (word in data):
                print("Found learning",line_no)
                return
            line_no += 1
    return -1
check_for_line()"""
            

#from a file containg a numbers seperated by comma , print the count of even number
with open("even.txt" , 'r') as file:
    data = file.read()
    new_data = data.split(",")
    print(new_data)
    count = 0
    for item in new_data:
        integ_data = int(item)
        print(item)
        if integ_data % 2 == 0:
            count += 1
    print(count)
        

    