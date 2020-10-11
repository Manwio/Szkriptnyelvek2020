#!/usr/bin/env python3

import turtle
t = turtle.Turtle()
hossz = 220
unit = 20
x = unit
y = hossz - unit


def koordinata():
    t.forward(hossz)
    t.backward(2*hossz)
    t.forward(hossz)
    t.left(90)
    t.forward(hossz)
    t.backward(2*hossz)
    t.forward(hossz)
    t.right(90)


def vonal(x, y):
    t.up()
    t.goto(0, y)
    t.down()
    t.goto(x, 0)


def negyed1(x=20, y=220, unit=20):
    while y > 0:
        vonal(x, y)
        x += unit
        y -= unit
    t.goto(0, 0)


def negyed2(x=-20, y=220, unit=20):
    while y > 0:
        vonal(x, y)
        x -= unit
        y -= unit
    t.goto(0, 0)


def negyed3(x=-20, y=-220, unit=20):
    while y < 0:
        vonal(x, y)
        x -= unit
        y += unit
    t.goto(0, 0)


def negyed4(x=20, y=-220, unit=20):
    while y < 0:
        vonal(x, y)
        x += unit
        y += unit
    t.goto(0, 0)


def main():
    t.speed(5)
    t.shape("turtle")
##############################################################################
    koordinata()
    negyed1(x, y, unit)
    negyed4(x, -y, unit)
    negyed3(-x, -y, unit)
    negyed2(-x, y, unit)

    turtle.done()


##############################################################################


if __name__ == "__main__":
    main()