from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

starting_pos = [(0, 0),(-20, 0),(-40, 0)]

snake = Snake()
food = Food()
score = Scoreboard()
high_score = 0


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
segments = []
is_game_on = True

while is_game_on:
	screen.update()
	time.sleep(0.1)
	#collision with food
	snake.move()
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		score.increase_score()
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
		score.reset()
		snake.reset()

		# collision with tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()


screen.exitonclick()
