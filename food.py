from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed(0)
        self.refresh_position()

    def refresh_position(self):
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x,rand_y)
