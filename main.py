from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("Pong")

screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    line = Line((0,0))
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce_vert()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_hori()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_hori()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()



screen.exitonclick()
