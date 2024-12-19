import random

#defining the variable and checking the number of times the user is playing
def paradox():
  global payoff, toss
  payoff = 1
  toss = 1

  while True:
    coin = random.choice(["heads","tails"])
    print("The toss outcome is ", coin)
    
    if coin == "heads":
      break
    else:
      payoff = payoff ** 2
      toss += 1

    return payoff, toss

#comparing the amount and payoff
def gain_loss(x):
  paradox()
  gain = payoff - x
  loss = x - payoff
  print("You gained ", gain, "and you lost ", loss)

#calling the function and running the paradox
def game():
  global x
  x = int(input("How much are you willing to pay for the game?"))
  gain_loss(x)

  chance = input("Do you want to play again: Yes or No ").lower()
  if chance == "yes":
    game()

game()
