import random


def main():
    gn = number_generator()
    yg = user_guess()
    un = int_convert(yg)
    resp = compare_value(un, gn)
    play_again(resp)


def number_generator():
    generated_number = random.randint(1, 1000)
    return generated_number


def user_guess():
    your_guess = input("Please guess a number between 1 and 1000: ")
    return your_guess


def int_convert(your_guess):
    done = False
    while not done:
        try:
            your_guess = int(your_guess)
            done = True
        except ValueError:
            print("You did not enter a number... Try Again!")
            main()
    return your_guess


def compare_value(your_guess, generated_number):
    i = 1
    try:
        while your_guess != generated_number and i < 10 and type(
                your_guess) == int:
            if your_guess > generated_number:
                try:
                    your_guess = int(input(
                        "{} tries left! Guess Lower: ".format(10-i)))
                except ValueError:
                    print("You did not enter a number... Try again!")
                    your_guess = int(input(
                        "{} tries left! Guess Lower: ".format(10-i)))

            else:
                your_guess = int(input(
                    "{} tries left! Guess Higher: ".format(10-i)))
            i += 1
        else:
            if your_guess == generated_number:
                print("You Win! You guessed the number in {} tries.".format(i))
            elif type(your_guess) != int:
                your_guess = int(input(
                    "Please enter a number, {} tries left!: ".format(10-i)))
            else:
                print("You Lose! My number was {}".format(generated_number))
            response = input("Do you want to play again (Y/N)? ")
            return response
    except Exception as e:
        print("Had this error: {}".format(e))
        # raise e


def play_again(response):
    while response.upper() != "Y":
        if response.upper() == "N":
            print("Thanks for playing. Good Bye!")
            break
        else:
            response = input(
                '''Sorry, I didn't understand that.
Do you want to play again(Y/N)? ''')
    else:
        main()


if __name__ == '__main__':
    main()
