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

    def withdraw_balance(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceChecker(
                f"Sorry. {self.name} only has the balance of {self.balance}"
            )
    
        
account_name = input("Hello, What is your name? : ")
account_balance = int(input(f"Hello, {account_name}. How much would you like to deposit? : "))
    
user_justin = User_Account(account_name, account_balance)

def Bet():
    bet_status = True

    while bet_status:
        bot_choice_bet = random.randint(1,5)
        player_amount_bet = int(input("Please enter how much you want to bet? : "))
        player_choice_bet = input("Plese enter your number from 1 - 5 : ")

        if player_choice_bet == bot_choice_bet:
            user_justin.balance = user_justin.balance + player_amount_bet
            print(f"You Won. Your Balance is now {user_justin.balance}")
            ask_again()
            
            
            
        else:
            user_justin.balance = user_justin.balance - player_amount_bet
            print(f"You Lose. Your Balance is now {user_justin.balance}")
            ask_again()


def ask_again():
    player_ask_again = input("Do you want to play again?\n 1. Yes \n 2. No \n ")

    if player_ask_again == "1":

        if user_justin.balance <= 0:
                print(f"Sorry you only have: ${user_justin.balance} balance left. ")
                main()
        else:
            Bet()
    else:
        main()


def main():
    while True:
        action_ask_user = input(f"\n Hello. {account_name}. What action do you want? \n 1. Check Balance \n 2. Deposit \n 3. Bet \n 4. Withdraw \n 5. Quit \n")

        if action_ask_user == "1":
            user_justin.check_balance()

        elif action_ask_user == "2":
            player_ask_deposit_amount = int(input("How much do you want to deposit? : "))
            user_justin.balance = user_justin.balance + player_ask_deposit_amount
            print(f"Your balance is now: ${user_justin.balance}.")
        
        elif action_ask_user == "3":
            Bet()

       

main()