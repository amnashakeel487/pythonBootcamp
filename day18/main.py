import turtle as t
import random
from color_list import color_list

# Enable RGB values
t.colormode(255)

# Create turtle
tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):

    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()