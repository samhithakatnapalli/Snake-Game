from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write("Game Over", align="center", font=("Courier", 15, "bold"))