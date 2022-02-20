from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.move_turtle()
        self.destination = 1

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.destination += 1








