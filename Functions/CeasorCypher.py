
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text,shift):
    encrypted_text=[]
    for letter in text:
        position=alphabets.index(letter)
        new_position=shift+position
        encrypted_text.append(alphabets[new_position])

    return "".join(encrypted_text)

direction=input("Type encode to encrypt the message \n"
      "Type decode to decrypt the message").lower()

print("Type youre message: ")
shift=int(input("Enter the number which you want to shift: "))