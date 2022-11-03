# This is a game to practice the use of "turtle". This module allows the developer
# create a graphical context to show stuff. In this case i'm gonna try to 
# re-create a classical old game called "pong". 

import turtle

window = turtle.Screen()
window.title("Pong! by @arielgv")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0

paddle_1= turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.color('white')
paddle_1.penup()
paddle_1.goto(-350,0)

paddle_2= turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.color('white')
paddle_2.penup()
paddle_2.goto(350,0)

ball= turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 4
ball.dy = -4

scoring = turtle.Turtle()
scoring.speed(0)
scoring.penup()
scoring.color("white")
scoring.hideturtle()
scoring.goto(0,250)
scoring.write("Player A: 0  Player B: 0 ", align="center", font=("Courier", 22, "normal"))



def paddle1up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle1down():
    y = paddle_1.ycor()
    y -=20
    paddle_1.sety(y)

def paddle2up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle2down():
    y = paddle_2.ycor()
    y -=20
    paddle_2.sety(y)



#Keyboard binding:
window.listen()
window.onkeypress(paddle1up,"w")
window.onkeypress(paddle1down, "s")
window.onkeypress(paddle2down,"j")
window.onkeypress(paddle2up,"u")

while True:
    window.update()
    #movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #creating up & down borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        scoring.clear()
        scoring.write("Player A: {}  Player B: {} ".format(score_a,score_b), align="center", font=("Courier", 22, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        scoring.clear()
        scoring.write("Player A: {}  Player B: {} ".format(score_a,score_b), align="center", font=("Courier", 22, "normal"))



    #creating pad bouncing

    if ball.xcor() > 340 and (ball.ycor()<paddle_2.ycor()+40 and ball.ycor()>paddle_2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and (ball.ycor()<paddle_1.ycor()+40 and ball.ycor()>paddle_1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1



    





