alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plaintext, shift_number):
    cipher = ""
    for n in plaintext:
        new_position = alphabet.index(n) + shift_number
        if new_position > 25:
            new_position -= 26
        cipher += alphabet[new_position]
    print (f"Your ciphertext is {cipher}")

def decrypt(plaintext, shift_number):
    cipher = ""
    for n in plaintext:
        new_position = alphabet.index(n) - shift_number
        if new_position < 0:
            new_position += 26
        cipher += alphabet[new_position]
    print (f"Your plaintext is {cipher}")

if direction.lower() == "encode":
    encrypt(text, shift)
elif direction.lower() == "decode":
    decrypt(text,shift)
else:
    print("Incorrect instructions my g")

