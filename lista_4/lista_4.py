import math

from sympy import primerange


def main():
    ########### ZADANIE 1 ##########
    print("\nZadanie 1")
    print(kelvin_to_celsius(0))

    ########### ZADANIE 2 ##########
    print("\nZadanie 2")
    print(is_perfect_number(7))

    ########### ZADANIE 3 ##########
    print("\nZadanie 3")
    prime_numbers = [x for x in range(1, 101) if x in set(primerange(2, x + 1))]
    print(prime_numbers)

    ########### ZADANIE 4 ##########
    print("\nZadanie 4")
    print(factorial(5))
    print(factorial(int(input("number: "))))

    ########### ZADANIE 5 ##########
    print("\nZadanie 5")
    wielomian_1 = [-2, 3, 0, 4]
    wielomian_2 = [1, 5, 2]

    print("addition: ", add_polynomials(wielomian_1, wielomian_2))
    print("subtraction", subtract_polynomials(wielomian_1, wielomian_2))
    print("multiplication", multiply_polynomials(wielomian_1, wielomian_2))

    ########### ZADANIE 6 ##########
    print("\nZadanie 6")
    data = [120, 150, 130, 170, 140]

    print("Without built-in functions:")
    print("Mean:", mean(data))
    print("Max Value:", max_value(data))
    print("Min Value:", min_value(data))
    print("Standard Deviation:", std_dev(data))

    print("\nWith built-in functions:")
    print("Mean:", built_in_mean(data))
    print("Max Value:", built_in_max_value(data))
    print("Min Value:", built_in_min_value(data))
    print("Standard Deviation:", built_in_std_dev(data))


def kelvin_to_celsius(kelvin):
    return None if kelvin < 0 else kelvin - 273.15


def is_perfect_number(number):
    if number <= 1:
        return False

    divisors_sum = sum([i for i in range(1, number) if number % i == 0])

    return divisors_sum == number


def factorial(x):
    if x in (0, 1):
        return 1
    return x * factorial(x - 1)


def add_polynomials(p1, p2):
    if len(p1) > len(p2):
        p2.extend([0] * (len(p1) - len(p2)))
    else:
        p1.extend([0] * (len(p2) - len(p1)))
    return [a + b for a, b in zip(p1, p2)]


def subtract_polynomials(p1, p2):
    if len(p1) > len(p2):
        p2.extend([0] * (len(p1) - len(p2)))
    else:
        p1.extend([0] * (len(p2) - len(p1)))
    return [a - b for a, b in zip(p1, p2)]


def multiply_polynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result


def mean(values):
    return sum(values) / len(values)


def max_value(values):
    max_val = values[0]
    for val in values:
        if val > max_val:
            max_val = val
    return max_val


def min_value(values):
    min_val = values[0]
    for val in values:
        if val < min_val:
            min_val = val
    return min_val


def std_dev(values):
    variance = sum((x - mean(values)) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


def built_in_mean(values):
    return sum(values) / len(values)


def built_in_max_value(values):
    return max(values)


def built_in_min_value(values):
    return min(values)


def built_in_std_dev(values):
    avg = built_in_mean(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


if __name__ == '__main__':
    main()
