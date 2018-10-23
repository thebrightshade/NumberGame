import random
import logging

logger = logging.getLogger(__name__)


def main():
    gn = number_generator()
    # print(gn)
    un = user_guess()
    compare_value(un, gn)


def number_generator():
    generated_number = random.randint(1, 1000)
    return generated_number


def user_guess():
    try:
        your_guess = int(input("Please guess a number between 1 and 1000: "))
        return your_guess
    except Exception as error:
        logger.error(error)
        raise


def compare_value(your_guess, generated_number):
    i = 1
    while your_guess != generated_number and i < 10:
        if your_guess > generated_number:
            try:
                your_guess = int(
                    input("{} tries left! Guess Lower: ".format(10-i)))
            except Exception as error:
                logger.error(error)
                raise
        else:
            try:
                your_guess = int(
                    input("{} tries left! Guess Higher: ".format(10-i)))
            except Exception as error:
                logger.error(error)
                raise

        i += 1
    else:
        if your_guess == generated_number:
            print("You Win! You guessed the number in {} tries.".format(i))
        else:
            print("You Lose! My number was {}".format(generated_number))


if __name__ == '__main__':
    main()
