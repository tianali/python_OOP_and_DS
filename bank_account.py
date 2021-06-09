#1. Create a BankAccount class with the attributes interest rate and balance 
#2. Add a deposit method to the BankAccount class
#3. Add a withdraw method to the BankAccount class, if insufficient funds, print message "inssuficient funds: Charging a $5 fee" and deduct $5
#4. Add a display_account_info method to the BankAccount class and have it print to the console eg. "Balance: $100"
#5. Add a yield_interest method to the BankAccount class that increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount: #1
    def __init__(self, balance=0):
        self.int_rate = 0.01
        self.balance = balance

    def deposit(self, amount): #2
        self.balance += amount
        return self
    
    def withdraw(self, amount): #3
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self

    def display_account_info(self): #4
        print("Balance: " + str(self.balance))

    def yield_interest(self): #5
        if self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance
        return self

#Create two accounts
rich = BankAccount(1000)
poor = BankAccount()
print(rich.balance)
print(poor.balance)

#First account - make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (Chaining)
rich.deposit(400).deposit(600).deposit(2000).withdraw(100).yield_interest().display_account_info()

#Second account - make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code
poor.deposit(300).deposit(300).withdraw(10).withdraw(50).withdraw(90).withdraw(800).yield_interest().display_account_info()
