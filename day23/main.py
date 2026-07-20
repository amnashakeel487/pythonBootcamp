from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# ---------------------------- SCREEN SETUP ---------------------------- #

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# ---------------------------- CREATE OBJECTS ---------------------------- #

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# ---------------------------- KEYBOARD ---------------------------- #

screen.listen()
screen.onkey(player.go_up, "Up")

# ---------------------------- GAME LOOP ---------------------------- #

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect reaching finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()