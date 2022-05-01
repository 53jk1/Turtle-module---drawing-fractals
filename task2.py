import turtle
t = turtle.Turtle()

x = 1

for i in range(90):
    x = x*1.1
    for i in range(4):
        t.forward(x)
        t.left(90)