from dataclasses import dataclass
from abc import ABC,abstractmethod
from transaction import Transaction

@dataclass 
class Account(ABC):
    acc_no:int
    name:str
    def __post_init__(self):
        self.__balance=0
        self.transactions=[]
    def deposit(self,amount):
        if amount<0:
            raise ValueError("Balance cant be negative")
        self.__balance+=amount
        self.transactions.append(Transaction("Deposit",amount))
    def withdraw(self,amount):
        if  amount>0 or amount<self.__balance:
            self.__balance-=amount
            self.transactions.append(Transaction("Withdraw",amount))
            return
        raise ValueError("Balance cant be negative")
    @property
    def show_balance(self):
        return self.__balance