from datetime import datetime
import math


def main():
    ########### ZADANIE 1 ##########
    print("\nZadanie 1")
    say_hello()

    ########## ZADANIE 2 ##########
    print("\nZadanie 2")
    while True:
        try:
            a = float(input("Enter the first number (a): "))
            b = float(input("Enter the second number (b): "))
            break
        except ValueError:
            print("type in a number")

    print_calculations(a, b)

    ########## ZADANIE 3 ##########
    print("\nZadanie 3")
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius > 0:
                break
            else:
                print("Radius has to be positive")
        except ValueError:
            print("enter a number")

    print(calculate_circle(radius))

    ########## ZADANIE 4 ##########
    print("\nZadanie 4")
    while True:
        try:
            a = float(input("Enter the first number (a): "))
            b = float(input("Enter the second number (b): "))
            break
        except ValueError:
            print("Enter a number")

    comperator = compare_numbers(a, b)
    if comperator == 1:
        print(f"The number {a} is greater than {b}.")
    elif comperator == -1:
        print(f"The number {b} is greater than {a}.")
    else:
        print("The numbers are equal.")

    ########## ZADANIE 5 ##########
    print("\nZadanie 5")
    say_hello_to_adults()

    ########## ZADANIE 6 ##########
    print("\nZadanie 6")
    while True:
        try:
            a = float(input("Enter a number: "))
            break
        except ValueError:
            print("Type in a number")

    print("The number is even" if check_if_even(a) else "The number is odd")

    ########## ZADANIE 7 ##########
    print("\nZadanie 7")
    while True:
        try:
            a = float(input("Enter the first length: "))
            b = float(input("Enter the second length: "))
            c = float(input("Enter the third length: "))
            break
        except ValueError:
            print("Start again, type in a number")

    print("Yes, the lengths can form a triangle." if can_form_triangle(a, b, c) else "No, the lengths cannot form a "
                                                                                     "triangle.")
    ########## ZADANIE 8 ##########
    print("\nZadanie 8")
    while True:
        try:
            score = int(input("Enter the score (0-100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("type in a number")

    while True:
        try:
            output_format = input("Enter the output format (numerical || verbal || both): ")
            if output_format in ['numerical', 'verbal', 'both']:
                break
            else:
                print("Invalid output format. Please enter 'numerical', 'verbal', or 'both'.")
        except ValueError:
            print("Type in a number")

    print(grade_student(score, output_format))

def say_hello():
    while True:
        try:
            name = input("Enter your name: ")
            birthYear = int(input("Enter your year of birth: "))
            break
        except ValueError:
            print("Type in a number")
    age = datetime.now().year - birthYear
    print(f"{name}, you are {age} years old.")


def print_calculations(a, b):
    print(f"Sum (a + b): {a + b}")
    print(f"Difference (a - b): {a - b}")
    print(f"Product (a * b): {a * b}")
    print(f"Quotient (a / b): {a / b}")
    print(f"Square root of the sum (sqrt(a + b)): {math.sqrt(a + b)}")
    print(f"Power (a^b): {a ** b}")
    print(f"Power (b^a): {b ** a}")


def calculate_circle(radius):
    return {"area": math.pi * radius ** 2,
            "circumference": 2 * math.pi * radius}


def compare_numbers(a, b):
    result = (
        0
        if a == b
        else 1
        if a > b
        else -1
    )

    return result


def say_hello_to_adults():
    while True:
        try:
            name = input("Enter your name: ")
            age = datetime.now().year - int(input("Enter your year of birth: "))
            break
        except ValueError:
            print("Enter a number")

    if age < 18:
        print(f"{name}, you are {age} years old, you are not an adult")

    else:
        print(f"{name}, you are {age} years old, you are an adult")


def check_if_even(a):
    return a % 2 == 0


def can_form_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def grade_student(score, output_format):
    if score < 50:
        grade_num = 2.0
        grade_verbal = "niedostateczny"
    elif score < 60:
        grade_num = 3.0
        grade_verbal = "downstate"
    elif score < 70:
        grade_num = 3.5
        grade_verbal = "dostateczny plus"
    elif score < 80:
        grade_num = 4.0
        grade_verbal = "dobry"
    elif score < 90:
        grade_num = 4.5
        grade_verbal = "dobry plus"
    elif score < 100:
        grade_num = 5.0
        grade_verbal = "bardzo dobry"
    else:
        grade_num = 5.5
        grade_verbal = "celujący"

    if output_format == 'both':
        return {"grade_num": grade_num, "grade_verbal": grade_verbal}
    elif output_format == 'numerical':
        return {"grade_num": grade_num}
    else:
        return {"grade_verbal": grade_verbal}


if __name__ == '__main__':
    main()
