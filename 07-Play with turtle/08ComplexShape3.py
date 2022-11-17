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
turtle.speed(15)
cycle=1
length=10
while cycle<=100:
    t.forward(length)
    t.right(90)
    cycle+=1
    length+=2

#Wait untill close the screen
turtle.done()
