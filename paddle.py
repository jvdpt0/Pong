from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(UP)
        self.goto(position)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len = 5)
        self.penup()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)
