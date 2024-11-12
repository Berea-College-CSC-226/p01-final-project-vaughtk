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
import turtle                           # allows us to use the turtles library
from asyncio import wait_for
from datetime import time

from pygame.time import delay

height = 100
width = 100
depth = 15
turtle.speed(0)
# All the colors to use; the rows loop will select a color on each iteration
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'white']


wn = turtle.Screen()                    # creates a graphics window

box_turtle = turtle.Turtle()            # create a turtle named myturtle
box_turtle.speed(10)
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

box_turtle.write("PEN-T", font=("Matrix II",
                                    60, "normal"))
delay(800)
box_turtle.color('gray')
box_turtle.write("PEN-T", font=("Matrix II",
                                    60, "normal"))
delay(200)
box_turtle.color('light gray')
box_turtle.write("PEN-T", font=("Matrix II",
                                    60, "normal"))
delay(200)
box_turtle.pendown()
box_turtle.pensize(1500)
box_turtle.color('white')
box_turtle.forward(1)
box_turtle.pensize(2)
box_turtle.color('black')



#----FROM T12----
class ClickyTurtle:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(600,600)
        self.wn.title("Draw")
        self.wn.bgcolor("white")
        self.tess = turtle.Turtle()
        self.tess.color("purple")
        self.tess.pensize(2)
        self.tess.shape("circle")

        # NOTICE that the screen is responding to the click events!
        self.wn.onclick(self.h1)      # Wire up a click handler to the window.

        self.wn.mainloop()

    def h1(self, x, y):
        self.tess.goto(x, y)

def main():
    c = ClickyTurtle()
main()


wn.exitonclick()                        # Closes the program when a user clicks in the window
