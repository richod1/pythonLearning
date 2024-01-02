import random


def guess_game():
    print("Welcome to the guessing game!!")

    lower_bounds=1
    uper_bonds=100
    secret_number=random.randint(lower_bounds,uper_bonds)

    attemps=0

    while True:
        guess=int(input(f"Guess the number between {lower_bounds} and {uper_bonds} :"))
        attemps+=1
        if guess < secret_number:
            print("Too low! Try again")
        elif guess > secret_number:
            print("Too high! Try again")
        else:
            print(f"Congratulation you guess the number! :{secret_number} in {attemps} attemps ")
        break
if __name__=="__main__":
    guess_game()