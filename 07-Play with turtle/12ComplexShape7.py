import turtle

#Create the screen instance
s = turtle.getscreen()
#Create Turtle instance
t = turtle.Turtle()
t.speed(15)
s.bgcolor("black")
count=1
while count<=500:
    if count//100==0:
        t.pencolor("red")
    elif count//100==1:
        t.pencolor("orange")
    elif count//100==2:
        t.pencolor("yellow")
    elif count//100==3:
        t.pencolor("lightgreen")
    elif count//100==4:
        t.pencolor("magenta")
    else:
        t.pencolor("white")
    t.forward(5+count)
    t.right(91)
    count+=1

turtle.done()
