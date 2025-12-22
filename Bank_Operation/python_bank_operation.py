
import random

class User():

    def __init__(self):
        self.name = ""
        self.pin = ""
        self.account_number = ""
        self.balance = 0.0


    def accepted_pin(self):
     while True:
        input_pin = input("Create a 4-digit PIN: ")

        if len(input_pin) != 4 or not input_pin.isdigit():
            print("Invalid PIN. PIN must be exactly 4 digits.")
            continue   

        self.pin = input_pin
        print("PIN accepted.")
        break

    

    def create_account(self):
        print("     ")
        print("Welcome to Noorlap Banking Ltd")
        print("Create Account")
        print("     ")
        
        self.name = input("Enter your name: ")
        self.pin = input("Create your 4-digit pin: ")


        #check if the pin is weak

        if self.pin == "1111" or self.pin == "0000":
            print("The pin is too weak. Please choose a stronger one!")
            self.pin = input("Create your 4-digit pin: ")
            return
        self.accepted_pin()
        

        
        ## Make sure the pin is Four digit
    


            
        
            
        


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

    def withdraw_money(self,amount):
        print("     ")
        print("     ")
        if self.balance <= 0:
            print("insuficient balance")
        else:
            self.balance -= amount
            print(f"{amount} has been successfully withdrawn.your balance is {self.balance}")

    def transfer(self,amount,receiver):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        receiver.balance += amount

        print(f"Transfer of {amount} is successful!")
        print(f"Your new balance: ₦{self.balance}")

    def change_pin(self):
        old_pin = input("Create your 4-digit pin: ")
        if old_pin != self.pin:
            print("Incorrect Pin")
            return
        
        new_pin = input("Enter the new pin: ")
        if new_pin == old_pin:
            print("same password!")
            return
        if len(new_pin) != 4:
            print("Invalid pin")

        self.pin = new_pin
        print("Pin successfully changed")


         




user1 = User()
user2 = User()

user1.create_account()
user1.check_balance()
user1.deposit_money(1000.0)
user1.withdraw_money(100)


user2.create_account()
amount = float(input("\nEnter amount to send: "))
user1.transfer(500 , user2)

print("     ")
print("     ")
user1.check_balance()

print("receiver: ")
user2.check_balance()


 