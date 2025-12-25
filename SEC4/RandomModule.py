# The random module in Python is a built-in module used to generate random numbers
# and make random selections. It helps in choosing values unpredictably from a
# range, list, or sequence and is commonly used in games, simulations, and testing.
import random
# i can also use an my module using import
import MyModule
random_int = random.randint(1, 10)
if random_int == 4:
  print("You won the game")
else:
  print("Loser!")
  # here we printed the number we added in our mymodule file
print(MyModule.my_module)
