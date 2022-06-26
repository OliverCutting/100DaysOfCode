from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.pu()
    self.goto(0, 280)
    self.hideturtle()
    self.color('white')
    self.score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score = {self.score}", align='center', font=('Arial', 16))

  def gain_point(self):
    self.score += 1
    self.update_scoreboard()

  def game_over(self):
    self.goto(0,0)
    self.write(f"GAME OVER", align='center', font=('Arial', 24))