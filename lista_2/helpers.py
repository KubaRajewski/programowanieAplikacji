from itertools import combinations


def get_numbers():
    numbers = []
    while True:
        value = input("Enter a number or 'end' to finish: ")
        if value == 'end':
            if not numbers:
                raise ValueError("No numbers were entered.")
            break

        try:
            number = float(value)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'end'.")

    return numbers


def get_positive_int():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("incorrect input")
    return n


def get_range():
    range_of_numbers = []
    while True:
        try:
            a = int(input("Enter the lower bound of range (a): "))
            b = int(input("Enter the upper bound of range (b): "))

            if a > b:
                raise RangeException

            break
        except ValueError:
            print("Invalid input, type in an integer")
        except RangeException:
            print("Invalid range, 'a' must be smaller or equal to 'b'")

    range_of_numbers.append(a)
    range_of_numbers.append(b)

    return range_of_numbers


def guess_game(lower_bound, upper_bound, number):
    counter = 0
    while True:
        try:
            guess = float(input("Guess a number: "))
            counter += 1

            if guess < lower_bound or guess > upper_bound:
                print("Number is not in range, try again")
            elif guess == number:
                print(f"Congratulations, you won! It took you {counter} tries.")
                break
            elif guess > number:
                print("Lower")
            elif guess < number:
                print("Higher")

        except ValueError:
            print("Enter a number")


def print_combinations(n_books, choose):
    for combination in combinations(range(1, n_books + 1), choose):
        print(' '.join(map(str, combination)))


class RangeException(Exception):
    """Range Exception"""
    pass
