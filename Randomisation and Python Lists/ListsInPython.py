import random
states_of_pakistan = [
    "Punjab",
    "Sindh",
    "Khyber Pakhtunkhwa",
    "Balochistan",
    "Islamabad Capital Territory",
    "Gilgit-Baltistan",
    "Azad Jammu and Kashmir"
]

print(states_of_pakistan)

states_of_pakistan[3]= "Balochi"
print(states_of_pakistan)

states_of_pakistan.append("India")
print(states_of_pakistan)


picker = random.randint(0,len(states_of_pakistan)-1)

print("the one who is picked is: ", {states_of_pakistan[picker]})
