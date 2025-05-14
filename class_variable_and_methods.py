"""
4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name.
 Add a class method change_bank_name(cls, name) that allows changing the bank name.
 Show that it affects all instances.

"""

class Bank:
    bank_name = "Saad Bank"  # class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name has been changed to: {cls.bank_name}")

    def display(self):
        print(f"{self.account_holder} has an account in {Bank.bank_name}")

# Create instances
acc1 = Bank("Ali")
acc2 = Bank("Zara")

# Display initial bank name
acc1.display()
acc2.display()

# Change the bank name
Bank.change_bank_name("National Trust Bank")

# Display updated bank name
acc1.display()
acc2.display()


        