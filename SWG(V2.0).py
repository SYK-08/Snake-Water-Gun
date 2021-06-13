import random

print("\nWelcome to the Snake water gun game!\n")

lst = ["s", "w", "g"]

def run_again():
    inp1 = input("Do you want to play again?(y/n):\nType here:")
    if inp1 == "n":
        print("Oh, okay see ya.")
        exit()
    elif inp1 == "y":
        run()
    else:
        print("\n--------Invalid Input--------\n")
        run_again()

def run():
    attempts = 1
    player = 0
    comp = 0
    while (attempts <= 10):
        rand = random.choice(lst)
        inp = input("\nChoose one from below:\n1.Snake(s)\n2.Water(w)\n3.Gun(g)\n\nType Here:")
        inp = inp.lower()

        attempts += 1

        if inp == "s" and rand == "s":
            print(f"Tie.\nYou choosed Snake and Computer also choosed Snake.\n----------><----------")
        elif inp == "w" and rand == "w":
            print(f"Tie.\nYou choosed Water and Computer also choosed Water.\n----------><----------")
        elif inp == "g" and rand == "g":
            print(f"Tie.\nYou choosed Gun and Computer also choosed Gun.\n----------><----------")
        
        elif inp == "s" and rand == "w":
            player += 1
            print("You Won!\nYou chosed Snake and Computer chosed Water.\nSo Snake drank the water.\n/You got 1 point\\.\n----------><----------")
        elif inp == "s" and rand == "g":
            comp += 1
            print("You lost.\nYou chosed Snake whereas Computer chosed Gun.\nThe gun shot the snake to death.\n/Computer got 1 point\\.\n----------><----------")
        elif inp == "w" and rand == "s":
            comp += 1
            print("You lost.\nYou chosed Water whereas Computer chosed Snake.\nThe Snake drank the water.\n/Computer got 1 point\\.\n----------><----------")
        elif inp == "w" and rand == "g":
            player += 1
            print("You Won!\nYou chosed Water whereas Computer chosed gun.\nSo, the Gun was drowned in water.\n/You got 1 point\\.\n----------><----------")
        elif inp == "g" and rand == "s":
            player += 1
            print("You Won!\nYou chosed Gun whereas Computer chosed Snake.\nSo, the Gun shot the snake to death\n/You got 1 point\\.\n----------><----------")
        elif inp == "g" and rand == "w":
            comp += 1
            print("You lost.\nYou chosed Gun whereas Computer chosed Water.\nTSo, the Gun was drowned in Water.\n//Computer got 1 point")
        else:
            print("\n-----Invalid input-----\n")
            continue
        
        print(f"Number of attempts left: {11 - attempts}")

        if attempts > 10:
            print("Game Over.\n\n--------FINAL RESULTS--------\n\n")
            if comp > player:
                print(f"You lost.\n--------------------\nYour score: {player}\nComputer's score: {comp}\n--------------------")
            elif comp < player:
                print(f"Hurray! You won.\n--------------------\nYour score: {player}\nComputer's score: {comp}\n--------------------")
            else:
                print(f"It's a tie.\n--------------------\nYour score: {player}\nComputer's score: {comp}\n--------------------")

            while attempts > 10:
                run_again()

run()
run_again()
