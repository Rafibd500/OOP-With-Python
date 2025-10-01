class Bank:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.min = 100
        self.max = 100000
    def view_balance(self):
        print(f'Your current balance: {self.balance}')
    def deposit(self, ammount):
        if ammount < self.min:
            print(f'Minimum Ammount to deposit is: {self.min}')
        elif ammount > self.max:
            print(f'Maximum Ammount to deposit is: {self.max}')
        else :
            self.balance += ammount
            print(f'{ammount} TK deposited to your account.')
            self.view_balance()
    def withdraw(self, ammount):
        if ammount < self.min:
            print(f'Minimum Ammount to withdraw is: {self.min}')
        elif ammount > self.max:
            print(f'Maximum Ammount to withdraw is: {self.max}')
        else :
            self.balance -= ammount
            print(f'{ammount} TK withdrawn from your account.')
            self.view_balance()


user1 = Bank('user1')
user1.view_balance()
user1.deposit(1000)
user1.deposit(50000)
user1.withdraw(5000)