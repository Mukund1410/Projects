# def rule():
#     print("Rules of the Game\n")
#     print("   - Each player gets 5 turns to roll the dice.")
#     print("   - A player can choose to roll the dice or pass the turn to the next player at any time during their turn.")
#     print("   - On their turn, the player rolls a six-sided die, which generates a random number between 1 and 6.")
#     print("   - The number rolled on the dice is added to the player's score.")
#     print("   - If a player rolls a 1, their score is reset to 0 for that round, and their turn ends immediately.")
#     print("   - If a player rolls 1 three times across all their turns, they are eliminated from further play.")
#     print("   - After a player has rolled the dice 5 times, their turns are considered exhausted, and they can no longer participate.")
#     print("   - The game continues until all players have exhausted their turns.")
#     print("   - At the end of the game, the scores of all players are displayed.")
#     print("   - The player with the highest score is declared the winner. In case of a tie, the players with the highest score share the win.")
#     print("   - After rolling the dice, the player is given the option to:")
#     print("     - Roll Again to try their luck further, or")
#     print("     - Pass the Turn to avoid the risk of rolling a 1.")
#     print("\n\n\nEnjoy!!")

def get_number_of_racers():
    racers=0
    while True:
        
        racers=input("Enter number of racers (2 - 10): ")
        
        if racers.isdigit():
            racers=int(racers)
        
        else:
            print("Invalid input!.. Please Try Again!")
            continue
        
        if 2<=racers<=10:
            return racers
        else:
            print("Number not in range...Try again!!")
            
racers=get_number_of_racers()
print(racers)