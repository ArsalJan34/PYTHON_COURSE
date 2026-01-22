import random

worldList = ["jon", "robb", "eddard"]

chosen_word = random.choice(worldList)
print(chosen_word)
placeholder = ""
wordLength = len(chosen_word)
for position in range(wordLength):
  placeholder+="_"
print(placeholder)

gameOver = False
correctLetters = []

while not gameOver:
  guess = input("Guess a letter: ").lower()

  display = ""

  for letter in chosen_word:
    if letter == guess:
     display += letter
     correctLetters.append(letter)
    elif letter in correctLetters:
     display += letter

    else:
     display += "_"
  print(display)
  if "_" not in display:
    gameOver = True
    print("You win")

