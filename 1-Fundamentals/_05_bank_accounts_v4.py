# Bank account version 4, Any amount of accounts - using lists


# Memory space for the account information
accountNamesList = []
accountBalancesList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)
   
def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('       Name', accountNamesList[accountNumber])
    print('       Balance:', accountBalancesList[accountNumber])
    print('       Password:', accountPasswordsList[accountNumber])
    print()

def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
        
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    
    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] + amountToDeposit
    return accountBalancesList[accountNumber]
    
def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountBalancesList[accountNumber]:
        print('You cannot withdraw more than you have in your account')
        return None

    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalancesList[accountNumber]


# Create two accounts to start with
print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, 'nuts')


# Loop
while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()
    
    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber= input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
        
    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('What is the amount of your initial deposit? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = len(accountNamesList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':
        print('Show:')
        nAccounts = len(accountNamesList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
 
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)       

print('Done')


'''
The data is represented using lists - 3 parallel lists
To create a new account, the appropriate value is appended to each of the 3 lists
The code is still working with global data; now there are 3 global lists of data


   list         list           list            list
    |            |              |               |
Account #  -    Name     -    Password    -    Balance
0          -    Joe      -    soup        -    100
1          -    Mary     -    nuts        -    3550
2          -    Bill     -    frisbee     -    1000
3          -    Sue      -    xyyzz       -    750
4          -    Henry    -    PW          -    10000


All the passwords are grouped together in one list, this is not logical
Also every time you need to add a new attribute to an account like address/phone number, a new
global list needs to be created

A better approach is the following:


Account #  -    Name     -    Password    -    Balance
0          -    Joe      -    soup        -    100      <--- list
1          -    Mary     -    nuts        -    3550     <--- list
2          -    Bill     -    frisbee     -    1000     <--- list
3          -    Sue      -    xyyzz       -    750      <--- list
4          -    Henry    -    PW          -    10000    <--- list


This approach each row is the data assoicated with a single account
Much more natural
'''