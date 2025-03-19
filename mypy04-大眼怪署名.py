import turtle
t=turtle.Pen()

author=turtle.textinput('作者','请输入你的名字')
#头
t.fillcolor('pink')
t.begin_fill()
t.circle(150)
t.end_fill()
#左眼
t.penup()
t.goto(-70,160)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(70)
t.end_fill()
#右眼
t.penup()
t.goto(70,160)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(70)
t.end_fill()

t.penup()
t.goto(-30,220)
t.pendown()
t.dot(30)

t.penup()
t.goto(30,220)
t.pendown()
t.dot(30)


turtle.penup()
turtle.goto(20,-70)
turtle.pencolor('black')
turtle.write('粉色大眼怪',align='center',font=('楷体',45))

turtle.goto(200,-130)
turtle.write('小画家：'+author,align='center',font=('楷体',20))
