from turtle import Turtle, Screen

# Create a turtle object
tim = Turtle()

# Change turtle shape and color
tim.shape("turtle")
tim.color("blue")

# Draw a square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

# Create the screen
screen = Screen()

# Keep the window open until clicked
screen.exitonclick()