import turtle
import winsound
#def f(start):
 #   turtle.fd(50)
  #  turtle.lt(60)
wn = turtle.Screen()
wn.title("pong by @imroz0512")
wn.bgpic("ny.gif")
#wn.setworldcoordinates(0.1,0.5,-0.1,-0.5) 
#wn.onkey(f,"up")
#wn.listen()
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(2)
paddle_a.shape("square")
paddle_a.color("skyblue")
paddle_a.shapesize(stretch_wid=7, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(2)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=7, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("greenYellow")
ball.shapesize(1,1,3)
#ball.shearfactor(-0.5)
#ball.shapetransform(1,0.1,0.2,1) 
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy =-0.3

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")
pen.pensize(2)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Comic Sans MS", 24, "bold"))

#function
def paddle_a_up():
    y= paddle_a.ycor()
    y += 30
    paddle_a.sety(y)


def paddle_a_down():
    y= paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)
    

def paddle_b_up():
    y= paddle_b.ycor()
    y += 30
    paddle_b.sety(y)



def paddle_b_down():
    y= paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"a")
wn.onkeypress(paddle_a_down,"w")
wn.onkeypress(paddle_b_up,"k")
wn.onkeypress(paddle_b_down,"i")


#main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wave",winsound.SND_FILENAME|winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wave",winsound.SND_FILENAME|winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=  1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "bold"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "bold"))    

    #Boder chacking for paddle
    if paddle_a.ycor() > 240:
        paddle_a.goto(-350,220)

    if paddle_a.ycor() < -230:
        paddle_a.goto(-350,-210)

    if paddle_b.ycor() > 240:
        paddle_b.goto(350,220)

    if paddle_b.ycor() < -230:
        paddle_b.goto(350,-210)        

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and  ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wave",winsound.SND_FILENAME|winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and  ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wave",winsound.SND_FILENAME|winsound.SND_ASYNC)

