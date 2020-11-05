from turtle import Turtle, Screen

# Defines a method for drawing the Mandelbrot circle


def drawCircle(points, turtle):

    # Uses a list to store all the coordinates for the points along the arc
    pointsList = []

    # Draws segments of the circle and stores the pen position, determined by the points argument
    for p in range(points):
        pointsList.append(turtle.pos())
        turtle.dot()
        turtle.circle(200, 360/points)

    return pointsList


def lines(pointsList, factor, turtle):
    # Moves the pen to the product of the point multiplied by the factor-argument
    i = 0
    while i < len(pointsList):
        turtle.goto(pointsList[(i*factor) % len(pointsList)])
        turtle.penup()
        if(i < len(pointsList)-1):
            turtle.goto(pointsList[i+1])
            turtle.pendown()

        i += 1

# Creates a screen and a turtle, sets the start position to bottom of the screen


def main():
    screen = Screen()
    t = Turtle()
    t.speed(2)
    t.penup()
    t.goto(0, -screen.window_height()/2 + 20)
    t.pendown()

    points = 10
    factor = 2

    pointsList = drawCircle(points=points, turtle=t)
    lines(pointsList=pointsList, factor=factor, turtle=t)
    screen.exitonclick()


main()
