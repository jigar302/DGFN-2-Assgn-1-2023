'''
TPRG 2131 Fall 202* Assignment 1
Sept, 202*
Phil J <philip.jarvis@durhamcollege>

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''


# FUNCTIONS AND FORMULA FOR 5 LEVEL AREA VOLUME CALCULATOR

import math

# FUNCTIONS FOR AREA AND VOLUME CALCULATIONS of rectangle, square, parallelogram, cube, cuboid.
def calculate_area_of_rectangle(length, breadth):
    return length * breadth

def calculate_area_of_square(side_length):
    return side_length * side_length

def calculate_area_of_parallelogram(breadth, height):
    return breadth * height

def calculate_volume_of_cube(side_length):
    return side_length ** 3

def calculate_volume_of_cuboid(length, width, height):
    return length * width * height
# Main menu started
def main():
    view_mode = 'v'  # V/v for default calculations

    while True:
        print("A/V calculator")
        print("level 0")
        print("Enter Q/q to quit")
        print("Enter V/v to change the calculated view and D/d for default view")
        print("Level 1")
        print("Calculate Area")
        print("Calculate Volume")
        print("1.Area of rectangle")
        print("2.Area of square")
        print("3.Area of parallelogram")
        print("4.Volume of cube")
        print("5.Volume of cuboid")
        choice = input("Enter your choice: ")
        
        if choice.lower() == 'q': # This will exit the program
            print("Exiting the program")
            break
        elif choice.lower() == 'v': # V will give calculation in view mode with the equation.
            view_mode = 'v'
        elif choice.lower() == 'd': # D will only give calculations.
            view_mode = 'd'
        elif choice == '1': # If press 1 it we will calculate area of rectangle.
            length = float(input("Enter the length of the rectangle: "))
            breadth = float(input("Enter the breadth of the rectangle: "))
            area = calculate_area_of_rectangle(length, breadth)
            if view_mode == 'v':
                print(f"{length} * {breadth} = {area} (x * y = z)")
            else:
                print(f"The area of the rectangle is: {area}")
        elif choice == '2': # If press 2 we will calculate area of square.
            side_length = float(input("Enter the side length of the square: "))
            area = calculate_area_of_square(side_length)
            if view_mode == 'v':
                print(f"{side_length} * {side_length} = {area} (x * x = z)")
            else:
                print(f"The area of the square is: {area}")
        elif choice == '3': # If press 3 we will calculate area of parallelogram.
            breadth = float(input("Enter the breadth of the parallelogram: "))
            height = float(input("Enter the height of the parallelogram: "))
            area = calculate_area_of_parallelogram(breadth, height)
            if view_mode == 'v':
                print(f"{breadth} * {height} = {area} (x * y = z)")
            else:
                print(f"The area of the parallelogram is: {area}")
        elif choice == '4': # If press 4 we will calculate volume of cube.
            side_length = float(input("Enter the side length of the cube: "))
            volume = calculate_volume_of_cube(side_length)
            if view_mode == 'v':
                print(f"{side_length}^3 = {volume} (x^3 = z)")
            else:
                print(f"The volume of the cube is: {volume}")
        elif choice == '5': # If press 5 we will calculate volume of cuboid.
            length = float(input("Enter the length of the cuboid: "))
            width = float(input("Enter the width of the cuboid: "))
            height = float(input("Enter the height of the cuboid: "))
            volume = calculate_volume_of_cuboid(length, width, height)
            if view_mode == 'v':
                print(f"{length} * {width} * {height} = {volume} (x * y * z = w)")
            else:
                print(f"The volume of the cuboid is: {volume}")
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()