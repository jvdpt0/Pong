import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')

paddle1 = Paddle((-350,0))
paddle2 = Paddle((350,0))
ball = Ball()


screen.listen()
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle2.up, 'w')
screen.onkey(paddle2.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 385:
        ball.set_center()
        
    if ball.xcor() < -385:
        ball.set_center()
screen.exitonclick()