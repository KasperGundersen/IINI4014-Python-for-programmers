import turtle
from Die import Die

# Method for creating the canvas. sets the pen at the given coordinates


def createWindow(pen, die):
    window = turtle.Screen()
    pen.up()
    pen.goto(die.posX, die.posY)
    pen.down()

# Method for drawing the dice. Fills it with the given color


def drawDie(pen, die):
    pen.fillcolor(terning.dieColor)
    pen.begin_fill()
    for i in range(4):
        pen.forward(die.size)
        pen.left(90)
    pen.end_fill()

# A helping method for drawing a dot in the center of the dice
# it is used when rolling a 1,3 or 5


def drawCenterDot(pen, die):
    pen.forward(die.size/2)
    pen.left(90)
    pen.forward(die.size/2)
    pen.dot()

# Method for drawing the dot on the dice.
# First it roll the die, then draws the result
# The even numbers are drawn in the same way, and the odd numbers are drawn in the same way


def drawDots(pen, die):
    pen.pencolor(die.dotColor)
    dots = die.roll()
    pen.up()
    length = die.size

    # The even numbers are drawn as two and two dots in a row
    # 2 dots equals to 1 row, 4 dots = 2 rows, 6 dots = 3 rows
    if(dots % 2 == 0):
        pen.forward(length/4)
        pen.left(90)
        myLength = length/dots
        if(dots == 4):
            myLength = length/3
        if(dots == 6):
            myLength = length/4

        pen.forward(myLength)
        position = [pen.xcor(), pen.ycor()]
        pen.right(90)
        for i in range(int(dots/2)):
            pen.dot()
            pen.forward(length/2)
            pen.dot()
            pen.goto(position[0], position[1]+myLength*(i+1))

    # If a odd number is rolled the method draws a center dot regardless
    else:
        # draws center if it rolls 1,3 or 5
        drawCenterDot(pen, die)

        # If you get 3 or 5 dots, it will draw dots around the center dot
        # Two more dots if you roll 3, and four more if you roll 5
        if(dots == 5 or dots == 3):
            quarter = length/4
            position = [pen.xcor(), pen.ycor()]

            pen.goto(position[0]+quarter, position[1]+quarter)
            pen.dot()
            pen.goto(position[0]-quarter, position[1]-quarter)
            pen.dot()
            if(dots == 5):
                pen.goto(position[0]+quarter, position[1]-quarter)
                pen.dot()
                pen.goto(position[0]-quarter, position[1]+quarter)
                pen.dot()


if __name__ == "__main__":

    # Creates a die and sets some colors
    terning = Die(-50, -50, 200)
    terning.setColor("pink", "blue")

    pen = turtle.Turtle()
    pen.speed(0)

    # Create a canvas, then draws the die and then the dots
    createWindow(pen, terning)
    drawDie(pen, terning)
    drawDots(pen, terning)

    pen.hideturtle()
    turtle.done()
    pass
