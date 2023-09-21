class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        self.__account_balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds!")
    
    def display_balance(self):
        return self.__account_balance


# Example usage:
account = BankAccount("1234567890", "John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(account.display_balance())
