# encapsulation --> Hide details
# access modifier --> public, private, protected
class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name      # public
        self.inital_deposit = initial_deposit
        self.__balance = initial_deposit    # Private
        self._branch = "mirpur 11"           # protected
    def __view_balance(self):
        return f'{self.balance}'
    def deposit(self, ammount):
        self.__balance += ammount
user = Bank('user', 1000)
# print(dir(user))
user.deposit(2000)
print(user._Bank__balance)


