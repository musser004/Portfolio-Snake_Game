from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initial screen setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initial snake/food/scoreboard setup

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Setting up user controls, and their corresponding snake movement methods

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Loop condition and core gameplay loop. Screen updates, sleeps 1/8 second, and moves snake forward in current direction

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.12)
    snake.move()

    # Detecting collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.point()

    # Detecting collision with walls

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False

    # Detecting collision with head and tail segments of snake

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

# After the gameplay loop completes, scoreboard update/game over screen. Then, screen will close from user mouse click

scoreboard.end()
scoreboard.game_over()
screen.exitonclick()
