import turtle

t = turtle.Turtle()
count=1
while count<=100:
    t.forward(1+count)
    t.right(15)
    count+=1

turtle.done()
