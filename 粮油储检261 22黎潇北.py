import turtle as Sl

screen = Sl.Screen()
screen.title("粮油储检261 22黎潇北 第5周作业")
screen.setup(1920, 1080)

pen = Sl.Turtle()
pen.shape("turtle")
pen.pensize(3)
pen.speed(3)

pen.circle(150)

pen.penup()
pen.goto(-35, 120)
pen.pendown()
pen.circle(25)

pen.penup()
pen.goto(35, 120)
pen.pendown()
pen.circle(15)

pen.penup()
pen.goto(40, 70)
pen.setheading(90)
pen.pendown()
pen.circle(40, 180)

pen.hideturtle()
screen.update()

from scipy import integrate
