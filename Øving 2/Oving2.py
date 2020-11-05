import math

# declares the initial length and number of sides in order to use Archimedes' method
sides = 6
sideLength = 1
equal = False


def ArchimedesPi():
    global sideLength
    global sides

    # Calculates the different sides and
    halfSide = sideLength/2
    adjacent = math.sqrt(1-halfSide**2)
    b = 1 - adjacent
    newSideLength = math.sqrt(b**2+halfSide**2)
    perimeter = sides*sideLength

    # Rounds pi to 10 decimals
    pi = round(perimeter/2, 10)

    # Declaring new values for the sides
    sideLength = newSideLength
    sides = sides*2

    # Returning pi
    return pi


oldPi = 0
counter = 0

while equal is False:

    # Running Archimedes' method to get pi
    newPi = ArchimedesPi()

    # Checking if the new pi is equal to the previous
    if newPi == oldPi:
        counter += 1
    oldPi = newPi
    print(newPi)

    # If we had several equal Pi in a row, the loop breaks
    if counter == 2:
        equal = True

# The result with 10 decimals:
""" 3.0
3.1058285412
3.1326286133
3.139350203
3.1410319509
3.1414524723
3.1415576079
3.1415838921
3.1415904632
3.141592106
3.1415925167
3.1415926194
3.141592645
3.1415926515
3.1415926531
3.1415926535
3.1415926536
3.1415926536
3.1415926536 """
