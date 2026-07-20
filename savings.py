from main import Account

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._Account__balance * 0.05

s=SavingsAccount(8543,"jeyu")
print(s.calculate_interest())
