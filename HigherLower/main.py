from DataandArt import  logo,vs,data
import random

def HigherLower():
    a = random.choice(data)
    b = random.choice(data)

    while b == a:  # Ensure `b` is different from `a`
        b = random.choice(data)

    print(logo)
    score = 0
    while True:
        # Display the comparison
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")

        # Take user input
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Determine if the user's choice is correct
        if (choice == "a" and a['follower_count'] > b['follower_count']) or (
                choice == "b" and b['follower_count'] > a['follower_count']):
            score += 1
            print(f"You guessed correctly! Current Score: {score}")

            # Shift `b` to `a` and select a new `b`
            a = b if a['follower_count'] > b['follower_count'] else a
            b = random.choice(data)
            while b == a:  # Avoid duplicates
                b = random.choice(data)
        else:
            # User guessed wrong, end the game
            print(f"You guessed wrong. Total Score: {score}")
            break



if __name__ == '__main__':
    HigherLower()