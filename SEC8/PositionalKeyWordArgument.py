#funtions with more than 1 input
def greet_with(name, location):
  print(f"hello {name}")
  print(f"what is it like in {location}")

greet_with("arsal", "new york")
# or
# greet_with(name:"arsal", location:"new york")

# KEY Arguments
def my_function(a,b,c):
  print(f"a={a}")
  print(f"b={b}")
  print(f"c={c}")

my_function(a=1,b=2,c=3)
my_function(1,2,3)
