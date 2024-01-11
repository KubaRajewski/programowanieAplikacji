import random
from collections import Counter
import re


def main():
    ########### ZADANIE 1 ##########
    print("\nZadanie 1")
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random_choices = [random.choice(original_list) for i in range(3)]
    print(random_choices)

    ########### ZADANIE 2 ##########
    print("\nZadanie 2")
    print(read_file_content("input.txt"))

    ########### ZADANIE 3 ##########
    print("\nZadanie 3")
    print(count_occurrences("input.txt", "ala"))

    ########### ZADANIE 4 ##########
    print("\nZadanie 4")
    print(combine_lists([1, 2, 3], [2, 3, 4, 5], [5, 6, 7]))

    ########### ZADANIE 5 ##########
    print("\nZadanie 5")
    print(count_unique_words('input.txt', 'output.txt'))


def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("The file does not exist.")
        return None


def count_occurrences(file_path, search_word):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()

        word_count = content.count(search_word.lower())
        return f"The word '{search_word}' occurred {word_count} time(s) in the file '{file_path}'."
    except FileNotFoundError:
        return "The file does not exist."


def combine_lists(*lists):
    combined_list = []
    for lst in lists:
        for item in lst:
            if item not in combined_list:
                combined_list.append(item)
    return combined_list


def count_unique_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)

        word_counts = Counter(words)

        with open(output_file, 'w') as file:
            for word, count in word_counts.items():
                file.write(f"{word}: {count}\n")

        return f"Word counts have been written to {output_file}"

    except FileNotFoundError:
        return "The input file does not exist."


if __name__ == '__main__':
    main()
