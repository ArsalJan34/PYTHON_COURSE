print("Welcome to the RollerCoaster!")
height = int(input("Enter Your Height : "))
bill = 0
if height > 120:
  print("You are welcome to enjoy the ride! ")
  age = int(input("Enter your age please : "))
  if age <= 12:
    bill = 5
    print("you have to pay 5$")
  elif age <= 18:
    bill = 7
    print("You have to pay 7$")
  else:
    bill = 12
    print("you have to pay 12$")
else:
  print("Sorry You have to grow taller to get the ride")
Wants_photo = input("If you want photos press Y :")
if Wants_photo == "Y":
   bill += 3
   print(f"Your bill will be {bill}")
else:
  print(f"Your Bill Will be {bill}")
