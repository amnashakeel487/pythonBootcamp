import turtle
import pandas as pd

# ---------------------------- SCREEN SETUP ---------------------------- #

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ---------------------------- READ DATA ---------------------------- #

data = pd.read_csv("50_states.csv")

all_states = data["state"].to_list()
guessed_states = []

# ---------------------------- GAME LOOP ---------------------------- #

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    # If user closes the input dialog
    if answer_state is None:
        break

    answer_state = answer_state.title()

    # Exit and save missing states
    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    # Check correct answer
    if answer_state in all_states and answer_state not in guessed_states:

        guessed_states.append(answer_state)

        # Get row of the guessed state
        state_data = data[data.state == answer_state]

        # Create turtle for writing
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        # Move to state's coordinates
        writer.goto(
            state_data.x.item(),
            state_data.y.item()
        )

        # Write state name
        writer.write(
            answer_state,
            align="center",
            font=("Arial", 8, "normal")
        )

# ---------------------------- END OF GAME ---------------------------- #

if len(guessed_states) == 50:
    winner = turtle.Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(0, 250)
    winner.color("green")
    winner.write(
        "🎉 Congratulations! You guessed all 50 states!",
        align="center",
        font=("Arial", 16, "bold")
    )

screen.exitonclick()