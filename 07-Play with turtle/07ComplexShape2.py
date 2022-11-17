import turtle

#Create the screen instance
s = turtle.getscreen()
#Create Turtle instance
t = turtle.Turtle()
#Shape the turtle look like tutle
t.shape("turtle")
#Make it green
t.color("green")
#Increase the speed of Turtle
turtle.speed(7)
cycle=1
while cycle<=72:
    count=1
    while count<=4:
        t.forward(100)
        t.right(90)
        count+=1
    cycle+=1
    t.right(5)
#Wait untill close the screen
turtle.done()
