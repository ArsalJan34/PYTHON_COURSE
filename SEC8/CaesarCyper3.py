alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def caesar(originalText, shiftamount, encode_or_decode):
    OutputText = ""

    # normalize large shifts
    shiftamount %= len(alphabet)

    # flip shift for decoding only once (fixed)
    if encode_or_decode == "decode":
        shiftamount = -shiftamount

    for letter in originalText:
        if letter not in alphabet:
            OutputText += letter
        else:
            shiftedPosition = alphabet.index(letter) + shiftamount
            shiftedPosition %= len(alphabet)
            OutputText += alphabet[shiftedPosition]

    print(f"Here is the {encode_or_decode}d result: {OutputText}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(originalText=text, shiftamount=shift, encode_or_decode=direction)

    restart = input("Type YES if you want to go again, or NO if you want to quit:\n").lower()
    if restart == "no":
        should_continue = False
        print("GoodBye Sir")
