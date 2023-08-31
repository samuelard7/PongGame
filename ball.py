from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(0.88)
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        x_axis = self.xcor() + self.x
        y_axis = self.ycor() + self.y
        self.goto(x_axis, y_axis)

    def bounce_vert(self):
        self.y *= -1

    def bounce_hori(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_hori()
        self.move_speed = 0.1
