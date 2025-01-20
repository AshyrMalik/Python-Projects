import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock,paper,scissors]

user_picked= int(input("Press 0 for Rock \n"
              "Press 1 for paper \n"
              "press 2 for scissors\n"
              "Enter you're choice: "))
print("You Chose:\n",choices[user_picked])
random_picked = random.randint(0,2)
print("Computer Chose:\n",choices[random_picked])


if random_picked==user_picked:
    print("Its a tie ")
elif (user_picked==0 and random_picked==1) or(user_picked==1 and random_picked==2) or(user_picked==2 and random_picked==0):
    print("You lost")
else:
    print("You won")


