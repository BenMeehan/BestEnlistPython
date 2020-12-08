import turtle


def mov_left_up():
    y = timmy1.ycor()
    y += 20
    timmy1.sety(y)


def mov_left_down():
    y = timmy1.ycor()
    y -= 20
    timmy1.sety(y)


def mov_right_up():
    y = timmy2.ycor()
    y += 20
    timmy2.sety(y)


def mov_right_down():
    y = timmy2.ycor()
    y -= 20
    timmy2.sety(y)


screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgcolor('black')

timmy1 = turtle.Turtle()
timmy1.speed(0)
timmy1.shape('square')
timmy1.color('white')
timmy1.shapesize(3, 1)
timmy1.penup()
timmy1.goto(-450, 0)

timmy2 = turtle.Turtle()
timmy2.speed(0)
timmy2.shape('square')
timmy2.color('white')
timmy2.shapesize(3, 1)
timmy2.penup()
timmy2.goto(450, 0)

timmy_ball = turtle.Turtle()
timmy_ball.shape('circle')
timmy_ball.color('white')
timmy_ball.penup()
timmy_ball.goto(0, 0)
timmy_ball.dx = 6
timmy_ball.dy = -6
timmy_ball.speed(50)

timmy_score = turtle.Turtle()
timmy_score.speed(0)
timmy_score.color("yellow")
timmy_score.penup()
timmy_score.hideturtle()
timmy_score.goto(0, 250)
timmy_score.write("Left player : 0    Right player: 0",
                  align="center", font=("Helvetica", 20, "normal"))

screen.listen()
screen.onkeypress(mov_left_up, 's')
screen.onkeypress(mov_left_down, 'a')
screen.onkeypress(mov_right_up, 'Up')
screen.onkeypress(mov_right_down, 'Down')

left, right = 0, 0

while True:
    screen.update()
    timmy_ball.setx(timmy_ball.xcor()+timmy_ball.dx)
    timmy_ball.sety(timmy_ball.ycor()+timmy_ball.dy)

    if timmy_ball.ycor() <= -280:
        timmy_ball.sety(-280)
        timmy_ball.dy *= -1
    if timmy_ball.ycor() >= 280:
        timmy_ball.sety(280)
        timmy_ball.dy *= -1

    if timmy_ball.xcor() >= 500:
        timmy_ball.goto(0, 0)
        timmy_ball.dy *= -1
        left += 1
        timmy_score.clear()
        timmy_score.write(f"Left player : {left}    Right player: {right}", align="center",
                          font=("helvetica", 20, "normal"))
    if timmy_ball.xcor() <= -500:
        timmy_ball.goto(0, 0)
        timmy_ball.dy *= -1
        right += 1
        timmy_score.clear()
        timmy_score.write(f"Left player : {left}    Right player: {right}", align="center",
                          font=("helvetica", 20, "normal"))

    if (timmy_ball.xcor() > 430 and timmy_ball.xcor() < 450) and (timmy_ball.ycor() < timmy2.ycor()+40 and timmy_ball.ycor() > timmy2.ycor()-40):
        timmy_ball.setx(430)
        timmy_ball.dx *= -1
    if (timmy_ball.xcor() < -430 and timmy_ball.xcor() > -450) and (timmy_ball.ycor() < timmy1.ycor()+40 and timmy_ball.ycor() > timmy1.ycor()-40):
        timmy_ball.setx(-430)
        timmy_ball.dx *= -1


screen.exitonclick()
