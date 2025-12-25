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
# this generates random numbers between 0 and 1
random_0_1 = random.random()
print(random_0_1)
# this generates random float numbers between the numbers
random_float = random.uniform(1,10)
print(random_float)
