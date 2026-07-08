from random import randint

import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3
SEQUENCE_LENGTH = 10


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    for _ in range(ROUNDS_COUNT):
        start = randint(1, 20)
        step = randint(1, 10)
        hidden_index = randint(0, SEQUENCE_LENGTH - 1)
        numbers = []
        for index in range(SEQUENCE_LENGTH):
            numbers.append(start + index * step)
        correct_answer = str(numbers[hidden_index])
        display_numbers = []
        for index in range(SEQUENCE_LENGTH):
            if index == hidden_index:
                display_numbers.append("..")
            else:
                display_numbers.append(str(numbers[index]))
        question = " ".join(display_numbers)
        print(f"Question: {question}")
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
