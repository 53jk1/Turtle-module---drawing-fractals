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