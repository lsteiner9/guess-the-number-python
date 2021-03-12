from random import randint


def main():
    playing = True
    while playing:
        rand = randint(0, 100)
        userNum = -1
        print("Guess a number between 0 and 100, inclusive:")
        while rand != userNum:
            userNum = int(input(""))
            if userNum < rand:
                print("Too low! Guess again:")
            elif userNum > rand:
                print("Too high! Guess again:")
            else:
                print("You got it! Congrats!")
                playAgain = input("Do you want to play again? (y/n) ")
                if playAgain != "y" and playAgain != "Y":
                    playing = False
                    print("Thanks for playing.")


if __name__ == '__main__':
    main()
