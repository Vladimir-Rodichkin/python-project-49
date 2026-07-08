from random import choice, randint

import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3
OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
}


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    for _ in range(ROUNDS_COUNT):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operator = choice(list(OPERATIONS.keys()))
        correct_answer = str(OPERATIONS[operator](num1, num2))
        print(f"Question: {num1} {operator} {num2}")
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
