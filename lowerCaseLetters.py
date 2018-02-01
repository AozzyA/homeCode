import turtle

window = turtle.Screen()
tur = turtle.Turtle()
tur.penup()
tur.goto(-330, 0)
#tur.goto(-650, 0)
tur.pendown()

tur.lt(90)
tur.fd(60)
tur.lt(180)
tur.fd(60)
tur.lt(90)
tur.up()
tur.fd(10)
tur.down()

def drawa(tur):
    tur.circle(30, 360)

drawa(tur)
