import random
#the roll function
def roll():
    value_min=1
    value_max=6
#pour gener un nombre aleatoire entre valuemin et max
    roll=random.randint(value_min,value_max) 
    return roll

#le nombre de player
while True:
    players=input("enter the number of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("the number of payers should be between 2and 4")
    else:
        print("invalid,try agrain.")
print(players)
max_score=50
players_score=[ 0 for _ in range(players)] #creer une liste contient le score de chauqe joueur

while max(players_score)< max_score:
    for player_idx in range(players):
        print("\nplayer",player_idx+1," turn has just started!\n")
        current_score=0
        while True:
            should_roll=input("would u like to roll(y? )")
            if should_roll!="y":
                break
            value=roll()
            if value==1:
                print("you rolled a 1! Turn down")
                current_score=0
                break
            else:
                current_score+=value
                print("you rolled a: ",value)

            print("your score is:", current_score)
        players_score[player_idx]+=current_score
        print("your total score is : ",players_score[player_idx])
