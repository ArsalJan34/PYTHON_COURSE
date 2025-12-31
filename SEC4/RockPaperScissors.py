import random
user = int(input("What do you choose , 0 Rock , 1 Paper, 2 Scissors : "))
computer = random.randint(0,2)
print(f"Computer choice  : {computer}  ")
if user >= 3 or user < 0:
  print("you entered invalid input")
elif user == 0 and computer == 2:
  print("You won")
elif computer == 0 and user == 2:
  print("You lost")
elif user > computer:
  print("You lost")
elif computer == user:
  print("Its a draw")

