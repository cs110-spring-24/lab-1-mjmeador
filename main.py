import random
cpu = random.randint(1,3)
user = input("Rock, Paper, or Scissors? ")

if user == "rock":
  if cpu == 1: # the cpu chose rock
    print("Nobody wins. Both players are executed")
  elif cpu == 2: # the cpu chose paper
    print("You are 50 billion in debt now")
  else:  # the cpu chose scissors
    print("Yay! your children are saved.")

if user == "paper":
  if cpu == 1: # the cpu chose rock
    print("You win 10 pesos.")
  elif cpu == 2: # the cpu chose paper 
    print("Tie game. This device will self destruct in 5 seconds.")
  else: # the cpu chose scissors
    print("Your bones turn to dust.")

if user == "scissors": 
  if cpu == 1: # the cpu chose rock
    print("You are now on fire") 
  elif cpu == 2: # the cpu chose paper
    print("Your lifespan has extended by 10 years.")
  else: # the cpu chose scissors
    print("No contest. The world colllapses.")




