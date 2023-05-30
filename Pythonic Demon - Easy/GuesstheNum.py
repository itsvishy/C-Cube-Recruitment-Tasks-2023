# Guess the Number game

import random


def guessnum():
    nm = input("Enter name: ")
    lol = int(input("Lower limit: "))
    upl = int(input("Upper limit: "))
    rnds = int(input("No of rounds: "))

    t_pnts = 100  # Total points
    rnd_num = 1
    if upl > lol and rnds > 0:
        print(f"\nWelcome to the game, {nm}! Let's start.")

        numb = random.randint(lol, upl)

        while (rnd_num <= rnds):
            print(f"\nRound {rnd_num}\nCurrent Points: {t_pnts} ")

            while True:
                try:
                    g = int(input("Enter guess: "))
                    break
                except ValueError:
                    print("Invalid input.")

            if (rnd_num < rnds):
                if (g == numb):
                    print("You guessed it right!")
                    break
                elif (g < numb):
                    print("Too Low. Try again.")
                elif (g > numb):
                    print("Too High. Try again.")
                else:
                    print("Input error.")
            elif (rnd_num == rnds):
                if (g == numb):
                    print("You guessed it right!")
                    break
                elif (g < numb):
                    print("Better luck nxt time.")
                elif (g > numb):
                    print("Better luck nxt time.")
                else:
                    print("Input error.")

            t_pnts -= 5
            rnd_num += 1
            if t_pnts <= 0:
                print("Oops! Game Over! You ran out of points! Better luck next time.")
                break

    else:
        print("\nInvalid input.")

    print("\nThanks for playing.")
    print(f"Total points: {t_pnts}")


while True:
    guessnum()
    ch = input("\nStart another game?(Y/N): ")
    if ch in "Nn":
        break
