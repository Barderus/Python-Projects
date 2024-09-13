"""
"""
import pickle
class Account():
    
    def __init__(self, acc_name, acc_passcode):
        
        self.__acc_name = acc_name
        self.__acc_passcode = acc_passcode
        
    @property
    def acc_name(self):
        return self.__acc_name
    
    @acc_name.setter
    def acc_name(self,name):
        self.__acc_name = name

    @property
    def acc_passcode(self):
        return self.__acc_passcode
    
    @acc_passcode.setter
    def acc_passcode(self, passcode):
        self.__acc_passcode = passcode
    
    def save_account(self, filename):
        accounts = self.load_accounts(filename)
        accounts.append({"Name:":self.__acc_name, "Passcode":self.__acc_passcode})   
        with open(filename, "wb") as file:
            pickle.dump(accounts, file)
            
    def load_accounts(self, filename):
        try:
            with open(filename, "rb") as file:
                accounts = pickle.load(file)
        except FileNotFoundError:
            accounts = []
        return accounts
    