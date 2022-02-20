from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.score = 1

    def new_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE + (self.score - 1) * MOVE_INCREMENT)





