#encapsulation is hiding  the data(variable)inside a single unit(class)
#example
class BankAccount:
    def __init__(self,account_number,balance):
        self.acc_no = account_number
        self.__balance = balance # self_balance is a private variable
        #Getter method _ to safely read the value
    def get_balance(self):
        return self.__balance
        #Setter method - to safely modify the value
    def set_balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            self.__balance += amount
    

account1 = BankAccount(12345,10000)
print(account1.acc_no)
# print(account1.__balance) # this gaives an attribute error as 'BankAccount' object jas no attribute '__balance" this is as __balance is a private variable
print(account1.get_balance()) # this is the correct way to do it
print("Current balance =" ,account1.get_balance())
account1.set_balance(1277) # this is depositing or adding inot the account
print("After update the balance =", account1.get_balance())
account1.set_balance(-77)
print("After update the balance =", account1.get_balance())