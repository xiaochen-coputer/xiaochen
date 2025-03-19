import turtle
t=turtle.Turtle()
t.speed(8)

t.circle(150)

#左边眼睛
t.penup()
t.goto(-70,220)
t.pendown()
t.forward(50)


#右边眼睛
t.penup()
t.goto(70,220)
t.pendown()
t.forward(50)

#嘴巴
t.penup()
t.goto(40,70)
t.pendown()
t.circle(50)

