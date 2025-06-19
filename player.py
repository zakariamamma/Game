# hello guys here i make game rock paper scissors and i use some basics python please if see this comment like my code and follow me
# now i creat the game and in future a make the best IA in the WORLD
# you can to copy my code and game play
import time
import random
game = ["1_rock","2_paper","3_scissors"]
print("characters for your games ")
print("\033[33m")
print()
for i in game:
  print(i)
  print(20*"-")
  time.sleep(1.05)

print("\033[33m")
rock = 1
paper = 2
scissors = 3
while True:
  player = int(input("enter your numbers >>> "))
  time.sleep(1.005)
  print()
  repeat = input("do you want to continue >>> ")
  if repeat != "yes":
    break

  IA = random.randint(1,3)

  if player == 1 and IA == 1:
    print("\033[33mdraw\033[0m")

  elif player == 1 and IA == 2:
    print("\033[31mIA is win and you lose \033[0m")

  elif player == 1 and IA == 3:
    print("\033[32myou win and IA the loser\033[0m")

  elif player == 2 and IA == 1:
    print("\033[32myou win and IA the loser\033[0m")

  elif player == 2 and IA == 2:
    print("\033[33mdraw\033[0m")

  elif player == 2 and IA == 3:
    print("\033[31mIA is win and you lose \033[0m")

  elif player == 3 and IA == 1:
    print("\033[31mIA is win and you lose \033[0m")

  elif player == 3 and IA == 2:
    print("\033[32myou wine and IA the loser\033[0m")

  elif player == 3 and IA == 3:
    print("\033[33mdraw\033[0m")
  else:
    print("Error! enter number 1 to 3 ")

print("thank you for playing ")



