from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1

        self.hideturtle()
        self.penup()
        self.color("black")

        self.goto(-280, 260)

        self.update_scoreboard()

    def update_scoreboard(self):
        """Display the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level by 1."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display Game Over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))