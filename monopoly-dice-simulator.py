import random

tries = 0
steps = 0

#limits dice-roll tries to three rounds
while tries<3:
    #two dice roll at any given time
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    tries += 1
    steps = steps + dice1 + dice2
    
    #show user dice results
    print(f"You dice results are: {dice1},{dice2}")
    
    #repeat dice rollling if dice results are similar
    if dice1==dice2:
        continue
    else:
        break
#if dice results are similar for a third time consecutive
else:
    print("Go to Jail")
    
#outputs total number of steps
if dice1 != dice2:
    print("You are to move %d steps" %steps)
    