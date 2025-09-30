# print("what is your name?")
input("What is your name?")
# the input function pauses the program and waits for the user to type something
# the input functino takes an optional argument, which is the prompt to display to the user
#  if we print here ("hello arsal") but it doesnt know who is arsal so we use input function to get the name of the user
print("helllo" + input("what is your name?"))
# now that we run the program it will ask for the name and then it will print hello arsal
# so now what we are gonna do is to treat this input function as an string because code its eventually gonna replaced by string
print("hello " + input("what is your name?") + "!")
# now we can add more string to it like this