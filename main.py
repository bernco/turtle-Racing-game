from turtle import Turtle, Screen
import random

m_screen = Screen()

# to set up the screen resolution and title for the game
m_screen.setup(width=500, height=400)
m_screen.title("Bernco Turtle Racing")

# initiate the prompt for users to select which turtle color wins the race
user_bet = m_screen.textinput(title="Place your bet", prompt="Which turtle will win the race? red, "
                                                             "green, orange, purple, black, blue, grey?: ")

# list of colors for the turtles
turtle_colors = ["red", "green", "orange", "purple", "black", "blue", "grey"]

# list of y-axis positions for the turtles. The x position is the same for all since they all start at same x position
turtle_y_pos = [-150, -100, -50, 0, 50, 100, 150]

# only starts game when True
is_game_on = False

# empty list for our seven turtles
turtle_list = []

# designs the turtles and position them by looping through the color and position lists.
# Finally add new turtle instances to the turtle lists
for turtle in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(turtle_colors[turtle])
    new_turtle.goto(x=-230, y=turtle_y_pos[turtle])
    turtle_list.append(new_turtle)

# unless the user inserts a bet, don't start racing
if user_bet:
    is_game_on = True

# while there is an input from the user, race!
# Racing is via a random number generated for each turtle from 0 to 20 paces
while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_game_on = False
            if user_bet == turtle.pencolor():
                print(f"you won, the winning turtle is {turtle.pencolor()}")
            else:
                print(f"you lost the winning turtle is {turtle.pencolor()}")
        turtle_random_mov = random.randint(0, 20)
        turtle.forward(turtle_random_mov)

m_screen.exitonclick()
