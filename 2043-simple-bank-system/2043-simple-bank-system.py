class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.length = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in range(1,self.length+1) or account2 not in range(1,self.length+1) or money > self.balance[account1-1]:#checking valid account or not and sufficient funds
            return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in range(1,self.length +1):
            return False
        
        self.balance[account-1] += money
        return True
        
        

    def withdraw(self, account: int, money: int) -> bool:
        if account not in range(1,len(self.balance)+1) or self.balance[account-1] < money:#check if the account is valid or not and have sufficient funds
            return False
        self.balance[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)