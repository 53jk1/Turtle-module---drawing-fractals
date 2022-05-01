import turtle
t = turtle.Turtle()

for i in range(4):
    t.left(90)
    t.forward(20)

def frac_widly(x):
    if x<=1:
        return
    t.left(90)
    t.forward(x)
    t.right(90)
    t.forward(x)
    frac_widly(x/3)
    
    t.backward(x)
    t.right(90)
    t.forward(x)
    
    t.left(90)
    t.forward(x)
    frac_widly(x/3)
    
    t.backward(x)
    
    t.right(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    frac_widly(x/3)

    t.backward(x)
    t.left(90)
    t.forward(x)
    t.right(90)
    t.forward(64)
    frac_widly(64)

t.speed("fastest")

x=64
t.forward(x)
frac_widly(x)
