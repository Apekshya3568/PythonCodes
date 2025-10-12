#if_else statement
"""age = float(input('Enter your age:'))
if age >= 18:
    print('can vote')
else:
    print('cannot vote')
"""
# elif for multiple conditions
"""marks = int(input('Enter your marks:'))
if marks >= 90:
    print('You have got A grade')
elif marks >=80 and marks < 90:
    print('You have got B grade')
elif marks >= 70 and marks < 80:
    print('You have got C grade')
elif marks >= 60 and marks <70:
    print('You hvae got D grade')
else:
    print('You are fail')
"""

# IF ELSE IN LIST AS WELL 
fruits = ['apple' ,'mango' , 'banana','pineapple']
if 'apple' in fruits:
    print('apple is present') 

# even and odd
num = int(input('Enter the number:'))
if num %2 ==0 :
    print('It is an even number')
else:
    print('It is an odd number')

# multiple of 7 
num = int(input('Enter the number:'))
if num % 7 == 0 :
    print('It is the multiple of 7')
else:
    print('It is not a multiple of 7')



"""workers = ['Gopal', 'Hari', 'Shiva','Ganesh','Sita']
it_workers = ['Shiva','Sita']
bonus_given = []
i = 0
if workers[i] in it_workers:

    
    bonus_given.append(workers[i])
    i += 1
    print(bonus_given)
else:
    print('no bonus')"""




"""workers = ['Gopal', 'Hari', 'Shiva','Ganesh','Sita']
it_workers = ['Shiva','Sita']
bonus_given = []
i = 0
if i <= len(workers):
    for workers[i] in it_workers:
        bonus_given.append(workers[i])
        i += 1
        print(bonus_given)
"""
