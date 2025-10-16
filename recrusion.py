"""def show(n):
    if n == 0 :
        return
    print(n)
    show(n-1)
    print("end")""" # first n = 3 then it check n== 0 false then it print(n) which id 3 then it goes to show(n-1) whcih is 2 then it print(n) which is 2 then again show(n-1) which
    #is 2-1 = 1 then it agian check n == 0 it is false then it print(n) whch is 1 then again it show(n-1) which is 0 then it check n == 0 it is true then it return then it print("end)
"""show(3)"""
#output is 5 4 3 2 1 first we have given show(5) so n = 5 then n == 0 is false so it goes to print(n) which is 5 then it call again show(5-1) so now n = 4 so print(4) then again 
# show(4-1) then that is 3 so print (n) which is 3 agian show(3-1) which is print(n) is 2 again show(2-1) which is 1 then again print(n) is 1 then show(1-1_ then n = 0 
# and the if n== 0 is true and then it return 

"""def even_no(n):
    if n % 2 == 0:
        print(n)
    if n == 0:
        return
    even_no(n-1)
    print("end")
even_no(3)"""


# Key Points about return
#  return without a value → stops function, returns None by default.
# return with a value → stops function and sends that value back.
# In recursive functions, return is often used to:
# End recursion (base case)
# Pass values back through the recursive call stack/

# facotrial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1) # recrusion relation fact(n) = n * fact(n-1) fact(n-1) = n-1 * fact(n-2)
print(fact(5))

#write a recursive function to calculate the sum of first n natural numbers.

def natural(n):
   
    if n == 0:
        return 0
    return natural(n-1) + n
    
print(natural(5))
    
