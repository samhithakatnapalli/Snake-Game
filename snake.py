from turtle import Turtle
positions = [(0,0),(-20,0),(-40,0)]
moving_distance = 20

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head_of_snake = self.squares[0]

    def create_snake(self):
        for position in positions:
            self.add_squares(position)

    def add_squares(self,position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def extend_snake(self):
        self.add_squares(self.squares[-1].position())

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)

        self.head_of_snake.forward(moving_distance)

    def up(self):
        if self.head_of_snake.heading() != 270:
            self.head_of_snake.setheading(90)
    def down(self):
        if self.head_of_snake.heading() != 90:
            self.head_of_snake.setheading(270)
    def left(self):
        if self.head_of_snake.heading() != 0:
            self.head_of_snake.setheading(180)
    def right(self):
        if self.head_of_snake.heading() != 180:
            self.head_of_snake.setheading(0)

