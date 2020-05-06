import turtle as t

t.Screen().bgcolor("white")
pen = t.Turtle()

pen.speed(5)

pen.goto(0,0)

def ramie():

    pen.forward(150)

    n = 0
    while n<10:

        pen.right(36)
        pen.forward(15)
        pen.backward(15)

        if n == 10:
            break

        n+=1
    pen.up()
    pen.goto(0,0)
    pen.down()


l = 0
while l<10:
    ramie()
    pen.right(36)

    l+=1



t.done()