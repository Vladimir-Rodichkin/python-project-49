from random import randint

import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(ROUNDS_COUNT):
        num = randint(1, 100)
        print("Question:", num)
        answer = prompt.string("Your answer: ")
        correct_answer = "yes" if num % 2 == 0 else "no"
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
