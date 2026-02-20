alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





def caesar(originalText, shiftamount, encode_or_decode):
  OutputText = ""
  for letter in originalText:
    if letter not in alphabet:
       OutputText +=letter
    else:
        if encode_or_decode == "decode":
            shiftamount *= -1
        if encode_or_decode == "encode":
            shiftamount *= 1
        shiftedPosition = alphabet.index(letter) - shiftamount
        shiftedPosition % len(alphabet)
        OutputText += alphabet[shiftedPosition]

  print(f"Here is the {encode_or_decode}d result: {OutputText}")
# decrypt(originalText=text, shiftAmount=shift)
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(originalText=text, shiftamount=shift, encode_or_decode=direction)
restart = input("Type YES if you want to go again, Or Type NO if you want to quit").lower()
if restart == "no":
   should_continue = False
else:
   print("GoodBye Sir")


