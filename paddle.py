from turtle import Turtle

WIDTH = 600

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.setposition(position)

    def move_left(self):
        # Move left until you hit the left wall
        if self.xcor() > - WIDTH / 2 + 50:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def move_right(self):
        # Move right until you hit the right wall
        if self.xcor() < WIDTH / 2 - 60:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
