class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)
        #print(self.account.balance)	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount): 
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.balance

    def transfer_money(self, other_user, amount): 
        self.account.balance -= amount
        other_user.account.balance += amount
        print("User: " + self.name + ", Balance: ", (self.account.balance))
        print("User: " + other_user.name + ", Balance: ", (other_user.account.balance))

class BankAccount: #1
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
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
        print("Balance: ", (self.balance))

    def yield_interest(self): #5
        if self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance
        return self


#Create 3 instances of the User class
bear = User("Bear", "bear@gmail.com")
bugs = User("Bugs", "bugs@gmail.com")
blitzen = User("Blitzen", "blitzen@gmail.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
bear.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
bugs.make_deposit(50).make_deposit(1000).make_withdrawal(10).make_withdrawal(300).display_user_balance()

#Have the third user make 1 deposit and 3 withdrawals and then display their balance 
blitzen.make_deposit(50).make_withdrawal(10).make_withdrawal(300).make_withdrawal(200).display_user_balance()

bear.transfer_money(blitzen, 460)