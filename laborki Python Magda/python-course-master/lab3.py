#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
#3 Test your solutions

import math

def calculateFunctions():
    figure = raw_input("Enter your figure - ")
    print("Your figure is " + figure)

    if figure == 'circle':
        print("Insert value of the radius ")
        x = int(input())
        fieldOfCircle = math.pi * x**2
        print('Field of the circle is ', fieldOfCircle)
    elif figure == "rectangle":
        print("Insert value of the first side ")
        x = int(input())
        print("Insert value of the second side ")
        y = int(input())
        fieldOfRectangle = x*y
        print("Field of the rectangle is ", fieldOfRectangle)
    elif figure == "triangle":
        print("Insert value of the baseline")
        x = int(input())
        print("Insert value of the height")
        y = int(input())
        fieldOfTriangle = x*y/2
        print("Field of the triangle is ", fieldOfTriangle)
    elif figure == "rhombus":
        print("Insert value of first diagonal")
        x = int(input())
        print("Insert value of first diagonal")
        y = int(input())
        fieldOfRhombus = x*y/2
        print("Field of the triangle is ", fieldOfRhombus)
    else:
        print("Sorry, I don`t recognize the figure and cannot calculate the field. Try again. The avaiable figures are: circle, triangle, rectangle, rhombus")
        calculateFunctions()

#calculateFunctions()


#######