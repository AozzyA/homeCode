import turtle#acutally called turtle to draw a turtle beautiful also used 
#to draw other stuff
import datetime
# to draw a square or eventually a turtle you need to do this things below
# to draw a square you want to : move forward,turn right,move forward,turn 
#right,move forward turn right

window = turtle.Screen() #click the screen to close it
turtle.delay(0)
turtle.tracer(0, 0)
brad = turtle.Turtle()
brad.ht()

def draw_square(size): #draw square for turtles
    #    while True:
    #window = turtle.Screen() #this is the background where the turtle will 
    #move
    #window.bgcolor("white") # the color of the screen
     #this is how to start drawing like time.sleep you use turtle.Turtle
    brad.forward(size)#move turtle forward takes in a number which is the distance to move forward
    brad.left(90)# moves right 
    brad.forward(size)
    brad.left(90)
    brad.forward(size)
    brad.left(90)
    brad.forward(size)
    brad.left(90)
#   brad.left(10)
    




def draw_pin():
    #for x in range(0, 36):
    draw_square(10)
    brad.left(10)
        #print "We're on time %d" % (x)

def draw_pinPin():
    for x in range(0, 18):
        brad.speed(100)
        draw_pin()
        #brad.penup()
        brad.forward(50)
        #brad.pendown()
        draw_pin()
        brad.left(90)
        #brad.penup()
        brad.fd(50)
        #brad.pendown
        draw_pin()
        brad.lt(90)
        #brad.penup()
        brad.fd(50)
        #brad.pendown()
        draw_pin()
        brad.lt(90)
        #brad.penup()
        brad.fd(50)
        #brad.pendown
        brad.lt(30)
        #print "We're on time %d" % (x)

def draw_pinLoop():
    for x in range(0, 100):
        brad.lt(10)
        draw_pinPin()
        #now = datetime.datetime.now()
        #print ("loop count: " + str(x) + " " + now.strftime("%H:%M:%S"))
        
for x in range(0, 100):
    draw_pinLoop()
    brad.rt(90)
    brad.fd(100)
    now = datetime.datetime.now()
    print ("loop count: " + str(x) + " " + now.strftime("%H:%M:%S"))
        
turtle.update()
window.exitonclick()
