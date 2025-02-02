#2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.

class BankAccount:

    def __init__(self,amount=10000):
        self.amount=amount
        

    def deposit(self,money):
        self.amount+=money
        print(f'After depositing money the total amount is: {self.amount}')

    def withdraw(self,money):
        if(money<=self.amount):
            self.amount-=money
            print(f'Afetr withdrawing the money the remaining amount is: {self.amount}')
        else:
            print('Sufficient balance is not there in the account')
            print('Please enter lesser amount')

ba=BankAccount()
print("1.Deposit  2.withdraw")
choice=int(input("Please enter your choice"))
if choice==1:
    amount=int(input("please enter the amount to deposit:"))
    ba.deposit(amount)
elif choice==2:
    amount=int(input("Please enter the amount to withdraw: "))
    ba.withdraw(amount)
else:
    print('Please enter a valid choice ')


        

