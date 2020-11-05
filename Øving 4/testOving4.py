from turtle import Turtle, Screen
    
def points(amtPoints, turtle):
     for p in range(amtPoints):
        yield turtle.pos()
        turtle.dot()
        turtle.circle(200, 360/amtPoints)

def endPoints(amtPoints, factor, turtle):
    pointList = list(points(amtPoints,turtle))
    for p in range(len(pointList)):
        yield pointList[(p*factor) % len(pointList)]
    
    
def lines(amtPoints, factor, turtle):
    ep = endPoints(amtPoints, factor, turtle)
    startPoints = points(amtPoints, turtle)
    i = 0
    turtle.goto(next(startPoints))
    while i < amtPoints:
        turtle.goto(next(ep))
        turtle.penup()
        if(i < amtPoints-1):
            turtle.goto(next(startPoints))
            turtle.pendown()

        i += 1



def mainGenerator():
    t = Turtle()
    screen = Screen()
    t.speed(9)
    t.penup()
    t.goto(0, -screen.window_height()/2 + 20)
    t.pendown()
    lines(amtPoints=10, factor = 2, turtle=t)
    screen.exitonclick()

mainGenerator()
