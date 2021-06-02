import random
print("Welcome to the Snake water gun game!")
chance = 1
counter = 10
player_p = 0
comp_p = 0
choices = ["Snake", "Water", "Gun"]
def run():
    global choices
    global chance
    global player_p
    global comp_p
    global counter
    while chance > 0 and chance <= 10:
        a = random.choice(choices)
        counter -= 1
        print("Choose one from below:\n1.Snake(s)\n2.Water(w)\n3.Gun(g)")
        decision = input("Type here:")
        if decision == "s" and a == "Snake":
            chance += 1
            print(f"Draw. {counter} times left.")
        elif decision == 's' and a == "Water":
            chance += 1
            print(f"You Won! {counter} times left.\n-------------------------------")
            player_p += 1
        elif decision == "s" and a == "Gun":
            chance += 1
            print(f"You lost. {counter} times left.\n-------------------------------")
            comp_p += 1
        elif decision == "w" and a == 'Snake':
            chance += 1
            print(f"You lost. {counter} times left.\n-------------------------------")
            comp_p += 1
        elif decision == "w" and a == "Water":
            chance += 1
            print(f"Draw. {counter} times left.\n-------------------------------")
        elif decision == "w" and a == "Gun":
            chance += 1
            print(f"You Won! {counter} times left.\n-------------------------------")
            player_p += 1
        elif decision == "g" and a == "Snake":
            chance += 1
            print(f"You Won! {counter} times left.\n-------------------------------")
            player_p += 1
        elif decision == "g" and a == "Water":
            chance += 1
            print(f"You lost. {counter} times left.\n-------------------------------")
            comp_p += 1
        elif decision == "g" and a == "Gun":
            chance += 1
            print(f"Draw. {counter} times left.\n-------------------------------")
        
run()

print("Your score:", player_p)
print("Computer's score:", comp_p)

def winner():
    if player_p > comp_p:
        print("------------------------\nYou Won! Congratulations")
    elif player_p < comp_p:
        print("------------------------\nComputer Won! Better luck next time.")
    else:
        print("---------------\nIt's a DRAW!")

winner()
