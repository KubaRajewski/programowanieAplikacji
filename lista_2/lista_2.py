import random
from itertools import combinations

from helpers import *


def main():
    ########### ZADANIE 1 ##########
    print("\nZadanie 1")
    numbers = get_numbers()
    print(f"The average is {sum(numbers) / len(numbers)}.")


    # ########## ZADANIE 2 ##########
    print("\nZadanie 2")

    for i in range(0, get_positive_int()):
        print(i)

    # ########## ZADANIE 3 ##########
    # print("\nZadanie 3")
    #
    # range_of_numbers = get_range()
    # for i in range(range_of_numbers[0], range_of_numbers[1]):
    #     print(i)
    #
    # ########## ZADANIE 4 ##########
    # print("\nZadanie 4")
    #
    # while True:
    #     try:
    #         a = float(input("Enter a number: "))
    #         break
    #     except ValueError:
    #         print("Invalid input")
    #
    # for i in range(50, 101):
    #     if i % a == 0:
    #         print(i)
    #
    # ########## ZADANIE 5 ##########
    print("\nZadanie 5")

    game_range = get_range()
    lower_bound = game_range[0]
    upper_bound = game_range[1]
    guess_game(lower_bound, upper_bound, random.randint(lower_bound, upper_bound))
    #
    # ########## ZADANIE 6 ##########
    # print("\nZadanie 6")
    #
    # print("Enter the size of the square")
    # size = get_positive_int()
    # for i in range(size):
    #     print('*' * size)
    #
    # ########## ZADANIE 7 ##########
    # print("\nZadanie 7")
    #
    # print("Enter the number of books")
    # n_books = get_positive_int()
    # print("How many are we choosing?")
    # choose = get_positive_int()
    #
    # for combination in combinations(range(1, n_books + 1), choose):
    #     print(' '.join(map(str, combination)))


if __name__ == '__main__':
    main()
