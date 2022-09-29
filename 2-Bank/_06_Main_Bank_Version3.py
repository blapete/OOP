# Version 3, Using a dictionary


from _02_Account import *


# Memory for accounts

accountsDict = {}
nextAccountNumber = 0


# Create 2

oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print('Account number for Joe is:', joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print('Account number for Mary is:', marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()


# Use some methods

print('Calling methods of the two accounts ...')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')


# Show accounts

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()


# Create account from user input

print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('Account number for new account is:', newAccountNumber)
nextAccountNumber = nextAccountNumber + 1


# Show the newly created user account

accountsDict[newAccountNumber].show()


# Deposit 100

accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100, user's balance is:", usersBalance)


# Show the new account
accountsDict[newAccountNumber].show()


for x, y in accountsDict.items():
    print('Key/Account #: ', x, ' Value/Object: ', y)

print()


'''
In the previous version, there is a serious flaw

To close an account and remove it from the list, the pop() method could remove it

The users of accounts still have their account numbers but the index of the list has changed

The users will get account information of other accounts

TO handle large numbers of objects with unique identifiers, a dictionary is the go-to

It allows to delete accounts without altering the account numbers associated with them

To access methods:

oAccount = accountsDict[accountNumber]
oAccount.someMethodCall()

Alternatively:

accountsDict[accountNumber].someMethodCall()
'''