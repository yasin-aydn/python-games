from turtle import Screen
from ball import Ball
from paddles import Paddles
from texts import Texts
import win32api
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
ball.launch()

bracket_l = Paddles(700)
bracket_r = Paddles(-700)

line = Texts()
winner = Texts()
score = Texts()

line.create_line()
score.scoreboard()

right_bracket = True
left_bracket = True

start_time = time.time()

while True:

    ball.move()

    screen.update()

    bracket_l.move_r()

    bracket_r.move_l()

    if abs(ball.xcor()) > 300:
        if right_bracket:
            for q in bracket_r.paddles:
                if ball.distance(q) < 18:
                    ball.cosrate *= -1
                    ball.ball_speed += 0.4
                    right_bracket = False
                    left_bracket = True
                    break

        if left_bracket:
            for q in bracket_l.paddles:
                if ball.distance(q) < 18:
                    ball.cosrate *= -1
                    ball.ball_speed += 0.4
                    right_bracket = True
                    left_bracket = False
                    break

    if abs(ball.xcor()) > 780:
        if ball.xcor() > 0:
            score.left_score += 1
        else:
            score.right_score += 1
        score.refresh()
        if score.check():
            winner.winner(score.check())
            break
        screen.update()
        time.sleep(2)
        ball.ball_speed = 2
        ball.launch()

    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 0.005:
        time.sleep(0.005 - elapsed_time)
    start_time = time.time()
