from main import Account
class Bank:
    def __init__(self):
        self.accounts=[]
        self.total_accounts=0
    @classmethod
    def total_account(cls):
        return cls.total_accounts
    @staticmethod
    def is_valid_amount(amount):
        return amount>0
    def add_acc(self,acc):
        self.accounts.append(acc)
        self.total_accounts+=1
    def remove_acc(self,acc):
        for i in self.accounts:
            if acc == i.acc_no:
                self.accounts.remove(i)
                return "Account removed successfully"
        raise ValueError("Account not found")
        
    def find_acc(self,acc_no):
        for i in self.accounts:
            if i.acc_no == acc_no:
                return i
        raise ValueError("Account  not found")
    def show_acc(self):
        return self.accounts
    