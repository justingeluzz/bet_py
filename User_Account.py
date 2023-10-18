import random
import sys

class BalanceChecker(Exception):
    pass

class User_Account:
    def __init__(self, AccountName, InitialBalance ):
        self.name = AccountName
        self.balance = InitialBalance
        
    def check_balance(self):
        print(f"\n Your Balance is: ${self.balance}.")

    def check_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceChecker(
                f"\nSorry. {self.name} only has the balance of {self.balance}"
            )
    
    def withdraw_balance(self, amount):
        try:
            self.check_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.check_balance()

        except BalanceChecker as error:
            print(f"\nWithdraw failed: {error}")

    
        
account_name = input("Hello, What is your name? : ")
account_balance = int(input(f"\nHello, {account_name}. How much would you like to deposit? : "))
    
user_justin = User_Account(account_name, account_balance)

def Bet():
    bet_status = True

    while bet_status:
        bot_choice_bet = random.randint(1,5)
        player_amount_bet = int(input("Please enter how much you want to bet? : "))
        player_choice_bet = input("Plese enter your number from 1 - 5 : ")

        if player_choice_bet == bot_choice_bet:
            user_justin.balance = user_justin.balance + player_amount_bet
            print(f"\nYou Won. Your Balance is now ${user_justin.balance}\n")
            ask_again()
            
        else:
            user_justin.balance = user_justin.balance - player_amount_bet
            print(f"\nYou Lose. Your Balance is now ${user_justin.balance}\n")
            ask_again()

    
def ask_again():
    player_ask_again = input("\nDo you want to play again?\n 1. Yes \n 2. No \n ")

    if player_ask_again == "1":

        if user_justin.balance <= 0:
                print(f"\nSorry you only have: ${user_justin.balance} balance left. ")
                main()
        else:
            Bet()
    else:
        main()


def main():
    while True:
        action_ask_user = input(f"\n Hello. {account_name}. What action do you want? \n 1. Check Balance \n 2. Deposit \n 3. Bet \n 4. Withdraw \n 5. Quit \n \n")

        if action_ask_user == "1":
            user_justin.check_balance()

        elif action_ask_user == "2":
            player_ask_deposit_amount = int(input("\nHow much do you want to deposit? : "))
            user_justin.balance = user_justin.balance + player_ask_deposit_amount
            print(f"\nYour balance is now: ${user_justin.balance}.")
        
        elif action_ask_user == "3":
            Bet()

        elif action_ask_user == "4":
            player_ask_withdraw_amount = int(input("\nHow much would you like to withdraw? : "))

            user_justin.withdraw_balance(player_ask_withdraw_amount)
            
        elif action_ask_user == "5":
            print(f"\nThank you for playing {user_justin.name}")
            sys.exit()

main()