import random
import sys

class BalanceChecker(Exception):
    pass

class WinrateChecker(Exception):
    pass

class User_Account:
    def __init__(self, AccountName, InitialBalance, Games_Won, Games_Played ):
        self.name = AccountName
        self.balance = InitialBalance
        self.games_won = Games_Won
        self.games_played = Games_Played
        
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

    def check_player_win_rate(self):
        
        if self.games_played and self.games_won > 0:
            
            winrate = self.games_won / self.games_played * 100
            print(f"\nYour Winrate is: {winrate}")
        else:
            print("\n You haven't palayed games yet.")
        
    
    # def check_games_won(self, won):
    #     pass
    
    # def check_games_played(self, play):
    #     pass
account_balance = 0

account_name = input("Hello, What is your name? : ")
try:
    account_balance = int(input(f"\nHello, {account_name}. How much would you like to deposit? : "))
except ValueError:
    print("\nPlease Integer only")
    
player = User_Account(account_name, account_balance, 0, 0 )

def Bet():
    bet_status = True
    
    while bet_status:
        bot_choice_bet = random.randint(1,2)
        
        if player.balance <= 0:

            print("\n You have no balance please deposit first.")
            main()
        
        else:
            player_amount_bet = int(input("Please enter how much you want to bet? : "))
            player_choice_bet = int(input("Plese enter your number from 1 - 2 : "))

            
            if player_choice_bet == bot_choice_bet:
                player.games_won = player.games_won + 1
                player.games_played = player.games_played + 1
                player.balance = player.balance + player_amount_bet
                print(f"\nYou Won. Your Balance is now ${player.balance}. \nYour Score: {player.games_won}. \nGames Played: {player.games_played}")
                ask_again()
                
            else:
                player.games_played = player.games_played + 1
                player.balance = player.balance - player_amount_bet
                print(f"\nYou Lose. Your Balance is now ${player.balance}. \nYour Score: {player.games_won}. \nGames Played: {player.games_played} ")
                ask_again()

def ask_again():
    player_ask_again = input("\nDo you want to play again?\n 1. Yes \n 2. No \n ")

    if player_ask_again == "1":

        if player.balance <= 0:
                print(f"\nSorry you only have: ${player.balance} balance left. ")
                main()
        else:
            Bet()
    else:
        main()

def main():
    while True:
        action_ask_user = input(f"\n Hello. {account_name}. What action do you want? \n 1. Check Balance \n 2. Deposit \n 3. Bet \n 4. Check Winrate \n 5. Withdraw \n 6. Exit \n \n")

        if action_ask_user == "1":
            player.check_balance()

        elif action_ask_user == "2":
            try:
                player_ask_deposit_amount = int(input("\nHow much do you want to deposit? : "))
                player.balance = player.balance + player_ask_deposit_amount
                print(f"\nYour balance is now: ${player.balance}.")
            except ValueError:
                print("\nPlese input a valid integer")
        
        elif action_ask_user == "3":
            Bet()

        elif action_ask_user == "4":
            player.check_player_win_rate()

        elif action_ask_user == "5":
            player_ask_withdraw_amount = int(input("\nHow much would you like to withdraw? : "))

            player.withdraw_balance(player_ask_withdraw_amount)
            
        elif action_ask_user == "6":
            print(f"\nThank you for playing {player.name}")
            sys.exit()

if __name__ == "__main__":
    main()