import random


def main():
    gn = number_generator()
    # print(gn)
    un = user_guess()
    compare_value(un, gn)


def number_generator():
    generated_number = random.randint(1, 1000)
    return generated_number


def user_guess():
    your_guess = int(input("Please guess a number: "))
    return your_guess


def compare_value(your_guess, generated_number):
    i = 1
    while your_guess != generated_number and i < 10:
        if your_guess > generated_number:
            print("Guess Lower, {} tries left!".format(10-i))
        else:
            print("Guess Higher, {} tries left!".format(10-i))
        i += 1
        your_guess = user_guess()
    else:
        if your_guess == generated_number:
            print("You Win! You guessed the number in {} tries.".format(i))
        else:
            print("You Lose!")


if __name__ == '__main__':
    main()
