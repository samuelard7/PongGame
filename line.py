from turtle import Turtle

class Line(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.2)
        self.penup()
        self.goto(position)