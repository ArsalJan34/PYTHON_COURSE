print("Welcome to the RollerCoaster!")
height = int(input("Enter Your Height : "))
if height > 120:
  print("You are welcome to enjoy the ride! ")
  age = int(input("Enter your age please : "))
  if age <= 12:
    print("you have to pay 5$")
  elif age >= 12 & age <= 18:
    print("You have to pay 7$")
  else:
    print("you have to pay 12$")
else:
  print("Sorry You have to grow taller to get the ride")
Welcome = input("")
if Welcome == "Thank You":
   print("You are welcome, Enjoy your Ride Sir")
else:
  print("Enjoy your Ride")
