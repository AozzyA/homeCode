import steamCoding
import turtle

window = turtle.Screen() #click the screen to close it
tur = turtle.Turtle()
#tur.ht()
tur.penup()
tur.goto(-330, 0)
#tur.goto(-650, 0)
tur.pendown()

tur.write('Happy birthday', font=("courier new", 18, "normal"))
tur.up()
tur.goto(-330, -125)
tur.down()
steamCoding.drawJ(tur)
steamCoding.drawA()
steamCoding.drawK()
steamCoding.drawE()
tur.write('the best dad ever!!!!!!!!!', font=("courier new", 18, "normal"))
tur.ht()
