import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)

user_bet = screen.textinput(
    title="Make your Bet",
    prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

# Create turtles
for turtle_index in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()

    new_turtle.goto(x=-280, y=y_positions[turtle_index])

    all_turtles.append(new_turtle)


race_on = False

if user_bet:
    race_on = True


while race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 280:

            race_on = False

            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won.")
            else:
                print(f"You lost! The {winning_color} turtle won.")

        random_distance = random.randint(0, 10)

        turtle.forward(random_distance)


screen.exitonclick()