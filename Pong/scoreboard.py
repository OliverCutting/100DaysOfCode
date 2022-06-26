from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.r_paddle = 0
    self.l_paddle = 0
    self.pu()
    self.hideturtle()
    self.color('white')
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-100, 200)
    self.write(f"{self.l_paddle}", align='center', font=('Arial', 80))
    self.goto(100, 200)
    self.write(f"{self.r_paddle}", align='center', font=('Arial', 80))

  def r_gain_point(self):
    self.r_paddle += 1
    self.update_scoreboard()

  def l_gain_point(self):
    self.l_paddle += 1
    self.update_scoreboard()