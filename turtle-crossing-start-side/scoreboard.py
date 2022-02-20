FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.level = Turtle()
        self.level.penup()
        self.level.goto(x=100, y=250)
        self.level.hideturtle()


    def update(self, score):
        self.level.clear()
        self.level.write(f"LEVEL: {score}", font=FONT)


    def game_over(self):
        game_sign = Turtle()
        game_sign.write("Game Over", font=FONT, align="center")
        game_sign.penup()
        game_sign.hideturtle()




