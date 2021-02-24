from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.speed = 0.1
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.cars.append(new_car)

    def move_car(self):
        for i in range(len(self.cars)):
            random_speed = random.randint(5, 15)
            self.cars[i].forward(random_speed)

    def increase_speed(self):
        self.speed *= 0.6
