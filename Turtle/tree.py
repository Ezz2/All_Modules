# By Ezz

from turtle import *

Screen().setup(1000, 650)
Screen().bgcolor('#85D2D0')
setpos(-100, -240)
width(4)

def wood():
   for i in range(2):
      fd(120)
      left(90)
      fd(180)
      left(90)

color('#B8390E')
begin_fill()
wood()

color('Black')
wood()

up()
setpos(-250, -60)
down()


def triangle():
   for i in range(3):
      fd(400)
      left(120)

color("green")
begin_fill()
triangle()
end_fill()

color('Black')
triangle()
mainloop()
done()
