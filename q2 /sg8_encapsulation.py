# Activity 3 : 

class Bankaccount: 
    def _init_ (account_num, balance):
        self.__account_num = account_num
        self.__balance = balance
        
    def set account_num (self, account_num):
        print("Account 1")
        self.__account_num = 12345
        return self.__account_num
        
    def balance (self, balance):
        self.__balance = 1000
        return self.__balance
    
    def update_balance (balance):
        
        if new < 0:
            print("The balance must not be a negative number")
            print("Account number: {account_num} ")
            print("Balance: {balance}")
        if new > 0:
             updated = new + self.__balance
             print("Account number: {account_num} ")
             print("Balance: {new}")
             

a1 = Bankaccount(12345, 1000)

print("Account number: {account_num} ")
print("Balance: {balance}")

new = int(input("Update balance to "))

if new < 0:
  print("The balance must not be a negative number")
  print("Account number: {account_num} ")
  print("Balance: {balance}")
if new > 0:
  updated = new + balance
  
  
