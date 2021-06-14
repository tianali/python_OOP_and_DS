class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount): 
        self.account_balance -= amount 
        return self
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: ", (self.account_balance))
    # bonus add a transfer_money method and have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self, other_user, amount): 
        self.account_balance -= amount
        other_user.account_balance += amount
        print("User: " + self.name + ", Balance: ", (self.account_balance))
        print("User: " + other_user.name + ", Balance: ", (other_user.account_balance))

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