import random

print("""
  _                                            
 | |                                           
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                     
                    |___/                      
""")


word_list = ["python", "programming", "hangman", "developer", "computer",
    "keyboard", "algorithm", "function", "variable", "syntax",
    "loop", "condition", "integer", "boolean", "string",
    "dictionary", "list", "tuple", "lambda", "exception",
    "binary", "decimal", "hexadecimal", "recursive", "iteration",
    "debugging", "compiler", "interpreter", "module", "package",
    "virtual", "machine", "framework", "backend", "frontend",
    "server", "database", "network", "protocol", "software",
    "hardware", "pythonic", "array", "control", "structure",
    "syntaxerror", "runtime", "bitwise", "hashing", "sorting"]
hangman_stages = [
    """
      ------
      |    |
           |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\   |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\   |
     /     |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\   |
     / \   |
           |
    =========
    """

]



chosen_word = random.choice(word_list)
print(chosen_word)

list_of_lines =[]
for i in range(len(chosen_word)):
    list_of_lines.append("_")

count=0
print(list_of_lines)
lives = 0
while True:
    print(hangman_stages[lives])
    user_guess = input("Guess a letter: ").lower()

    found= False
    n=0
    for i in chosen_word:
        if i==user_guess:
            list_of_lines[n]=user_guess
            print("right guess")
            print(list_of_lines)
            count+=1
            found=True

        n+=1
    if not found:
        print("wrong guess")
        print(list_of_lines)
        lives+=1

    if count == len(chosen_word):
        print("You have won")
        break
    if lives==6:
        print("You have lost")
        print(hangman_stages[lives])
        break



