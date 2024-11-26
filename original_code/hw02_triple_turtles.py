######################################################################
# Author: Dr. Scott Heggen           TODO: Change this to your name, if modifying
# Username: heggens                  TODO: Change this to your username, if modifying

# Assignment: HW02: Loopy Turtles, Loopy Languages
# Purpose: Draws a 3D cube using turtles and nested for loops
######################################################################
# Acknowledgements:

# Original code by: Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import tkinter as tk       # Python's most commonly used GUI package.
import turtle  as turtle   # allows us to use the turtles library
#hopefully tk doesn't override Turtle AGAIN

from asyncio import wait_for
from datetime import time
from turtle import Turtle

from pygame.time import delay

state_stack = [] # for undo function

height = 100
width = 100
depth = 15
turtle.speed(0)
turtle.color('white')
# All the colors to use; the rows loop will select a color on each iteration
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'white']


wn = turtle.Screen()                    # creates a graphics window

box_turtle = turtle.Turtle()            # create a turtle named myturtle
box_turtle.speed(0)
box_turtle.penup()
box_turtle.shape('circle')              # possible shapes are 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
box_turtle.shapesize(5)

for row in range(6):                    # Loop for the rows
    box_turtle.color(colors[row])       # Set the turtles color on each row
    for col in range(7):                # Loop for the columns
        for dep in range(1):            # Loop for the depth
            # Moves box_turtle to a position based on row, col, and dep
            box_turtle.goto(col * width - 300 + dep * depth, row * height - 250 + dep * depth * 0.7)
            box_turtle.stamp()          # Stamps the shape onto the window
            box_turtle.stamp()          # Stamps the shape onto the window
colors_undo = ['white','white','white','white','white','white']
for row in range(6):                    # Loop for the rows
    box_turtle.color(colors_undo[row])       # Set the turtles color on each row
    for col in range(7):                # Loop for the columns
        for dep in range(1):            # Loop for the depth
            # Moves box_turtle to a position based on row, col, and dep
            box_turtle.goto(col * width - 300 + dep * depth, row * height - 250 + dep * depth * 0.7)
            box_turtle.stamp()          # Stamps the shape onto the window
            box_turtle.stamp()          # Stamps the shape onto the window

box_turtle.shapesize(1)
box_turtle.color('black')
box_turtle.goto(-140,-60)
box_turtle.pensize(3)
box_turtle.pencolor('black')
box_turtle.pendown()
box_turtle.forward(270)
box_turtle.left(90)
box_turtle.forward(125)
box_turtle.left(90)
box_turtle.forward(270)
box_turtle.left(90)
box_turtle.forward(125)
box_turtle.left(90)
box_turtle.forward(270)
box_turtle.forward(-210)

box_turtle.penup()


box_turtle.forward(-45)
box_turtle.left(90)
box_turtle.forward(15)

# write text
# move turtle

box_turtle.write("T-PEN", font=("Matrix II",
                                    60, "normal"))
delay(800)
box_turtle.color('gray')
box_turtle.write("T-PEN", font=("Matrix II",
                                    60, "normal"))
delay(200)
box_turtle.color('light gray')
box_turtle.write("T-PEN", font=("Matrix II",
                                    60, "normal"))
delay(200)
box_turtle.pendown()
box_turtle.pensize(1500)
box_turtle.color('white')
box_turtle.forward(1)
box_turtle.pensize(2)
#Box Turtle should now be invisible

#-------------------------------------
# Main Program Start
# IMPORT BUTTONS
#-------------------------------------

def undosave():
    "Creates a Savestate"
    print("Save Function Placeholder")
    '''
    state = {
    'position': turtle.pos(ClickyTurtle),
    'pen_color': turtle.pencolor(ClickyTurtle),
    'pen_state': turtle.isdown(ClickyTurtle)
    }
    state_stack.append(state)
    '''

def undoload():
    "Loads A Savestate"
    print("Load Function Placeholder")
    '''
    if state_stack:
        last_state = state_stack.pop(ClickyTurtle)
        turtle.penup(ClickyTurtle)
        turtle.goto(last_state['position'])
        if last_state['pen_state']:
            turtle.pendown(ClickyTurtle)
        turtle.pencolor(last_state['pen_color'])#----FROM T12----
    '''

ClickyTurtle = tk.Tk()

button_save = tk.Button(ClickyTurtle,
                   text="Save",
                   command=undosave,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_load = tk.Button(ClickyTurtle,
                   text="Load",
                   command=undoload,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_Clear = tk.Button(ClickyTurtle,
                   text="Clear",
                   command=turtleclear,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_PenUp = tk.Button(ClickyTurtle,
                   text="Pen Up",
                   command=turtleup,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_PenDown = tk.Button(ClickyTurtle,
                   text="Pen Down",
                   command=turtledown,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_Color = tk.Button(ClickyTurtle,
                   text="Pen Color",
                   command=pencolor,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button_save.pack(padx=20, pady=5)
button_load.pack(padx=20, pady=5)
button_Clear.pack(padx=20, pady=5)
button_PenUp.pack(padx=20, pady=5)
button_PenDown.pack(padx=20, pady=5)
button_Color.pack(padx=20, pady=5)

#Drawing Screen Import
#(Clicky Turtle is from T12  events and guis)

class ClickyTurtle:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(700,700)
        self.wn.title("T-PEN")
        self.wn.bgcolor("lightgreen")
        self.tess = turtle.Turtle()
        self.tess.color("Black")
        self.tess.pensize(1)
        self.tess.turtlesize(0.5)
        self.tess.shape("circle")

        # NOTICE that the screen is responding to the click events!
        self.wn.onclick(self.h1)      # Wire up a click handler to the window.

        self.wn.mainloop()

    def h1(self, x, y):
        self.tess.goto(x, y)

    def turtle_clear(self):
        "Uses the TurtleClear command"
        self.tess.clear()  # Clears the screen
        print("Clear Function Placeholder")

    def turtle_up(self):
        "Makes Pen Stop Drawing"
        self.tess.penup()  # Lifts the pen so the turtle doesn't draw while moving
        print("PenUp Function Placeholder")

    def turtle_down(self):
        "Makes Pen Resume Drawing"
        self.tess.pendown()  # Puts the pen down so the turtle draws as it moves
        print("PenDown Function Placeholder")

    def pen_color(self, color):
        "Changes Pen Color"
        self.tess.color(color)
        print("Pencolor Function Placeholder")
    #   colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'white']
    #   turtle.color(colors[1])       # Set the turtles color on each row

def main():
    c = ClickyTurtle()

main()

wn.exitonclick()                        # Closes the program when a user clicks in the window
