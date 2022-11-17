import turtle

#Create the screen instance
s = turtle.getscreen()
#Create Turtle instance
t = turtle.Turtle()
#Shape the turtle look like tutle
t.shape("turtle")
#Make it green
t.color("green")
t.speed(5)
count=100
while count>0:
    t.circle(count)
    count-=10
turtle.done()
