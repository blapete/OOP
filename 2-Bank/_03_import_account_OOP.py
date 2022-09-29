# from _02_account_OOP import *

# or

from _02_account_OOP import Account



oAccount = Account('Joe Schmoe', 1000, 'magic')
newBalance = oAccount.deposit(500, 'magic')
oAccount.withdraw(250, 'magic')
currentBalance = oAccount.getBalance('magic')
print('current balance:', currentBalance)