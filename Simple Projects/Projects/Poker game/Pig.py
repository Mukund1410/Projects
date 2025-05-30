import random
from rules import rule
rule()
class player:
    def __init__(self,player_name):
        self.score=0
        self.turns=0
        self.turns_left=True
        self.one_came=0
        self.name=player_name


def turn_left_or_not(players):
    for i in range(0,len(players)):
        if players[i].turns_left==True:
            return True
    return False
        
def rolling_die(player,player_fin):
    while True:
        if player.turns_left==False:
                print(player.name," your chances are exhausted")
                break    
        die=random.randint(1,6)
        if die==1:
            print(die," it is ")
            if player.turns==2:
                print(player.name,"!! Your score will be set to 0 :( Better Luck Next time\n")
                player.score=0
                player.turns+=1    
            print(player.name,"!! Your score will be set to 0 :( please wait for your next turn\n")
            player.one_came=1
            player.score=0
            player.turns+=1
            print("\nCurrent Scores:\t\tTurns Remaining:\n")
            for i in players:
                print(i.name,": ",i.score,"\t\t",i.name,": ",5-i.turns)
            if(player.turns==5):
                print("Hey! ",player.name," Your turns are over, now sit back enjoy the rest of the game! :)")
                player_fin+=1
                player.turns_left=False
            break
        print(die," it is ")
        player.score+=die
        player.turns+=1
        print("\nCurrent Scores:\t\tTurns Remaining:\n")
        for i in players:
            print(i.name,": ",i.score,"\t\t",i.name,": ",5-i.turns)
        if(player.turns==5):
            print("Hey! ",player.name," Your turns are over, now sit back enjoy the rest of the game! :)")
            player_fin=player_fin+1
            player.turns_left=False
            break
        roll=input(f"\n{player.name} you want to roll again or pass to next player? (c/p): ").lower()
        if(roll=='p'):
            break
        

        
player_fin=0
players=[]
player_count=int(input("Enter the number of players who want to play: "))
for i in range(0,player_count):
    player_name=input(f"Enter Player No.{i+1}'s Name: ")
    player1=player(player_name)
    players.append(player1)
    
print("Okay!! Let's Play\n")
while turn_left_or_not(players)==True:
    for i in range(len(players)):
        if players[i].turns_left==True:
            print("It's ",players[i].name,"'s chance \n")
            roll=input(f"{players[i].name} You want to Roll? (y/n): ").lower()
            if roll=='y':
                rolling_die(players[i],player_fin)
            if players[i].turns_left==False:
                # print("Your turns have exhausted ")
                i=(i+1)%player_count
        else:
                print(players[i].name,"'s turns have exhausted ")
                i=(i+1)%player_count
max=0       
for i in players:
    if i.score>max:
        max=i.score
        winner=i.name
    print("Score of ",i.name,": ",i.score)
print("Congratualtions!! ",winner," You Are The winner!!")
    

