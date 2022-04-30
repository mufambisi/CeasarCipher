alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    temp_text=""
    # global temp_text
    for shift_letter in text:
        temp_text += chr(ord(shift_letter)+shift)
    print(f"Cipher text = {temp_text}")


def decrypt (text, shift):
    temp_text=""
    # global temp_text
    for shift_letter in text:
        temp_text += chr(ord(shift_letter)-shift)
    print(f"Decrypted text = {temp_text}")

if direction.lower() == 'encode':
    encrypt(text, shift)
elif direction.lower() == 'decode':
    decrypt(text,shift)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
