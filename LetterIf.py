import upperCaseLetters
import turtle

#name = input('what is your name ').lower()

window = turtle.Screen()
tur = turtle.Turtle()
tur.penup()
tur.goto(-330, 0)
#tur.goto(-645, 0)
tur.pendown()

def blah():
    print("do nothing")

def clearS():
    tur.clear()
    blah()

while True:
    name = window.textinput("Name", "What is your name?").lower()

    for letter in name:
        if letter == 'a':
            upperCaseLetters.drawA(tur)
        elif letter == 'b':
            upperCaseLetters.drawB(tur)
        elif letter == 'c':
            upperCaseLetters.drawC(tur)
        elif letter == 'd':
            upperCaseLetters.drawD(tur)
        elif letter == 'e':
            upperCaseLetters.drawE(tur)
        elif letter == 'f':
            upperCaseLetters.drawF(tur)
        elif letter == 'g':
            upperCaseLetters.drawG(tur)
        elif letter == 'h':
            upperCaseLetters.drawH(tur)
        elif letter == 'i':
            upperCaseLetters.drawI(tur)
        elif letter == 'j':
            upperCaseLetters.drawJ(tur)
        elif letter == 'k':
            upperCaseLetters.drawK(tur)
        elif letter == 'l':
            upperCaseLetters.drawL(tur)
        elif letter == 'm':
            upperCaseLetters.drawM(tur)
        elif letter == 'n':
            upperCaseLetters.drawN(tur)
        elif letter == 'o':
            upperCaseLetters.drawO(tur)
        elif letter == 'p':
            upperCaseLetters.drawP(tur)
        elif letter == 'q':
            upperCaseLetters.drawQ(tur)
        elif letter == 'r':
            upperCaseLetters.drawR(tur)
        elif letter == 's':
            upperCaseLetters.drawS(tur)
        elif letter == 't':
            upperCaseLetters.drawT(tur)
        elif letter == 'u':
            upperCaseLetters.drawU(tur)
        elif letter == 'v':
            upperCaseLetters.drawV(tur)
        elif letter == 'w':
            upperCaseLetters.drawW(tur)
        elif letter == 'x':
            upperCaseLetters.drawX(tur)
        elif letter == 'y':
            upperCaseLetters.drawY(tur)
        elif letter == 'z':
            upperCaseLetters.drawZ(tur)
        elif letter == ' ':
            upperCaseLetters.space(tur, 40)
        elif letter == '.':
            upperCaseLetters.perid(tur)

    tur.lt(1800)


    
    #turtle.listen()
    #tur.onkey(clearS, 'a')
    tur.up()
    tur.goto(-330, 0)
    tur.down()

    turtle.listen()
    turtle.onclick(clearS)
    #turtle.onrelease(clearS) 


