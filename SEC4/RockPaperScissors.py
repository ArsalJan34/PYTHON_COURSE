import random
user = int(input("What do you choose , 0 Rock , 1 Paper, 2 Scissors : "))
computer = random.randint(0,2)
print(f"Computer choice  : {computer}  ")
if user > computer:
  print("You won")
else:
  print("You lost")
