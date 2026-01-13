import random
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = [
    '1','2','3','4','5','6','7','8','9'
]
symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '_','+','-'
]
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("how many letter would you like?\n"))
nr_symbols = int(input(f"How many symbols\n"))
nr_numbers = int(input(f"How many numbers?\n"))

# password = ""
# # nr_letter = 4
# for char in range(0,nr_letters +1):
# #1 -4 range
#  password += random.choice(letters)

# for char in range(0, nr_numbers +1):
#  password += random.choice(numbers)

# for char in range(0, nr_symbols +1):
#  password += random.choice(symbols)
# print(password)
password_list = []
for char in range(0, nr_letters):
  password_list.append(random.choice(letters))
for char in range(0, nr_numbers):
  password_list.append(random.choice(numbers))
for char in range(0, nr_symbols):
  password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
# now we will convert it into an string using for loop
# creating an empty variable called password here
password = ""
for char in password_list:
  password += char
  print(f"Your password is : {password}")
