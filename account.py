# Custom exception
class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass


class Account():

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance
        
    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('You cannot withdraw more than you have in your account')

        self.balance = self.balance - amountToWithdraw
        return self.balance

    # For testing
    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)


'''
- There is no code in this class to handle an AbortTransaction exception
- Any time one is raised, control is passed back to the caller
- If the caller has no code to handle the exception, control is passed back to the previous caller
- Repeats up the stack of calls
- Main file will handle it
'''