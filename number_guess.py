import random

top_of_range = int(input("Type a number: "))

if top_of_range <= 0:
    print("Please type a number larger than 0 next time.")
    quit()

random_number = random.randint(0, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess ,type 'exit' to quit the game : ")
    if user_guess.lower() == "exit":
        print("You exited the game.")
        break

    user_guess = int(user_guess)

    if user_guess == random_number:
        print("You got it right!")
        break
    else:
        print("You got it wrong! Better luck next time!")

print(f"You got it in {guess} guesses!")
