import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]
wordsList = ["Steve", "Tony", "Thor"]
lives = 6
chosenWord = random.choice(wordsList)
print(chosenWord)
placeholder = ""
wordLength = len(chosenWord)
for position in range(wordLength):
  placeholder +="_"
print(placeholder)
gameOver = False
correctLetters = []
while not gameOver:
  guess = input("Guess a letter").lower()
  display = ""
  for letter in chosenWord:
    if letter == guess:
      display +=letter
      correctLetters.append(guess)
    elif letter in correctLetters:
      display +=letter
    else:
      display+="_"
  print(display)
  if guess not in chosenWord:
    lives -= 1
    if lives == 0:
      gameOver = True
      print("you win")

  if "_" not in display:
    gameOver = True
    print("You won")

print(stages[lives])
