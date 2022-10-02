# from _02_account_OOP import *

# ^ bring in the entire contents of the imported file, or


from _02_account_OOP import Account


oAccount = Account('Joe Schmoe', 1000, 'magic')
newBalance = oAccount.deposit(500, 'magic')
oAccount.withdraw(250, 'magic')
currentBalance = oAccount.getBalance('magic')
print('current balance:', currentBalance)


'''
Benefits to importing class code:

1.
The module is reusable

2.
If the class code is included in the main program, every time the program is run Python compiles all the code in the class (it translates it into a lower-level language that is more easily runnable on the computer) even if there are no changes to the class


If the class code is imported:
Python optimizes the compile step, it creates a folder named __pycache__ in the project folder
Python then compiles the code in the class file and saves the compiled code in the __pycache__ folder with a variant of the original Python filename
For example, the original file _02_account_OOP.py will be named _02_account_OOP.cpython-38.pyc (depends on the version of Python), .pyc stands for Python Compiled
Python only recompiles the class file if the source code of the class file changes
If the source code doesn't change, Python can use the .pyc file
'''