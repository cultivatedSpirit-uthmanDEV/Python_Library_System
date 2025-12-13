
import random

class User():

    def __init__(self):
        self.name = ""
        self.pin = ""
        self.account_number = ""
        self.balance = 0.0
    

    def create_account(self):
        print("     ")
        print("Welcome to Noorlap Banking Ltd")
        print("Create Account")
        print("     ")

        self.name = input("Enter your name: ")
        self.pin = input("Create a 4-digit PIN: ")

        # Generate account number here:
        self.account_number = random.randint(1000000000, 9999999999)

        print("\nAccount Created Successfully!")
        print(f"Name: {self.name}")
        print(f"PIN: {self.pin}")
        print(f"Account Number: {self.account_number}")

    def check_balance(self):
        print("     ")
        print(f"Current Balance: #{self.balance}")
    def deposit_money(self,amount):
        if amount <= 0:
            print("invalid amount")
        else:
         self.balance += amount
         print(f"{amount} has been successfully added!. your new balance : {self.balance}")
         




user1 = User()

user1.create_account()
user1.check_balance()
user1.deposit_money(amount=100.0)


 