from datetime import datetime
import math


def main():
    print("\nZadanie 1")
    say_hello()

    print("\nZadanie 2")
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    print_calculations(a, b)

    print("\nZadanie 3")
    radius = float(input("Enter the radius of the circle: "))
    print(calculate_circle(radius))

    print("\nZadanie 4")
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    compare_numbers(a, b)

    print("\nZadanie 5")
    say_hello_to_adults()

    print("\nZadanie 6")
    a = float(input("Enter a number: "))
    print("The number is even" if check_if_even(a) else "The number is odd")

    print("\nZadanie 7")
    a = float(input("Enter the first length: "))
    b = float(input("Enter the second length: "))
    c = float(input("Enter the third length: "))
    print("Yes, the lengths can form a triangle." if can_form_triangle(a, b, c) else "No, the lengths cannot form a "
                                                                                     "triangle.")

    print("\nZadanie 8")
    score = int(input("Enter the score "))
    output_format = input("Enter the output format (numerical || verbal || both) ")
    print(grade_student(score, output_format))


def say_hello():
    name = input("Enter your name: ")
    age = datetime.now().year - int(input("Enter your year of birth: "))
    print(f"{name}, you are {age} years old.")


def print_calculations(a, b):
    print(f"Sum (a + b): {a + b}")
    print(f"Difference (a - b): {a - b}")
    print(f"Product (a * b): {a * b}")
    print(f"Quotient (a / b): {a / b if b != 0 else 'undefined'}")  # Check for division by zero
    print(f"Square root of the sum (sqrt(a + b)): {math.sqrt(a + b)}")
    print(f"Power (a^b): {a ** b}")
    print(f"Power (b^a): {b ** a}")


def calculate_circle(radius):
    if radius < 0:
        return {"error": "Invalid value, the radius cannot be negative."}
    else:
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        return {"area": area, "circumference": circumference}


def compare_numbers(a, b):
    result = (
        "The numbers are equal."
        if a == b
        else f"The number {a} is greater than {b}."
        if a > b
        else f"The number {b} is greater than {a}."
    )

    print(result)


def say_hello_to_adults():
    name = input("Enter your name: ")
    age = datetime.now().year - int(input("Enter your year of birth: "))
    if age < 18:
        print(f"{name}, you are {age} years old, you are not an adult")
    else:
        print(f"{name}, you are {age} years old, you are an adult")


def check_if_even(a):
    return a % 2 == 0


def can_form_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def grade_student(score, output_format):
    if score < 0 or score > 100:
        return {"error": "Invalid score. It must be between 0 and 100."}
    elif score < 50:
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
