from decimal import *
import math


#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

for x in range(56, 100):
    print(2*x**2+2*x+2)

#2 ask the user for a number and print its factorial (1p)

print('Insert a number here:')
x = int(input())
print('Factorial of your number is ', math.factorial(x))

#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

#def lowestValueFromArray(x):

print('How many elements do you want to have in array?:')
n = int(input())
print('Insert numbers')
array = []
for _ in range(n):
    x = int(input())
    array.append(x)

print('This is your array: ')
print(array)
print('This is a lowest value from your array: ')
print(min(array))

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
