import turtle as t

t.Screen().bgcolor("white")
pen = t.Turtle()

n = 0
while n<360:

    pen.forward(1)
    pen.right(1)

    n += 1


t.done()