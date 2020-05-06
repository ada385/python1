import turtle as t

t.Screen().bgcolor("white")
pen = t.Turtle()

pen.speed(2)

m = 0
n = 100

pen.up()
pen.goto(0,0)
pen.left(45)
pen.forward((n*(2 ** 0.5))/2)
pen.right(135)
pen.down()

while m < 10:

    pen.forward(n)
    pen.right(90)
    pen.forward(n)
    pen.right(90)
    pen.forward(n)
    pen.right(90)
    pen.forward(n)

    pen.up()
    pen.goto(0,0)
    
    pen.left(45)
    pen.forward(((n - 10)*(2 ** 0.5))/2)
    pen.right(135)
    pen.down()

    n -= 10
    m += 1



t.done()