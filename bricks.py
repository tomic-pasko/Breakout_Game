from turtle import Turtle


class Bricks(Turtle):
    bricks = []

    def __init__(self, position, colour):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(colour)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setposition(position)

        Bricks.bricks.append(self)

