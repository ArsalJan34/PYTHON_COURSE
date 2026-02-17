alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'enocode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

# creating a function called encrypt() that takes originalText and shiftAmount as 2 inputs
# Inside the encrypt() function shift each letter of the orginalText forwards in the alphabet
# by shift amount and print the encrypt text.
def encrypt(orignalText, shiftAmount):
  cipherText = ""
  for letter in orignalText:
    shiftedPosition = alphabet.index(letter) + shiftAmount
    # here we assigned old shiftedPosition to modulo of alphabet length
    shiftedPosition = shiftedPosition % len(alphabet)
    cipherText += alphabet[shiftedPosition]
  print(f"Here is the encoded result: {cipherText}")

encrypt(orignalText=text, shiftAmount=shift)
