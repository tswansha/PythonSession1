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
while cycle<=72:
    t.circle(50)
    t.right(5)
    cycle+=1

#Wait untill close the screen
turtle.done()
