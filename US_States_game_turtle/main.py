import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game ")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# load data
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    guess = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in all_states:
        guessed_states.append(guess)
        marker = turtle.Turtle()
        marker.penup()
        marker.hideturtle()
        state_data = data[data.state == guess]
        marker.goto(state_data.x.item(), state_data.y.item())
        marker.write(guess)




# Convert the guess to Title case
# Check if the guess is among the 50 states
# Write correct guesses onto the map
# Use a loop to allow the user to keep guessing
# Record the correct guesses in a list
# Keep track of the score