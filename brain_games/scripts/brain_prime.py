from random import randint

import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(ROUNDS_COUNT):
        number = randint(1, 100)
        correct_answer = "yes" if is_prime(number) else "no"
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
