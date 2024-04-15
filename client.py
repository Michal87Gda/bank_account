from result import Error, Success

class Client:
    next_id = 1

    def __init__(self, name:str, balance:int=0):
        self.id = Client.next_id
        self.name = name
        self.balance = balance
        Client.next_id += 1

    def deposit(self, amount : int):
        self.balance += amount
        return f"Client {self.name} has deposited {amount} successfully"

    def try_withdraw(self, amount : int):
        if self.balance < amount:
            return Error("Lack of money", amount)
        else :
            self.balance -= amount
            return Success("Money withdrawed", amount)

    def get_balance(self):
        return f"Your balance is : {self.balance} $$"

    def __str__(self):
        return f"Client {self.name} has now : {self.balance} $$"

class ClientWithMinimum(Client):
    def __init__(self,name, balance=0, minimum_balance = 1000):
        super().__init__(name, balance)
        self.minimumBalance=minimum_balance

    def try_withdraw(self, amount : int):
        if self.balance - amount >= self.minimumBalance:
            return super().try_withdraw(amount)
        else:
            return Error("Balance after withdrawing will be under Your min balance", amount)