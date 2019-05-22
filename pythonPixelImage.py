# Import turtle
import turtle as t

# Create a function to draw a pixel
def pixel(x, y, c):

    # Set the width and height of the square
    # (CHANGE THESE TO CHANGE THE SIZE OF EACH PIXEL)
    width = 50
    height = 50

    # Set the base of the square
    # (CHANGE THESE TO SET THE TOP LEFT AND TOP RIGHT OF THE IMAGE)
    baseX = -100
    baseY = -100

    # Go to the correct location for the pixel
    t.penup()
    t.goto(baseX + (x * width), baseY + (y * height))
    t.pendown()

    # Draw the pixel
    t.color(c)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Create an image
pixel(0,0,"black")
pixel(1,0,"white")
pixel(2,0,"white")
pixel(3,0,"black")
pixel(0,1,"white")
pixel(1,1,"white")
pixel(2,1,"white")
pixel(3,1,"white")
pixel(0,2,"white")
pixel(1,2,"black")
pixel(2,2,"black")
pixel(3,2,"white")
pixel(0,3,"black")
pixel(1,3,"black")
pixel(2,3,"black")
pixel(3,3,"black")


