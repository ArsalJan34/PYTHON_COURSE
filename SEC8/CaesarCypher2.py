alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

# creating a function called encrypt() that takes originalText and shiftAmount as 2 inputs
# Inside the encrypt() function shift each letter of the orginalText forwards in the alphabet
# by shift amount and print the encrypt text.
# def encrypt(originalText, shiftAmount):
#   cipherText = ""
#   for letter in originalText:
#     shiftedPosition = alphabet.index(letter) + shiftAmount
#     # here we assigned old shiftedPosition to modulo of alphabet length
#     shiftedPosition = shiftedPosition % len(alphabet)
#     cipherText += alphabet[shiftedPosition]
#   print(f"Here is the encoded result: {cipherText}")
# encrypt(originalText=text, shiftAmount=shift)

# def decrypt(originalText, shiftAmount):
#   cipherText2 = ""
#   for letter in originalText:
#     shiftedPosition = alphabet.index(letter) - shiftAmount
#     shiftedPosition % len(alphabet)
#     cipherText2 += alphabet[shiftedPosition]

#   print(f"Here is the encoded result: {cipherText2}")
# decrypt(originalText=text, shiftAmount=shift)


def caesar(originalText, shiftamount, encode_or_decode):
  cipherText2 = ""
  for letter in originalText:

    if encode_or_decode == "decode":
        shiftamount *= -1
    if encode_or_decode == "encode":
        shiftamount *= 1
    shiftedPosition = alphabet.index(letter) - shiftamount
    shiftedPosition % len(alphabet)
    cipherText2 += alphabet[shiftedPosition]

  print(f"Here is the {encode_or_decode}d result: {cipherText2}")
# decrypt(originalText=text, shiftAmount=shift)
caesar(originalText=text, shiftamount=shift, encode_or_decode=direction)
