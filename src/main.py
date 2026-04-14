# LD 1st Personal Portfolio
from main_func import *

# Call main_func function
root = tk.Tk()
# All the stuff
root.title("Home")
root.minsize(1000, 1000)
root.maxsize(2000,2000)
root.geometry("300x300+100+100")

label = tk.Label(root, text="Welcome to my programming portfolio!\nClick on any of the buttons to learn about a project I have built and get to run it!", font=("Comic Sans", 14, "bold"))

# Buttons
btn1 = tk.Button(root, text="Movie Recomender", command=movie_window)
btn1.pack()

btn2 = tk.Button(root, text="Gradebook Manager", command=gradebook_window)
btn2.pack()

btn3 = tk.Button(root, text="Pet Simulator", command=pet_sim_window)
btn3.pack()

btn4 = tk.Button(root, text="Sierpinski Triangle Generator", command=triangle_window)
btn4.pack()

btn5 = tk.Button(root, text="Close Program", command=root.destroy)
btn5.pack()

label.pack()
root.mainloop()