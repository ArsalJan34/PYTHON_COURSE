# Todo1 - Randomly choose a word from the world_list and assign it to a variable
# chosen_word then print it
# TODO3 - Ask user to guess letter and assign their answer to a variable called guess make the guess lowercase
# TODO3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word print "right" if it is wrong if its not
# world_list = ["steve", "tony", "thor"]
# chose_world = "steve"
# print(chose_world)
# guess = input("Enter an letter").lower()
# for words in chose_world:
#   print(words[0])
# letters = words[0]
# if guess == letters:
#   print("Right")
# else:
#   print("wrong")
# List of words
word_list = ["steve", "tony", "thor"]

# Choose a word (fixed for now)
chosen_word = "steve"
print(chosen_word)  # testing

# Ask user for ONE letter
guess = input("Enter a letter: ").lower()

# Check if letter is in the word
if guess in chosen_word:
    print("Right")

else:
    print("Wrong")

