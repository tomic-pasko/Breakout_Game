import time
from turtle import *
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard

game_is_on = True
amount = 30
WIDTH = 600
HEIGHT = 400

screen = Screen()
screen.title("Breakout Game")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.tracer(0)

pad = Paddle((0, -150))
ball = Ball()

score = Scoreboard()

# Bricks
rows = 4
columns = 10
brick_colors = ['blue', 'green', 'red', 'yellow']


x1 = -WIDTH/2 + 50
y1 = HEIGHT/2 - 50

# Grid of Bricks
for i in range(1, rows+1):
    for j in range(1, columns+2):
        Bricks((x1, y1), brick_colors[i-1])
        x1 += (WIDTH-100)/10
    x1 = -WIDTH/2 + 50
    y1 -= 30


screen.onkeypress(pad.move_left, 'Left')
screen.onkeypress(pad.move_right, 'Right')


screen.listen()


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with paddle

    if ball.distance(pad) < 30 and ball.ycor() < -120:
        ball.bounce_y()

    # Detect collision with left and right walls

    if ball.xcor() > WIDTH/2 - 25 or ball.xcor() < -WIDTH/2 + 25:
        ball.bounce_x()

    # Detect collision with upper wall

    if ball.ycor() > HEIGHT/2 - 25:
        ball.bounce_y()

    # Detect collision with brick

    for br in Bricks.bricks:
        if ball.distance(br) < 30:

            # Bounce from left/right side of brick
            if abs(ball.ycor()-br.ycor()) <= 10:
                ball.bounce_x()

            # Bounce from up/down side of brick
            else:
                ball.bounce_y()

            br.reset()
            score.point()

    # Detect ball passing the paddle
    if ball.ycor() < -200:
        game_is_on = False
        score.game_over()

screen.exitonclick()
