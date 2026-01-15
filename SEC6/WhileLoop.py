# using same example for while loop
def turn_right():
 turn_left()
 turn_left()
 turn_left()

def jump():
 move()
 turn_left()
 move()
 turn_right()
 move()
 turn_right()
 move()
 turn_left()


number_of_hurdles = 6
while number_of_hurdles > 0:
 jump()
#  its jumps while its greater than 0
# and when loop gets completed we will decrease the number of hurdles
 number_of_hurdles -=1
 print(number_of_hurdles)


# hurdles examples two it shuffles the goal so we put the same code but change the while loop here
# so
while not at_goal():
   jump()
# when it reaches the goal the loop will stop or it will keep repeating
