from turtle import Turtle

class Texts(Turtle):

    def __init__(self):
        self.right_score = 0
        self.left_score = 0
        super().__init__()
        self.color("gray")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.width(3)

    def create_line(self):
        self.goto(0,375)
        self.right(90)
        for q in range(19):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def scoreboard(self):
        self.goto(0,280)
        self.write(f"{self.left_score}  {self.right_score}", False, align="center",font=('Arial', 80, 'normal'))

    def refresh(self):
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}", False, align="center",font=('Arial', 80, 'normal'))

    def check(self):
        if self.right_score == 7:
            return "Right"
        elif self.left_score == 7:
            return "Left"
        else:
            return False
    
    def winner(self,player):
        self.write(f"{player} has won the game!", False, align="center",font=('Arial', 80, 'normal'))
