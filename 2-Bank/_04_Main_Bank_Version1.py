# Version 1, Using explicit variables for each Account object


from _02_Account import *


# Starter accounts for testing

oJoesAccount = Account('Joe', 100, 'JoesPassword')
print("Created an account for Joe")
oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print("Created an account for Mary")
oJoesAccount.show()
oMarysAccount.show()


# Use some methods

print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')


# Show accounts

oJoesAccount.show()
oMarysAccount.show()


# Create account from user input

print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oNewAccount = Account(userName, userBalance, userPassword)
oNewAccount.show()


# Deposit 100

oNewAccount.deposit(100, userPassword)
usersBalance = oNewAccount.getBalance(userPassword)
print()
print("After depositing 100, user's balance is", usersBalance)
oNewAccount.show()


'''
Each object (oJoesAccount, oMarysAccount, oNewAccount) is a global viable that contains a collection of three instance variables

If the definition of the Account class were to expand (address, phone number, DOB), each object would get a set of these additional instance variables

'''