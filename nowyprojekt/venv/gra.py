import random
import time

def win():
    print("wygrales!")

def loose():
    print("przegrales!")

random.seed(time.time())

gra = ["kamien", "papier", "nozyce"]

user = "start"

while user != "x":
    user = input("kamien, papier czy nozyce? (x konczy gre) ")

    if user == "x":
        print("KONIEC GRY:)")
        continue

    if user != "kamien" and user != "papier" and user != "nozyce":
        print("error! cos zle wpisales")
        continue

    computer = random.choice(gra)
    print(computer)

    if user == computer:
        print("remis!")

    if user == "kamien":
        if computer == "papier":
            loose()
        elif computer == "nozyce":
            win()

    if user == "papier":
        if computer == "kamien":
            win()
        elif computer == "nozyce":
            loose()

    if user == "nozyce":
        if computer == "kamien":
            loose()
        elif computer == "papier":
            win()