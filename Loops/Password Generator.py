import random
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/', '|', '\\', '~', '`']
numbers_as_strings = [str(i) for i in range(10)]
alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

length= int(input("How long would you like your password to be: "))
numbers=int(input("How many numbers would you like: "))
sym=int(input("How many symbols would you like: "))

password = ""
for i in range(sym):
    password += random.choice(symbols)  # Use random.choice() for simplicity

for i in range(numbers):
    password += random.choice(numbers_as_strings)

for i in range(length-numbers-sym+1):
    password= password + alphabets[random.randint(0,len(alphabets))]

password_list = list(password)
password= ''.join(random.shuffle(password_list))
print("Youre password is : ", password)
