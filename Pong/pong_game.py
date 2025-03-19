import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor('black')
my_screen.title("Pong")
my_screen.tracer(0,0)
my_screen.listen()
player1=Paddle(350)
player2=Paddle(-350)
ball=Ball()
my_board=ScoreBoard()

my_screen.onkey(key='Up',fun=player1.up)
my_screen.onkey(key='Down',fun=player1.down)
my_screen.onkey(key='w',fun=player2.up)
my_screen.onkey(key='s',fun=player2.down)

is_game_on=True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.change_direction()
    elif ball.distance(player1)<50 and ball.xcor()>320:
        ball.collision()
    elif ball.distance(player2)<50 and ball.xcor()<-320:
        ball.collision()
    elif ball.xcor()>350:
        my_board.increase_score(1)
        ball.reposition()
    elif ball.xcor()<-350:
        my_board.increase_score(2)
        ball.reposition()
    if my_board.player1_score==10 or my_board.player2_score==10:
        break
    ball.move()
my_board.winner()

my_screen.exitonclick()
