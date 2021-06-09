class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount): 
        self.account_balance -= amount 
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: " + str(self.account_balance))
    # bonus add a transfer_money method and have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self, other_user, amount): 
        self.account_balance -= amount
        other_user.account_balance += amount
        print("User: " + self.name + ", Balance: " + str(self.account_balance))
        print("User: " + other_user.name + ", Balance: " + str(other_user.account_balance))

#Create 3 instances of the User class
bear = User("Bear", "bear@gmail.com")
bugs = User("Bugs", "bugs@gmail.com")
blitzen = User("Blitzen", "blitzen@gmail.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
bear.make_deposit(100)
bear.make_deposit(200)
bear.make_deposit(300)
bear.make_withdrawal(100)
bear.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
bugs.make_deposit(50)
bugs.make_deposit(1000)
bugs.make_withdrawal(10)
bugs.make_withdrawal(300)
bugs.display_user_balance()

#Have the third user make 1 deposit and 3 withdrawals and then display their balance 
blitzen.make_deposit(50)
blitzen.make_withdrawal(10)
blitzen.make_withdrawal(300)
blitzen.make_withdrawal(200)
blitzen.display_user_balance()

bear.transfer_money(blitzen, 460)