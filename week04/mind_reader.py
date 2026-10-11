import random
import time

def play_game():
    print("\n" + "=" * 35)
    print("       MIND READER")
    print("   The Number Challenge")
    print("=" * 35)

    print("\nI am thinking of a number between 1 and 100.")
    print("You have 7 attempts to find it!")
    print("Let's see if you can read my mind...\n")

    secret_number = random.randint(1, 100)
    attempts = 7
    score = 100

    start_time = time.time()

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue

            if guess == secret_number:
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)

                print("\nAMAZING! You read my mind!")
                print("The secret number was", secret_number)
                print("Your score:", score)
                print("Time:", elapsed_time, "seconds")
                break

            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            attempts -= 1
            score -= 10

            print("Attempts left:", attempts)
            print("Current score:", max(score, 0))
            print()

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    else:
        print("\nGAME OVER!")
        print("The secret number was", secret_number)
        print("Better luck next time!")

    print("\nThanks for playing Mind Reader!")

play_game()
