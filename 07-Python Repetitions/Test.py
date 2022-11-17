from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

shape('turtle')
for i in range(1000):
    right(90)
    forward(10 + i)
done()
