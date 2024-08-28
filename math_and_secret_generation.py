"""This python program is a menu-driven python application with menu to
conduct some math and generate secure password"""
import secrets
import string
from datetime import datetime
import math

def generate_secure_password(length=12):
    """Generate a secure password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def calculate_percentage(part, whole):
    """Calculate the percentage of part/whole and format it."""
    try:
        percentage = (part / whole) * 100
        return f"{percentage:.2f}%"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def days_until_july_4_2025():
    """Calculate the number of days from today until July 4, 2025."""
    future_date = datetime(2025, 7, 4)
    today = datetime.today()
    delta = future_date - today
    return delta.days

def law_of_cosines(a, b, angle_degrees):
    """Calculate the length of the third side of a triangle using the Law of Cosines."""
    angle_radians = math.radians(angle_degrees)
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_radians))
    return c

def volume_of_cylinder(radius, height):
    """Calculate the volume of a right circular cylinder."""
    return math.pi * (radius ** 2) * height

def main():
    """Displayed a menu with various options and processes user
input accordingly. The function will run in a loop, displaying the
menu and executing the selected option until user choose to exit"""
    while True:
        print("\nMenu:")
        print("a. Generate Secure Password")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")

        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            try:
                length = int(input("Enter the desired password length (default is 12): ") or 12)
                if length < 1:
                    raise ValueError("Password length must be positive.")
                password = generate_secure_password(length)
                print(f"Generated password: {password}")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        elif choice == 'b':
            try:
                part = float(input("Enter the part value: "))
                whole = float(input("Enter the whole value: "))
                if whole == 0:
                    raise ValueError("The whole value cannot be zero.")
                result = calculate_percentage(part, whole)
                print(f"Formatted Percentage: {result}")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        elif choice == 'c':
            days = days_until_july_4_2025()
            print(f"There are {days} days until July 4, 2025.")

        elif choice == 'd':
            try:
                a = float(input("Enter the length of side a: "))
                b = float(input("Enter the length of side b: "))
                angle = float(input("Enter the angle between sides a and b (in degrees): "))
                if angle <= 0 or angle >= 180:
                    raise ValueError("The angle must be between 0 and 180 degrees.")
                c = law_of_cosines(a, b, angle)
                print(f"The length of the third side is: {c:.2f}")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        elif choice == 'e':
            try:
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                if radius < 0 or height < 0:
                    raise ValueError("Radius and height must be non-negative.")
                volume = volume_of_cylinder(radius, height)
                print(f"The volume of the cylinder is: {volume:.2f}")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        elif choice == 'f':
            print("Thank you for visiting the application. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid menu option.")

if __name__ == "__main__":
    main()
