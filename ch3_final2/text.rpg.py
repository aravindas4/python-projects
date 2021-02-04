from sys import exit

def treasure_room():
  print("""
      There is a big treasure box locked with a password
      Yes!, Its password of 1 magical number,
      Guess it carefully!. You have only one chance""")
  guess = "8"
  answer = input(":- ")
  if answer == guess:
    print("\nNice guess, Tressure opened. Congrats you win the game!")
  elif answer :
    game_over("You lost, Suddenly you hear a earthquake sound and house falls, You died")
    play_again()
  else:
    game_over("Go and learn type a number.")

def bear_room():
  print("""
      \nThere is a bear here.
      Behind the bear is another door.
      The bear is eating tasty honey!
      What would you do? (1 or 2)
      1). Fight for Honey.
      2). Try to escape through door by taunting the bear.""")

  answer = input(":- ")
  
  if answer == "1":
    game_over("Oh, The bear killed you.")
  elif answer == "2":
    print("""\noh,Fortunatly the bear moved from the door.
           You can go through it now freely!""")
    Tresure_room()
  else:
    game_over("type a number properly.")

def monster_room():
  print("""
      Now you entered the room of a monster who is hungry!
      The monster is sleeping.
      Behind the monster, there is another door.
      What would you do? (1 or 2)
      1). Show time!. Fight and kill the monster
      2). Go through the door silently and carfeully.""")
  answer = input(":- ")

  if answer == "1":
    game_over("""The monster woke and fight with you
               But! killed and ate you.""")
  elif answer == "2":
    treasure_room()
  else:
    game_over("Type a number properly.")

def play_again():
  print("\nDo you want to play again? (y or n)")

  answer = input(":- ").lower()
  if "y" in answer:
    start()
  else:
    exit()


def game_over(reason):
  print("\n" + reason)
  print("Game Over!")
  play_again()


def game_start():
  print("""
      You are standing ahead of haunted house.
      And you have two choices,(1 or 2)
      1) either open the gate and enter
      2) Leave that and move on""")

  answer = int(input(":- "))
  if answer == 1:
    print("""
          Now you are in front of two doors,
          LEFT and RIGHT, 
          which one do you take? (l or r)""")
  
    answer = input(":- ").lower()
    if ("l" or "left") in answer:
      bear_room()
    elif ("r" or "right") in answer:
      monster_room()
    else:
      game_over("type properly.Try again!.")
  
  elif answer == 2:
    game_over("Visit once")

game_start()