#!/usr/bin/python3

class Checkbook:
    """
    Class representing a simple checkbook system.
    Allows depositing, withdrawing, and checking balance.

    Attributes:
        balance (float): The current balance of the checkbook.
    """

    def __init__(self):
        """
        Initializes the Checkbook object with an initial balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the given amount into the checkbook balance.

        Parameters:
            amount (float): The amount to deposit into the checkbook.

        Prints the amount deposited and the updated balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the given amount from the checkbook balance if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw from the checkbook.

        Prints an error message if there are insufficient funds or the amount withdrawn with the updated balance.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook. Prompts the user for actions like deposit, withdraw, 
    or balance check, and performs the corresponding operations on the checkbook.
    Includes error handling for invalid inputs.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            # Handling invalid input for deposit amount
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            # Handling invalid input for withdraw amount
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
