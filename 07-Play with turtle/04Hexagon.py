import turtle

#Create the screen instance
s = turtle.getscreen()
#Create Turtle instance
t = turtle.Turtle()
#Shape the turtle look like tutle
t.shape("turtle")
#Make it green
t.color("green")
count=1
while count<=6:
    t.forward(100)
    t.right(60)
    count+=1
#Wait untill close the screen
turtle.done()
