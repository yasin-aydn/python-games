from turtle import Turtle
from random import choice
import math


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_speed = 2
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.angles = list(i for i in range(360) if i < 30 or 150 < i < 210 or 330 < i)
        self.launch()
        

    def launch(self):
        self.goto(0,0)
        self.chosen_angle = choice(self.angles)
        self.angle = math.radians(self.chosen_angle)
        self.cosrate = math.cos(self.angle)
        self.sinrate = math.sin(self.angle)

    def move(self):
        x,y = self.position()
        if abs(y) > 380:
            self.sinrate *= -1
        self.goto(x + self.ball_speed*self.cosrate,y + self.ball_speed*self.sinrate)






        

