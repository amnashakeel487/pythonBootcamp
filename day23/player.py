from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)  # Face upward
        self.goto(STARTING_POSITION)

    def go_up(self):
        """Move the player upward."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Return the player to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the player reached the finish line."""
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False