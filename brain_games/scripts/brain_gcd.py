from math import gcd
from random import randint

import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for _ in range(ROUNDS_COUNT):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        correct_answer = str(gcd(num1, num2))
        print(f"Question: {num1} {num2}")
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
