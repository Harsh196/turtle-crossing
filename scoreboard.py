from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def calculate_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!! Final score: {self.score}", align="center", font=FONT)
