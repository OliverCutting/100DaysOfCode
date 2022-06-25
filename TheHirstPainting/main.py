from turtle import *
import random

colorslist = [(253, 253, 241), (236, 250, 243), (188, 19, 46), (243, 232, 66), (251, 230, 236), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173)]
colormode(255)

turtle = Turtle()
turtle.speed('fastest')
size_of_grid = 10

def draw_row():
  for _ in range(size_of_grid):
    turtle.dot(35, random.choice(colorslist))
    turtle.fd(70)
    turtle.dot(35, random.choice(colorslist))

def turn_right():
  turtle.right(90)
  turtle.fd(70)
  turtle.right(90)

def turn_left():
  turtle.left(90)
  turtle.fd(70)
  turtle.left(90)

turtle.pu()
turtle.setpos(-350, -350)

for _ in range(int(size_of_grid)):
  draw_row()
  turn_left()
  draw_row()
  turn_right()

screen = Screen()
screen.exitonclick