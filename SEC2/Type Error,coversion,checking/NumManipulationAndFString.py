# previously we created bmi but it printed values in float now we will try
# to covert it into int and round the decimal value
bmi = 54 / 1.78 ** 2
print(bmi)
print(int(bmi))
# using int to convert is called as flooring in python
print(round(bmi))
# we can use round and add an ndigit to let it know how many digits we want after decimal
print(round(bmi, 3))
# It will give us 3 digits after the decimal point

# Assignment operators in python

score = 0
# when user scores
score += 1
print(score)
score += 1
print(score)
# f-string
# when we print string it will give us error
# print("your score is : " + score)
print(f"your score is : {score}")
# Now this will give the right value output without causing any error
