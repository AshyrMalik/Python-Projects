import random

word_list = ["ashar","malik","khan"]
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
lives = 6

for i in chosen_word:
    user_guess = input("Guess a letter: ").lower()

    if i==user_guess:
        list_of_lines[count]=user_guess
        print(list_of_lines)
        count+=1
    else:
        lives-=1
        count+=1


if count==len(chosen_word):
    print("You have won")

