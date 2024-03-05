from turtle import Turtle
import win32api

paddle_locations = [-40,-20,0,20,40]


class Paddles(Turtle):

    def __init__(self,x_pos):
        super().__init__()
        self.paddle_speed = 2.7
        self.paddles = []
        for q in range(5):
            paddle = Turtle()
            paddle.shape("square")
            paddle.penup()
            paddle.speed("fastest")
            paddle.color("white")
            paddle.left(90)
            paddle.goto(x_pos,paddle_locations[q])
            self.paddles.append(paddle)

    def up(self):
        _,y = self.paddles[-1].position()
        if abs(y) < 380:
            for q in self.paddles:
                q.setheading(90)
                q.forward(self.paddle_speed)

    def down(self):
        _,y = self.paddles[0].position()
        if abs(y) < 380:
            for q in self.paddles:
                q.setheading(-90)
                q.forward(self.paddle_speed)

    def move_l(self):
        if win32api.GetKeyState(0x57) < 0:
            self.up()
        if win32api.GetKeyState(0x53) < 0:
            self.down()

    def move_r(self):
        if win32api.GetKeyState(0x26) < 0:
            self.up()
        if win32api.GetKeyState(0x28) < 0:
            self.down()



            
