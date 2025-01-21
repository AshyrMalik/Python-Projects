
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v','w', 'x', 'y', 'z']

def encrypt(text,shift):
    encrypted_text=[]
    for letter in text:
        position=alphabets.index(letter)
        new_position=shift+position
        encrypted_text.append(alphabets[new_position])

    return "".join(encrypted_text)

def decrypt(text,shift):
    decrypted_text=""
    for letters in text:
        position=alphabets.index(letters)
        new_position = position - shift
        decrypted_text+=(alphabets[new_position])
    return decrypted_text

while(True):
    direction = input("Type encode to encrypt the message \n"
                      "Type decode to decrypt the message\n"
                      "Type anything else to exit\n"
                      "Enter your choice: ").lower()

msg=(input("Type your message: "))
shift=int(input("Enter the number which you want to shift: "))

    if direction=="encode":
        encrypt(msg,shift)
    elif direction=="decode":
        decrypt(msg,shift)
    else:
        print("Closing Application")
        break