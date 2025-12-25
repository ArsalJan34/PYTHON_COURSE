print("Welcome to treasure island")
print("Your mission is to find the lost treaser")
print("You're at cross road where you want to go? ")
# .lower() returns the string coverted into the lowercase
direction = input("Go 'Left' or Go 'Right' : ").lower()
if direction == "Left":
  print("You have come to lake. There is an island on the middle of lake")
else:
  print("You lost the game")
wait = input("Type 'wait' to wait for boat or type 'swim' to swim across the lake  : ")
if wait == "wait":
  print("You have arrived at the island. There is house with three doors")
else:
  print("You have died by drowning")
door = input("Pick a door 'Yellow', 'red', or 'blue' : ")
if door == "yellow":
  print("you have won the game and the treason is yours ")
else:
  print("You have lost the game.Try again")
