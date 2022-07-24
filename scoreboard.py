from turtle import Turtle
WIDTH = 400

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, WIDTH/2 - 35)
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -WIDTH / 4)
        self.write('GAME OVER', align='center', font=('Courier', 30, 'normal'))