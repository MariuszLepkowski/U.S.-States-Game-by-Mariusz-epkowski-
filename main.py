import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game (by Mariusz Łepkowski)")
screen.screensize(600, 600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
list_of_states = states.state.to_list()

score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in list_of_states if state not in correct_guesses]
        data = pandas.DataFrame(states_to_learn)
        data.to_csv("states_to_learn.csv")
        break
    for state in list_of_states:
        if answer_state == state and answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
            score += 1
            chosen_state = states[states.state == f"{answer_state}"].to_dict()
            pen = turtle.Turtle()
            chosen_state_xy = tuple(chosen_state["x"].values()) + tuple(chosen_state["y"].values())
            pen.hideturtle()
            pen.pu()
            pen.goto(chosen_state_xy)
            pen.write(answer_state)

