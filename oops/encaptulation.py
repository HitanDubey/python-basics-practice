class bankaccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.__balance +=amount

    def withdrawl(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
            
account = bankaccount(1000)
account.deposite(5000)
account.withdrawl(2000)

print(account.get_balance())