# Version 2, Using a list


from _02_Account import *


# Memory for accounts

accountsList = [ ]  


# Starter accounts for testing

oAccount = Account('Joe', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Mary's account number is 1")

accountsList[0].show()
accountsList[1].show()
print()


# Use some methods

print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')


# Show accounts

accountsList[0].show()
accountsList[1].show()


# Create account from user input

print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)  # append to list of accounts


# Show the newly created user account

print('Created new account, account number is 2')
accountsList[2].show()


# Deposit 100

accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print()
print("After depositing 100, user's balance is:", usersBalance)


# Show new account

accountsList[2].show()


for p in accountsList:
    print(p)

print()


'''
The difference between this and version 1:

Now, there is only one global variable - accountsList

This is a good step to reduce the number of global variables

Also, oAccount is serving as a temporary variable

When a new Account object is created, the result is assigned to the variable oAccount

Right after that, it gets appended to the list of accounts

The variable then gets reused
'''