def main():
    ########### ZADANIE 1 ##########
    print("\nZadanie 1")
    while True:
        n = input("How many numbers would you like to input? ")
        if n.isnumeric():
            if int(n) > 0:
                break
        else:
            print("Try again")

    numbers = []
    for i in range(0, int(n)):
        numbers.append(int(input("number: ")))

    print(f"list: {numbers}")

    ########### ZADANIE 2 ##########
    print("\nZadanie 2")
    print(f"sum: {sum(numbers)}")

    ########## ZADANIE 3 ##########
    print("\nZadanie 3")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")

    ########### ZADANIE 4 ##########
    print("\nZadanie 4")
    wanted_sum = int(input("What sum are you looking for? "))
    for pair in find_pairs(numbers, wanted_sum):
        print(f"{pair[0]} + {pair[1]} = {pair[0] + pair[1]}")

    ########### ZADANIE 5 ##########
    print("\nZadanie 5")
    fields_of_study = {
        'Computer Science': 'Faculty of Computer Science and Management',
        'Civil Engineering': 'Faculty of Civil Engineering',
        'Biotechnology': 'Faculty of Chemistry',
        'Electronics': 'Faculty of Electronics',
        'Mechanical Engineering': 'Faculty of Mechanical Engineering'
    }
    fields_of_study.get('Computer Science', "You cannot study this field at the Wrocław University of Science and "
                                            "Technology.")

    ########## ZADANIE 6 ##########
    print("\nZadanie 6")
    count_characters("Example sentence to test")


def find_pairs(nums, target_sum):
    pairs = []
    seen = set()

    for num in nums:
        complement = target_sum - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs


def count_characters(sentence):
    sentence = sentence.lower().replace(' ', '')
    char_count = {}

    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


main()
