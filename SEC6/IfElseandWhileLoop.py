def turn_right():
 turn_left()
 turn_left()
 turn_left()

def jump():
#  we are going to remove the move function first move function because it if there is a wall it will still move
#  move()
 turn_left()
 move()
 turn_right()
 move()
 turn_right()
 move()
 turn_left()


while not at_goal():
  if wall_in_front():
   jump()
  else:
   move()

