import re
from turtle import Turtle, Screen, color
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a colour: ')
colours = ['purple', 'red', 'blue', 'green', 'orange']
all_turtles = []

count = 0
for turtle_index in range(0, 5):
  turtle = Turtle(shape='turtle')
  turtle.color(colours[turtle_index])
  turtle.pu()
  count += 100
  turtle.goto(-230, (-280 + count))
  all_turtles.append(turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      print(f"{turtle.pencolor()} won!")
      if turtle.pencolor() == user_bet:
        print("You won!")
      else:
        print("You lose!")
      is_race_on = False
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

screen.exitonclick()
