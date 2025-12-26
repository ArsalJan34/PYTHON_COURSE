import random
user = int(input("What do you choose , 0 Rock , 1 Paper, 2 Scissors : "))
computer = random.randint(0,2)
print(f"Computer choice  : {computer}  ")
if user == 0 and computer == 2:
  print("You won")
elif computer > user:
  print("You lost")
elif computer == user:
  print("Its a draw")
else:
  print("you entered invalid input")
