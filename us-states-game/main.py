import time
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
draw_turtle = turtle.Turtle()
draw_turtle.hideturtle()
draw_turtle.penup()
data = pandas.read_csv("50_states.csv", index_col=False)
guessed_states = []
missing_states = []
game_is_on = True
all_states = data.state.to_list()
score = {}
while len(guessed_states) < 50:
    time.sleep(0.6)
    prompt = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Type the name of a state").title()
    data_row = data[data.state == prompt].reset_index()
    if prompt == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]
        break
    else:
        x_cor = data_row.x
        y_cor = data_row.y
        draw_turtle.goto(x_cor[0], y_cor[0])
        draw_turtle.write(prompt)
        guessed_states.append(prompt)


states_left = {"missing_states": missing_states, }
pandas.DataFrame(states_left).to_csv("user_score.csv")