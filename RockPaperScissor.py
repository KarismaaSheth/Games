import random
Hands = ["rock", "paper", "scissors"]
score = 0

#checking for invalid data
while True:
  try:
    choice = int(input("Enter the number of times the game is to be played - 3, 5 or 7 "))
    if choice not in [3,5,7]:
      print("It is an invalid input")
      continue
    break
  except ValueError:
    print("Enter one of the given options: 3,5,7 ")

#looping the game according to the number of times the game is to be played 
for i in range(choice):
  option = random.choice(Hands)

  name = input("What is your move?").lower() 

#checking the possibilities of the computer choosing rock
  if option == "rock":

    if name == "rock":
      print("The computer chose ", option)
      print("It is a tie!")
      score += 0
    elif name == "paper":
      print("The computer chose ", option)
      print("You won!")
      score += 1
    elif name == "scissors":
      print("The computer chose ", option)
      print("The computer won!")
      score += 0

#checking the possibilities of the computer choosing paper
  elif option == "paper":

    if name == "rock":
      print("The computer chose ", option)
      print("The computer won!")
      score += 0
    elif name == "paper":
      print("The computer chose ", option)
      print("It is a tie!")
      score += 0
    elif name == "scissors":
      print("The computer chose ", option)
      print("You won!")
      score += 1

#checking the possibilities of the computer choosing scissor
  elif option == "scissors":

    if name == "rock":
      print("The computer chose ", option)
      print("You won!!")
      score += 1
    elif name == "paper":
      print("The computer chose ", option)
      print("The computer won!")
      score += 0
    elif name == "scissors":
      print("The computer chose ", option)
      print("It is a tie!")
      score += 0

#displaying the result
Computer_score = choice - score
print("Your score is ",score, "the computer's score ",Computer_score)

if Computer_score > score:
  print("The computer won the game!")
elif Computer_score == score:
  print("It is a tie!")
else:
  print("You won the game!")
