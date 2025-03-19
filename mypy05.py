import turtle
t=turtle.Pen()
t.speed(0)
author=turtle.textinput('作者','请输入你的名字')

facesize=150 #头部
eyesize=facesize/2  #眼球
eyeballsize=facesize/10 #眼珠

r=(100000%256)/255.0
g=(100%256)/255.0
b=(120%256)/255.0

#头
t.fillcolor(r,g,b)
t.begin_fill()
t.circle(facesize)
t.end_fill()
#左眼
t.penup()
t.goto(-70,160)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(eyesize)
t.end_fill()
#右眼
t.penup()
t.goto(70,160)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(eyesize)
t.end_fill()

t.penup()
t.goto(-30,220)
t.pendown()
t.dot(eyeballsize)

t.penup()
t.goto(30,220)
t.pendown()
t.dot(eyeballsize)


turtle.penup()
turtle.goto(20,-70)
turtle.pencolor('black')
turtle.write('粉色大眼怪',align='center',font=('楷体',45))

turtle.goto(200,-130)
turtle.write('小画家：'+author,align='center',font=('楷体',20))




