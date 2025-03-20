from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.xpos=pos
        self.shape('square')
        self.shapesize(stretch_len=5)
        self.penup()
        self.color('white')
        self.goto(x=self.xpos,y=0)
        self.left(90)

    def up(self):
        if self.ycor()<225:
            self.forward(20)

    def down(self):
        if self.ycor()>-225:
            self.back(20)