from turtle import *
import math

# Name your Turtle.
#t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
 #y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
def drawnShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        alvin.forward(50)
        alvin.right(angle)
        drawnSides+=1

another = True

alvin = Turtle()
alvin.pencolor("green")
alvin.turtlesize(2,2)
alvin.pensize(5)

while another == True:
    print("How many sides?")
    numSides = int(input())
    
    print("What color?")
    chosenColor = input()
    
    drawnShape(alvin,numSides,chosenColor)

    print("Do you want to draw another shape?")
    answer = input()
    if (answer == "no"):
        another = False
        
#for side in range(sides):
#    alvin.forward(50)
#    alvin.right(angle)

print("All done")












# Close window on click.
exitonclick()
