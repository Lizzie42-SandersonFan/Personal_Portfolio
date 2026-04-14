# Stuff for the main. This stuff will be called on main.py
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from pet_sim_main import ps_main
from gb_main import gb_main
from fp_main import fp_main
from movie_recomender import mv_main

# Build main pop-up.
# Text: Welcome to my programming portfolio! Click on any of the buttons to learn about a project I have built and get to run it!
# Buttons: Pet Simulator, Simple Grade Book, Sierpinski Triangle Generator, Movie Recomender

# Pet Simulator:
    # Discription: This is a project that saves pets that you have made to a CSV and you are able to select a pet and take care of it!
    # Learned: I learned how to read a CSV and begin applying classes
    # Challenge: being able to correctly update information in the CSV
    # Button to run. When clicked, show text that says: This is running in the terminal, please head there to use this program
def pet_sim_window():
    new_window = Toplevel()
    new_window.title("Pet Simulator")
    new_window.minsize(1500, 500)
    new_window.maxsize(2000,2000)
    new_window.geometry("300x300+200+200")

    about = Label(new_window, text="This is a project that saves pets that you have made to a CSV and you are able to select a pet and take care of it!\nSome things that I learned from this project were how to read a CSV and start applying my newly learned knowledge of classes!\nOne challenge I had while making this was that I was struggling with updating the information in the CSV correctly.", font=("Comic Sans", 14, "bold"))

    run_btn = tk.Button(new_window, text="Run the code!", command=lambda: [change_text(run_btn), ps_main()])
    run_btn.pack()

    leave_btn = tk.Button(new_window, text="Close Window", command=new_window.destroy)
    leave_btn.pack()

    about.pack()

# Simple Grade Book:
    # Discription: This is a project where you can manage a group of students in a gradebook. You can add grades, add students, and see information!
    # Learned: I learned how to apply class relationships
    # Challenge: Figuring out the class relationship and putting methods in the right class
    # Button to run. When clicked, show text that says: This is running in the terminal, please head there to use this program
def gradebook_window():
    new_window = Toplevel()
    new_window.title("Gradebook Manager")
    new_window.minsize(1500, 500)
    new_window.maxsize(2000,2000)
    new_window.geometry("300x300+100+100")

    about = Label(new_window, text="This is a project where you can manage a group of students in a gradebook. You can add grades, add students, and see information!\nSomething I learned from this project was the aggregation class relationship.\nOne challenge I had while making this was figuring out the classes in the first place, and what methods go in which class.", font=("Comic Sans", 14, "bold"))

    run_btn = tk.Button(new_window, text="Run the code!", command=lambda: [change_text(run_btn), gb_main()])
    run_btn.pack()

    leave_btn = tk.Button(new_window, text="Close Window", command=new_window.destroy)
    leave_btn.pack()

    about.pack()

# Sierpinski Triangle Generator:
    # Discription: This is a project that allows you to generate a Sierpinski Triangle with a certain depth of 1-5, as well as pick colors for your triangle!
    # Learned: I learned about recursion functions
    # Challenge: Figuring out the recursion
    # Button to run. When clicked, show text that says: This is running in the terminal, please head there to use this program
def triangle_window():
    new_window = Toplevel()
    new_window.title("Sierpinski Triangle")
    new_window.minsize(1500, 500)
    new_window.maxsize(2000,2000)
    new_window.geometry("300x300+100+100")

    about = Label(new_window, text="This is a project that allows you to generate a Sierpinski Triangle with a certain depth of 1-5, as well as pick colors for your triangle!\nSomething I learned from this project was the recursion function.\nOne challenge I had while making this was figuring out the recursion and making it draw the triangle.", font=("Comic Sans", 14, "bold"))

    run_btn = tk.Button(new_window, text="Run the code!", command=lambda: [change_text(run_btn), fp_main()])
    run_btn.pack()

    leave_btn = tk.Button(new_window, text="Close Window", command=new_window.destroy)
    leave_btn.pack()

    about.pack()

# Movie Recomender:
    # Discription: This is a project where you can pick parameters for movies you would like to search for in a pre-established CSV!
    # Learned: Filing through a CSV and parsing the retrived information
    # Challenge: Figuring out how to apply multiple filters
    # Button to run. When clicked, show text that says: This is running in the terminal, please head there to use this program
def movie_window():
    new_window = Toplevel()
    new_window.title("Movie Recomender")
    new_window.minsize(1500, 500)
    new_window.maxsize(2000,2000)
    new_window.geometry("300x300+100+100")

    about = Label(new_window, text="This is a project where you can pick parameters for movies you would like to search for in a pre-established CSV!\nSomething I learned from this project was filing through a CSV and parsing any retrived information.\nOne challenge I had while making this was figuring out how I would manage the user enter multiple parameters.", font=("Comic Sans", 14, "bold"))

    run_btn = tk.Button(new_window, text="Run the code!", command=lambda: [change_text(run_btn), mv_main()])
    run_btn.pack()

    leave_btn = tk.Button(new_window, text="Close Window", command=new_window.destroy)
    leave_btn.pack()

    about.pack()

def change_text(button):
    button.config(text="This program is running in the terminal, head there!")
