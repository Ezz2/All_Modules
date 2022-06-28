# By Ezz

from turtle import *

bgcolor('black')
hideturtle()
speed(15)
for i in range(120):
   if i % 2 == 0:
      color('cyan')
   else:
      color('Cyan')
      forward(i * 3)
   left(91)
done()
