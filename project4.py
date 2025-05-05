#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
#that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "National Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change class variable

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Create instances
acc1 = Bank("farral Ayesha")
acc2 = Bank("raid")
acc3 = Bank("orhan sadoon")
# Display info before changing bank name
acc1.display_info()
acc2.display_info()
acc3.display_info()

# Change bank name using class method
Bank.change_bank_name("International Bank")

# Display info after changing bank name
acc1.display_info()
acc2.display_info()
acc3.display_info()