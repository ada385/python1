import turtle as t

t.Screen().bgcolor("white")
pen = t.Turtle()

pen.speed(0)

def rysuj_okrag():
    
    n = 0
    while n<360:

        pen.forward(1)
        pen.right(1)

        n += 1

rysuj_okrag()

pen.up()
pen.backward(3)
pen.right(90)
pen.down()

rysuj_okrag()

pen.up()
pen.left(90)
pen.forward(6)
pen.left(90)
pen.down()

rysuj_okrag()

pen.up()
pen.right(90)
pen.forward(120)
pen.down()

rysuj_okrag()

pen.up()
pen.left(90)
pen.down()

rysuj_okrag()

t.done()