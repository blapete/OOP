# Main program for controlling a Bank made up of Accounts


from bank import *
   

# Create an instance of the Bank
oBank = Bank('9 to 5', '123 Main Street, Anytown, USA', '(650) 555-1212')


#Main
while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]      # get the first letter
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'i':
            oBank.getInfo()
        elif action == 'o':
            oBank.openAccount()
        elif action == 'q':
            break
        elif action == 's':
            oBank.show()
        elif action == 'w':
            oBank.withdraw()
    except AbortTransaction as error:
        print(error)        # Print out the text of the error message
        

print('Done')


'''
Top-level menu presented to the user and asks for an action

There is now a try block around the calls to the methods with the oBank object

If any method call raises an AbortTransaction exception, control will be transferred to the except statement

The AbortTransaction exception that was raised at any lower level is handled in the except clause

The value of the exception is assigned to a variable error 

When the variable is printed the user will see the associated error message

Since the exception was handled in the except clause, the program continues running
'''