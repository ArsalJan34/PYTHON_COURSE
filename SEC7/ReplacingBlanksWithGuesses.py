import random

worldList = ["Jon", "Robb", "Eddard"]

chosen_word = random.choice(worldList)
print(chosen_word)
placeholder = ""
wordLength = len(chosen_word)
for position in range(wordLength):
  placeholder+="*"
print(placeholder)
guess = input("Guess a letter: ").lower()
display = ""
for letter in chosen_word:
  if letter == guess:
    display += letter
  else:
    display += "_"
print(display)
