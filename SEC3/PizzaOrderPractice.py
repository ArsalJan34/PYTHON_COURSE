print("Welcome to python pizzaaaaa!")
pizza = input("What pizza do you want L, M, S : ")
pepproni = input("Do you want pepproni Y Or N : ")
Extra_cheese = input("Do you want Extra Cheese Y Or N: ")

Bill = 0

if pizza == "S":
  Bill += 15
elif pizza == "M":
  Bill += 20
elif pizza == "L":
  Bill += 25
else:
  print("You typed the wrong input")
if pepproni == "Y":
  if pizza == "S":
    Bill += 2
  else:
    Bill += 3
if Extra_cheese == "Y":
  Bill += 1
  print(f"Your bill will be ${Bill}.")
