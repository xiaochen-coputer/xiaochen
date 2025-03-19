import turtle
t=turtle.Turtle()
t.speed(0)
t.color('green','red')
t.pencolor('orange')
t.fillcolor('yellow')
angle=360
n  =   int(turtle.textinput('绘制正多边形','请输入边数:'))
t.begin_fill()
for i in range(20):
    for j in range(n):
        t.forward(100)
        t.left(angle/n)
    t.left(18)
t.end_fill()
t.hideturtle()
