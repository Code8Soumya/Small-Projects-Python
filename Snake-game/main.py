from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 600, height= 600)
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up" )
screen.onkey(snake.down, "Down" )
screen.onkey(snake.right, "Right" )
screen.onkey(snake.left, "Left" )

game_on = True

while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.incscore()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_on = False
        score.game_over()

    for val in range(1, len(snake.segments) ):
        if snake.segments[0].distance(snake.segments[val]) < 10:
            game_on = False
            score.game_over()




screen.exitonclick()