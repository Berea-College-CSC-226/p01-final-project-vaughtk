######################################################################
# Author: Kai Vaught
# Username: VaughtK

# Assignment: HW02: Loopy Turtles, Loopy Languages
# Purpose: Draws a 3D cube using turtles and nested for loops
######################################################################
# Acknowledgements:

# Original code by: Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import tkinter as tk       # Python's most commonly used GUI package.
import turtle   # allows us to use the turtles library
from asyncio import wait_for
import time
#hopefully self doesn't override Turtle AGAIN
import pygame
from pygame.time import delay

'''
Pygame.time delay is to keep delays consistent, mainly for the intro but also to space commands.
I also think it's appropriate to preemptively import a pygame library at this time due to my plans
to use arrow key commands.
At this current state they are unused.

I will use https://docs.python.org/3/library/turtle.html#turtle.onkeypress
to learn how to use hoselfeys with Turtles without involving an external library.
'''

TurtleSizeSeries = [0.4, 0.5, 0.7, 1, 1.3, 1.5, 1.8, 2, 2.5, 3]
'''A list of different Turtle Sizes'''

class TPen:
    def __init__(self):
        # Legend of Tuna keyboard movement
        self.wn = turtle.Screen()
        self.wn.setup(700,700)
        self.wn.title("T-PEN")
        self.wn.bgcolor("white")
        self.c = ClickyTurtle(self.wn)

        # Tutorial
        print(
            "HOTKEYS: Number Rows = Pen/Turtle Sizes F - ; = Colors <, and >. = Pen Down and Pen Up BackSpace = Clear. WASD + ARROWS = MOVE")
        self.c.penup()
        self.c.forward(-305)
        self.c.write("Number Rows = Pen/Turtle Sizes F thru ; = Colors <, and >. = Pen Down and Pen Up BackSpace = Clear. WASD + ARROWS = MOVE")
        self.c.forward(305)
        self.c.pendown()
        # Tutorial


        self.wn.onkey(self.c.go_up, "Up")
        self.wn.onkey(self.c.go_up, "w")
        self.wn.onkey(self.c.go_down, "Down")
        self.wn.onkey(self.c.go_down, "s")
        self.wn.onkey(self.c.go_left, "Left")
        self.wn.onkey(self.c.go_left, "a")
        self.wn.onkey(self.c.go_right, "Right")
        self.wn.onkey(self.c.go_right, "d")
        self.wn.onkey(self.c.pen_up, ",")
        self.wn.onkey(self.c.pen_down, ".")
        self.wn.onkey(self.c.pen_color_black, "f")
        self.wn.onkey(self.c.pen_color_red, "g")
        self.wn.onkey(self.c.pen_color_blue, "h")
        self.wn.onkey(self.c.pen_color_green, "j")
        self.wn.onkey(self.c.pen_color_yellow, "k")
        self.wn.onkey(self.c.pen_color_orange, "l")
        self.wn.onkey(self.c.pen_color_purple, ";")
        self.wn.onkey(self.c.pen_size_1, "1")
        self.wn.onkey(self.c.pen_size_2, "2")
        self.wn.onkey(self.c.pen_size_3, "3")
        self.wn.onkey(self.c.pen_size_4, "4")
        self.wn.onkey(self.c.pen_size_5, "5")
        self.wn.onkey(self.c.pen_size_6, "6")
        self.wn.onkey(self.c.pen_size_7, "7")
        self.wn.onkey(self.c.pen_size_8, "8")
        self.wn.onkey(self.c.pen_size_9, "9")
        self.wn.onkey(self.c.pen_size_10, "0")
        self.wn.onkey(self.c.turtle_clear, "BackSpace")



        self.wn.onclick(self.c.h1)

        self.c.goto(+1, +0)
        self.c.goto(+-1, 0)
        self.wn.listen()
        self.wn.mainloop()

#Drawing Screen Import
#(Clicky Turtle is from T12  events and guis)

class ClickyTurtle(turtle.Turtle):
    def __init__(self, wn):
        super().__init__()
        self.surf = None # Dummy Values make the code compatible.
        # self.rect = None # Legend of Tuna was concerned with player visibility and preventing the player from leaving screen confines. The self compatible Turtle does not have these concerns in mind.
        # self.rect = self.surf.get_rect()
        self.screen = wn
        self.color("black")
        self.pensize(1)
        self.turtlesize(0.5)
        self.speed(0)
        self.shape("circle")
    def go_up(self):
        self.setheading(90)
        self.forward(10)

    def go_down(self):
        self.setheading(270)
        self.forward(10)

    def go_left(self):
        self.setheading(180)
        self.forward(10)

    def go_right(self):
        self.setheading(0)
        self.forward(10)

    def pen_up(self):
        self.penup()

    def pen_down(self):
        self.pendown()

    def pen_color_black(self):
        self.pencolor("black")
        self.color("black")

    def pen_color_red(self):
        self.pencolor("red")
        self.color("red")

    def pen_color_green(self):
        self.pencolor("green")
        self.color("green")

    def pen_color_blue(self):
        self.pencolor("blue")
        self.color("blue")

    def pen_color_yellow(self):
        self.pencolor("yellow")
        self.color("yellow")

    def pen_color_orange(self):
        self.pencolor("orange")
        self.color("orange")

    def pen_color_purple(self):
        self.pencolor("purple")
        self.color("purple")

    def pen_size_1(self):
        self.turtlesize(TurtleSizeSeries[0])
        self.pensize(1)

    def pen_size_2(self):
        self.turtlesize(TurtleSizeSeries[1])
        self.pensize(2)

    def pen_size_3(self):
        self.turtlesize(TurtleSizeSeries[2])
        self.pensize(4)

    def pen_size_4(self):
        self.turtlesize(TurtleSizeSeries[3])
        self.pensize(6)

    def pen_size_5(self):
        self.turtlesize(TurtleSizeSeries[4])
        self.pensize(8)

    def pen_size_6(self):
        self.turtlesize(TurtleSizeSeries[5])
        self.pensize(10)

    def pen_size_7(self):
        self.turtlesize(TurtleSizeSeries[6])
        self.pensize(20)

    def pen_size_8(self):
        self.turtlesize(TurtleSizeSeries[7])
        self.pensize(25)

    def pen_size_9(self):
        self.turtlesize(TurtleSizeSeries[8])
        self.pensize(30)

    def pen_size_10(self):
        self.turtlesize(TurtleSizeSeries[9])
        self.pensize(40)

    def turtle_clear(self):
        self.clear()

    def button_turtle_clear(self):
        self.clear()

        '''
        # NOTICE that the screen is responding to the click events!
        self.wn.onclick(self.h1)      # Wire up a click handler to the window.
        # onclick should only be implemented once Legend of Tuna movement is done
        '''


    def h1(self, x, y):
        self.goto(x, y)

    # -------------------------------------
    # Main Program Start
    # IMPORT BUTTONS
    # -------------------------------------

'''
    ui = tk.Tk()

    button_Clear = tk.Button(ui,
                             text="Clear (BCK-SPC)",
                             command=button_turtle_clear,
                             bd=3,
                             bg="lightgray",
                             font=("Arial", 12),
                             height=2,
                             highlightthickness=2,
                             padx=10,
                             pady=5,
                             width=15,
                             wraplength=100)

    button_PenUp = tk.Button(ui,
                             text="Pen Up (,<)",
                             command="turtle_up",
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

    button_PenDown = tk.Button(ui,
                               text="Pen Down(.>)",
                               command="turtle_down",
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

    button_Color = tk.Button(ui,
                             text="Pen Color (SPACE)",
                             command="pen_color",
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

    button_Clear.pack(padx=20, pady=5)
    button_PenUp.pack(padx=20, pady=5)
    button_PenDown.pack(padx=20, pady=5)
    button_Color.pack(padx=20, pady=5)



                THESE ARE ALL DEPRECATED

            def turtle_clear_deprecated(self):
                "Uses the TurtleClear command"
                self.clear()  # Clears the screen
        
            def turtle_up(self):
                "Makes Pen Stop Drawing"
                self.penup()  # Lifts the pen so the turtle doesn't draw while moving
                print("PenUp Function Placeholder")
        
            def turtle_down(self):
                "Makes Pen Resume Drawing"
                self.pendown()  # Puts the pen down so the turtle draws as it moves
                print("PenDown Function Placeholder")
        
            def pen_color(self, color):
                "Changes Pen Color"
                self.color(color)
                print("Pencolor Function Placeholder")
                colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'white'] #List that turtle Tess takes colors from
                self.color(colors[1])       # Cycles the turtle's color
                self.pencolor(colors[1])  # Cycles the turtle's pen color
        
            def listen(self, xdummy, ydummy):
                pass
'''

def main():
    c = TPen()
    height = 100
    width = 100
    depth = 15
    turtle.speed(0)
    turtle.color('white')

    wn = turtle.Screen()  # creates a graphics window


main()


