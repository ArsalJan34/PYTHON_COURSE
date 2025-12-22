len("Hello")

name = "hello"
print(len(name))
# this is how we check something that if its string or its another
# datatype
print(type("Hello"))

print(type(123))
print(type(0.2))
print(type(True))

# print("Number of letter in your name :")
# name = (input("Enter your name: "))
# print(len(name))

name = (input("Enter your name here : "))
Length = len(name)
# print("The length of your name is : " + Length)
# so the above code will give us error that can only concatenate str not int to str
# lets check what data types are these
print(type(name))
print(type(Length))
# so here it will print name as string and Length as the int
