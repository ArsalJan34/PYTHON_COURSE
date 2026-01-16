def turn_right():
 turn_left()
 turn_left()
 turn_left()

while not at_goal():
  if right_is_clear():
    turn_right()
    move()
  elif front_is_clear():
    move()
  else:
    turn_left()
# its working but not properly so i will learn and come back to make it more workable
