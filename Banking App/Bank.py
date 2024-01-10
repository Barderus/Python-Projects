'''
Author: Gabriel dos Reis
Program: Bank.py
Description:
The bank offers the following types of accounts to its customers: 
    * savings accounts
    * checking accounts
    * money market accounts. 
    
Customers are allowed to:
    * deposit money into an account (thereby increasing its balance)
    * withdraw money from an account (thereby decreasing its balance)
    * earn interest on the account
    
Each account has an interest rate. Assume that you are writing a program that will calculate the amount of interest 
earned for a bank account.
'''

class Customer():
    '''
        Customer class that represents a customer object
    '''
    def __init__(self,name, acc_num, exp_date, cv, acc_type):
        '''
            Constructor __init__ that accepts the following arguments:
                name : String --> Customer name
                acc_num : String --> Bank Account number
                exp_date : String --> Account expire date
                cv : String --> Security code
                acc_type : String --> Account type
        '''
        self.__name = name
        self.__acc_num= acc_num
        self.__exp_date = exp_date
        self.__cv = cv
        self.__acc_type = acc_type
    
    # Setters and getters     
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def acc_num(self):
        return self.__acc_num
    @acc_num.setter
    def acc_num(self, acc_num):
        self.__acc_num = acc_num
        
    @property
    def exp_date(self):
        return self.__exp_date
    @exp_date.setter
    def exp_date(self, exp_date):
        self.__exp_date = exp_date
        
    @property
    def cv(self):
        return self.__cv
    @cv.setter
    def cv(self, cv):
        self.__cv = cv
        
    @property
    def type(self):
        return self.__acc_type
    @type.setter
    def type(self, acc_type):
        self.__acc_type = acc_type
        
    def __str__(self):
        display_str = f"Account type: {self.__acc_type}\nAccount Number: {self.__acc_num}\nValid Thru: {self.__exp_date}\tSec code: {self.__cv}\n\t{self.__name}"
        
        return display_str



class Checkings(Customer):
    '''
    Checkings class that allows the user to see their balance, deposit money on the account, 
    withdraw money off the account. It is a subclass of Customer. 
    '''
    def __init__(self, name, acc_num, exp_date, cv, acc_type, balance = 0.0):
        '''
            Constructor class that have as arguments:
                name : String --> Customer name
                acc_num : String --> Bank Account number
                exp_date : String --> Account expire date
                cv : String --> Security code
                acc_type : String --> Account type            
                balance: Float -> Represents user's balance
        '''
    
        # Call the superclass __init__ method and pass the required arguments.
        Customer.__init__(self,name, acc_num, exp_date, cv, acc_type)
        
        self.__balance = balance
        # Dictionary to store checkings account (acc_num : [list of information])
        self.__checkings_acc = {}
        # Dictionary to store transactions (date: [list of transactions])
        self.__transaction = {}
    
    # Allow the user to add money to an account
    def deposit(self, amount):
        self.__balance += amount
    
    # Allow user to withdraw money to an account
    def withdraw(self, amount):
        if self.__balance <= 0:
            print("Sorry, you do not have enough funds in the account to withdraw.")
        else:            
            self.__balance -= amount
       
    # Allows the usert to transfer money between accounts if the account has enough funds
    def transfer(self, recipient, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            recipient.deposit(amount)
            print("Transfer completed.") 
        else:
            print("Sorry, you do not have enough funds in the account to complete this transfer.") 
    
    # Display the balance
    def get_balance(self):
        return self.__balance
    
    # Displaythe bank account information
    def __str__(self) -> str:
        display_str = Customer.acc_num + f"Balance: ${self.__balance}"
        return display_str


  
class Savings(Customer):
    
    '''
        Savings class that allows the user to see their balance, deposit money on the account, 
        withdraw money off the account, and calculate the interest rate. It is a subclass of Customer.
    '''
    def __init__(self, name, acc_num, exp_date, cv, acc_type, balance = 0.0, interest_rate = 0.0):
        '''
        Constructor class that have as arguments:
            name : String --> Customer name
            acc_num : String --> Bank Account number
            exp_date : String --> Account expire date
            cv : String --> Security code
            acc_type : String --> Account type 
            balance: Float -> Represents user's balance
            interest_rate: Float -> Represents the interest rate an account has
        '''
        
        # Call the superclass __init__ method and pass the required arguments.
        Customer.__init__(self,name, acc_num, exp_date, cv, acc_type)
        
        self.__balance = balance
        self.__interest_rate = interest_rate
        
        # Dictionary to store checkings account (acc_num : [list of information])
        self.__checkings_acc = {}
        # Dictionary to store transactions (date: [list of transactions])
        self.__transaction = {}
    
    # Allow the user to add money to an account
    def deposit(self, amount):
        self.__balance += amount
    
    # Allow user to withdraw money to an account
    def withdraw(self, amount):
        if self.__balance <= 0:
            print("Sorry, you do not have enough funds in the account to withdraw.")
        else:            
            self.__balance -= amount
    
    # Calculates the interest rate on an account in a specific amount of time and update the balance
    def calc_interest(self, time):
        interest = self.__balance * self.__interest_rate * time
        self.__balance += interest
        return interest
    
    # Allows the usert to transfer money between accounts if the account has enough funds
    def transfer(self, recipient, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            recipient.deposit(amount)
            print("Transfer completed.") 
        else:
            print("Sorry, you do not have enough funds in the account to complete this transfer.") 
    
    # Display the balance
    def get_balance(self):
        return self.__balance
    
    def __str__(self) -> str:
        ''' String representation of the object '''
        display_str = Customer.acc_num + f"Balance: ${self.__balance}\nInterest rate: {self.__interest_rate * 100:.1f}%"
        
        return display_str



class Transactions(Checkings):
    def __init__(self):
        pass
    def add_transaction(self, transaction):
    # Save transaction information to the file
    # You can use the same approach described in the previous response
        pass

def lookup_transactions(self, date):
    # Look up transactions based on the provided date
    # Retrieve and return transactions for that date from self.transactions
        pass

