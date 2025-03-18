from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(x=0,y=0)
        self.x_move=12
        self.y_move=random.randint(-10,10)
    def change_direction(self):
        self.y_move*=-1

    def collision(self):
        self.x_move*=-1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)