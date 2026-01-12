import time
from gameover import GameOver
from score import Score
from food import Food
from snake import Snake
from turtle import Screen

screen = Screen()

def start_game():
    snake = Snake()
    food = Food()
    scoreboard = Score()

    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()
        # checking for food eaten by using distance method in turtle
        if snake.head_of_snake.distance(food) < 14:
            food.refresh_position()
            snake.extend_snake()
            scoreboard.increase_score()

        #collision detection with walls
        if snake.head_of_snake.xcor() > 280 or snake.head_of_snake.xcor() < -280 or snake.head_of_snake.ycor() > 280 or snake.head_of_snake.ycor() < -280:
            GameOver()
            screen.update()
            time.sleep(2)
            is_game_on = False

        #collsion with self
        for square in snake.squares[1:]:
            if snake.head_of_snake.distance(square) < 10:
                GameOver()
                screen.update()
                time.sleep(2)
                is_game_on = False

play_again = True
while play_again:
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    if screen.textinput("Game start?", "Do you want to start the game?").lower() == "yes":
        start_game()
    else:
        play_again = False

screen.exitonclick()