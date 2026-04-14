# LD 1st Fractal Pattern Generator
import turtle
from fp_drawing import *
from all_helpers import *

# Create a Python program that generates a Sierpinski Triangle fractal pattern using recursion. The program should allow users to customize the recursion depth and color of the fractal.

# STEPS
# Implement a main function that runs the program and handles user input
# Create a function to draw the Sierpinski Triangle using recursion
# Use Python's turtle graphics module for drawing
# Allow users to specify:
    # Recursion depth (1-5)
    # Triangle color
# HINT: Remember to implement a base case in your recursive function to prevent infinite recursion!

# EXTRA CREDIT
# Add an option to change the background color (1 point)

def fp_main():
    
    start_point = [[-500, -400], [0, 500], [500, -400]]
    # Greet user
    while True:
        depth = input("Enter Recursion Depth for your Triangle (1-5):\n")
        if depth == "1" or depth == "2" or depth == "3" or depth == "4" or depth == "5":
            # Valid input
            depth = int(depth)
            break
        else:
            print("Invalid input. Try again")
            continue
    while True:
        pen_color = input("Enter the hex code for the LINE color you would like (Ex: #FFFFFF, #000000, #1656AD):\n").strip().upper()
        if is_valid_hexa_code(pen_color):
            # Valid color
            break
        else:
            print("Invalid input. Please try again")
            continue
    while True:
        back_color = input("Enter the hex code for the BACKGROUND color you would like (Ex: #FFFFFF, #000000, #1656AD):\n").strip().upper()
        if is_valid_hexa_code(back_color) and back_color != pen_color:
            # Valid color
            break
        else:
            if is_valid_hexa_code(back_color) == False:
                print("Invalid color. Try again")
                continue
            elif back_color == pen_color:
                print("Your background color cannot be the same as your lines. Pick a different color")
                continue
            else:
                print("What in world happened!?!?")

    # Set up turtle colors and start drawing!
    my_turtle = turtle.Turtle()
    my_turtle.hideturtle()
    my_turtle.pencolor(pen_color)
    my_turtle.pensize(6)
    my_turtle.speed("fast")
    turtle.bgcolor(back_color)
    recursive_draw(my_turtle, depth, start_point)
    turtle.done()
    # Now figure out how the user can save it as an image
