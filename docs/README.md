# Kacper Bąk
## nr albumu 40851
### Akademia WSB
Autor rozwiązał zadanie pierwsze pisząc program, zawierający instrukcję rysowania kwadratu:
```python
import turtle  
t = turtle.Turtle()  
  
for i in range(4):  
    t.left(90)  
    t.forward(200)
```

Autor w ramach laboratoriów narysował również skrypt w języku Python według przykładu rozwiązując przy tym zadanie numer 2:
```python
import turtle  
t = turtle.Turtle()  
  
x = 1  
  
for i in range(90):  
    x = x*1.1  
    for i in range(4):  
        t.forward(x)  
        t.left(90)
```

![[Pasted image 20220502003545.png]]

Autor w ramach zadania 3 odwzorował algorytmem w języku Python przykładowy fraktal:
```python
import turtle  
def draw_sierpinski(length,depth):  
    if depth==0:  
        for i in range(0,3):  
            t.fd(length)  
            t.left(120)  
    else:  
        draw_sierpinski(length/2,depth-1)  
        t.fd(length/2)  
        draw_sierpinski(length/2,depth-1)  
        t.bk(length/2)  
        t.left(60)  
        t.fd(length/2)  
        t.right(60)  
        draw_sierpinski(length/2,depth-1)  
        t.left(60)  
        t.bk(length/2)  
        t.right(60)  
  
window = turtle.Screen()  
t = turtle.Turtle()  
t.speed("fastest")  
draw_sierpinski(100,3)  
t.backward(100)  
draw_sierpinski(100,3)  
t.left(60)  
t.forward(100)  
t.right(60)  
draw_sierpinski(100, 3)  
window.exitonclick()
```
![[Pasted image 20220502004843.png]]

W ramach zadania 4, autor w swoich programach wykorzystał metody i klasy do generowania fraktali, aby narysować 4 dowolne fraktale.
```python
from turtle import *  
  
import turtle  
  
tur = turtle.Turtle()  
  
tur.speed(6)  
  
tur.getscreen().bgcolor("black")  
tur.color("cyan")  
  
tur.penup()  
  
tur.goto((-200, 50))  
  
tur.pendown()  
  
  
def star(turtle, size):  
    if size <= 10:  
        return  
    else:  
        for i in range(5):  
            turtle.forward(size)  
            star(turtle, size / 3)  
  
            turtle.left(216)  
  
  
star(tur, 360)  
turtle.done()
```

![[Pasted image 20220502005312.png]]

```python
from turtle import *  
import turtle  
  
speed('fastest')  
  
right(-90)  
  
angle = 30  
  
  
def yaxis(size, lvl):  
    if lvl > 0:  
        colormode(255)  
  
        pencolor(0, 255 // lvl, 0)  
  
        forward(size)  
  
        right(angle)  
  
        yaxis(0.8 * size, lvl - 1)  
  
        pencolor(0, 255 // lvl, 0)  
  
        lt(2 * angle)  
  
        yaxis(0.8 * size, lvl - 1)  
  
        pencolor(0, 255 // lvl, 0)  
  
        right(angle)  
        forward(-size)  
  
  
yaxis(80, 7)  
turtle.done()
```

![[Pasted image 20220502005400.png]]

```python
from turtle import *  
import turtle  
  
speed = 5  
bg_color = "black"  
pen_color = "red"  
screen_width = 800  
screen_height = 800  
drawing_width = 700  
drawing_height = 700  
pen_width = 5  
title = "Python Guides"  
fractal_depth = 3  
  
  
def drawline(tur, pos1, pos2):  
    tur.penup()  
    tur.goto(pos1[0], pos1[1])  
    tur.pendown()  
    tur.goto(pos2[0], pos2[1])  
  
  
def recursivedraw(tur, x, y, width, height, count):  
    drawline(  
        tur,  
        [x + width * 0.25, height // 2 + y],  
        [x + width * 0.75, height // 2 + y],  
    )  
    drawline(  
        tur,  
        [x + width * 0.25, (height * 0.5) // 2 + y],  
        [x + width * 0.25, (height * 1.5) // 2 + y],  
    )  
    drawline(  
        tur,  
        [x + width * 0.75, (height * 0.5) // 2 + y],  
        [x + width * 0.75, (height * 1.5) // 2 + y],  
    )  
  
    if count <= 0:  # The base case  
        return  
    else:  # The recursive step  
        count -= 1  
  
        recursivedraw(tur, x, y, width // 2, height // 2, count)  
  
        recursivedraw(tur, x + width // 2, y, width // 2, height // 2, count)  
  
        recursivedraw(tur, x, y + width // 2, width // 2, height // 2, count)  
  
        recursivedraw(tur, x + width // 2, y + width // 2, width // 2, height // 2, count)  
  
  
if __name__ == "__main__":  
    screenset = turtle.Screen()  
    screenset.setup(screen_width, screen_height)  
    screenset.title(title)  
    screenset.bgcolor(bg_color)  
  
    artistpen = turtle.Turtle()  
    artistpen.hideturtle()  
    artistpen.pensize(pen_width)  
    artistpen.color(pen_color)  
    artistpen.speed(speed)  
  
    recursivedraw(artistpen, - drawing_width / 2, - drawing_height / 2, drawing_width, drawing_height, fractal_depth)  
  
    turtle.done()
```

![[Pasted image 20220502005527.png]]

```python
from turtle import *  
import turtle  
  
  
def fractdraw(stp, rule, ang, dept, t):  
    if dept > 0:  
        x = lambda: fractdraw(stp, "a", ang, dept - 1, t)  
        y = lambda: fractdraw(stp, "b", ang, dept - 1, t)  
        left = lambda: t.left(ang)  
        right = lambda: t.right(ang)  
        forward = lambda: t.forward(stp)  
        if rule == "a":  
            left();  
            y();  
            forward();  
            right();  
            x();  
            forward();  
            x();  
            right();  
            forward();  
            y();  
            left();  
        if rule == "b":  
            right();  
            x();  
            forward();  
            left();  
            y();  
            forward();  
            y();  
            left();  
            forward();  
            x();  
            right();  
  
  
turtle = turtle.Turtle()  
turtle.speed(0)  
fractdraw(5, "a", 90, 5, turtle)
```
![[Pasted image 20220502005949.png]]