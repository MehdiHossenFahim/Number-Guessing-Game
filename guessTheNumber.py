import random

while True:
    computerGuess = random.randint(1, 100)
    print("""Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have 5 chances to guess the correct number.\n
    Please select the difficulty level:
    \t1. Easy (10 chances)
    \t2. Medium (5 chances)
    \t3. Hard (3 chances)
    """)
    ##############################################################
    #---------------------- Set Difficulty ----------------------#
    ##############################################################
    while True:
        try:
            difficultyChoice = int(input("Enter your choice: "))
            if 1 <= difficultyChoice <= 3:
                break
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a number between 1 and 3.")
            continue
    if difficultyChoice == 1:
        loopRange = 10
        print("Great! You have selected the Easy difficulty Level")
    elif difficultyChoice == 2:
        loopRange = 5
        print("Great! You have selected the Medium difficulty Level")
    elif difficultyChoice == 3:
        loopRange = 3
        print("\nGreat! You have selected the Hard difficulty Level")

    print("Let's start the game!")

    ##############################################################
    # --------------------- Game Logic Control ------------------#
    ##############################################################
    for i in range(1,loopRange+1):
        guess = int(input('\nEnter your guess: '))
        if computerGuess < guess:
            print(f"Incorrect! The number is less than {guess}.")
        elif computerGuess > guess:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            break

    if computerGuess == guess:
        print("\nCongratulations! You guessed the correct number in {} attempts.".format(i))
    else:
        print("\nSorry, you didn't get it. The number was", computerGuess)
    answer = input("Do you want to play again? (y) or (n): ").lower()
    if answer != "y":
        break


