import turtle as t
import random

# Create a turtle
tim = t.Turtle()

# Set turtle speed
tim.speed("fastest")

# List of colors
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen"
]


# Function to draw a shape
def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


# Draw shapes from triangle (3 sides) to decagon (10 sides)
for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = t.Screen()
screen.exitonclick()