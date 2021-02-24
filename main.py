import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(key="Up", fun=player.up)
game_is_on = True
while game_is_on:
    time.sleep(car_manager.speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.final_score()
    if player.ycor() >= 280:
        scoreboard.calculate_score()
        car_manager.increase_speed()
        player.goto(0, -280)

screen.exitonclick()