# By Ezz

from turtle import *
speed(4.6)
Screen().bgcolor('White')
width(2)

def wood():
   for i in range(1):

      forward(100)
      left(90)
      forward(20)
      left(90)
      forward(100)
      left(90)
      forward(20)
      left(180)
      forward(100)
      right(90)
      forward(100)
      right(90)
      forward(20)
      right(90)
      forward(100)
      right(90)
      forward(100)
      right(90)
      forward(100)
      right(90)
      forward(20)
      right(90)
      forward(100)
      right(90)
      forward(20)

color('Black')
wood()

for i in range(1):
   speed(4)
   color('red')
   begin_fill()
   pensize(3)
   left(50)
   forward(133)
   circle(50, 200)
   right(500)
   circle(50, 200)
   forward(133)
   end_fill()
