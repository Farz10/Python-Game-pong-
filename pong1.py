#Simple python game for beginners

import turtle
import time
import winsound

wn = turtle.Screen()
wn.title("Pong by fz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #sets automatic window updation off
              #inturn speed up the game a bit

#Paddle A
paddle_a = turtle.Turtle() #(module.Class format--objectoriented))
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #default 20*20
paddle_a.penup() #avoid lining by turtle while they move
paddle_a.goto(-350, 0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball

ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen (turtle)
pen = turtle.Turtle()
pen.speed(0) #animation speed
pen.color("yellow")
pen.penup()
pen.hideturtle() #else a pen(like arrow) in yellow on screen will be diplayed
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center", font=("Times New Roman",24,"normal"))

#score
score_a = 0
score_b = 0


#Functions

def pad_a_up():
    y = paddle_a.ycor() #object.returnycoordinate using turtle mod
    y += 20
    paddle_a.sety(y)
def pad_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def pad_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def pad_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(pad_a_up,"w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")



# Main game loop
while True:
    wn.update()
    time.sleep(1 / 100) #time lapse to control ball speed



    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boarder checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction of ball
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Left and right
    if ball.xcor() > 350:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear() #so that score dont overwrite on currrent score, but clear and print
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Times New Roman", 24, "normal"))

    elif ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "normal"))


    # paddle and ball collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

