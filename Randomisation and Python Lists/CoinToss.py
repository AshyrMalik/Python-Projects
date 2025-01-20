import random

choice = int(input("Press 1 for Heads or 0 for tails: "))
toss = random.randint(0,1)

if toss == 1 and choice==1:
    print("Its Heads and you have won the toss")
elif toss == 0 and choice==0:
    print("Its Tails and you have won the toss")
elif toss == 1 and choice==0:
    print("Its Heads and you have lost the toss")
elif toss == 0 and choice==1 :
    print("Its Tails and you have lost the toss")
