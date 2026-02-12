import turtle
import math
import random

# --- Setup ---
t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
t.speed(0)
t.width(2)
t.hideturtle()

# Make result reproducible but unique to you
random.seed(42)

# --- Drawing ---
points = 360
layers = 6

for layer in range(layers):
    radius = 40 + layer * 25
    phase = random.uniform(0, math.pi)

    for i in range(points):
        angle = math.radians(i)

        # Polar equation (custom flower curve)
        r = radius * math.sin(5 * angle + phase)

        x = r * math.cos(angle)
        y = r * math.sin(angle)

        # Color gradient
        red = (math.sin(angle) + 1) / 2
        green = (math.sin(angle + 2) + 1) / 2
        blue = (math.sin(angle + 4) + 1) / 2

        t.pencolor(red, green, blue)

        if i == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

    t.right(360 / layers)

turtle.done()
