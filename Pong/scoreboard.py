from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score=0
        self.player2_score=0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed(0)
        self.goto(x=0,y=250)
        self.write(f"Left: {self.player1_score}  Right: {self.player2_score}",align='center',font=('courier',24,'bold'))
        
    def increase_score(self,index):
        if index==1:
            self.player1_score+=1
        elif index==2:
            self.player2_score+=1
        self.clear()
        self.write(f"Left: {self.player1_score}  Right: {self.player2_score}", align='center',
                   font=('courier', 24, 'bold'))
    def winner(self):
        self.goto(x=0,y=0)
        if self.player1_score==10:
            self.write("Player 1 wins", align='center',
                       font=('courier', 24, 'bold'))
        else:
            self.write("Player 2 wins", align='center',
                       font=('courier', 24, 'bold'))
