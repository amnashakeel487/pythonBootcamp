from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# ---------------- SCREEN ---------------- #

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# ---------------- OBJECTS ---------------- #

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

# ---------------- KEYBOARD ---------------- #

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# ---------------- GAME LOOP ---------------- #

game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)

    screen.update()

    ball.move()

    # Bounce from top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce from right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Bounce from left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right player misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Left player misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()