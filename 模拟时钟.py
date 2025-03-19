import turtle
from datetime import datetime


def getWeek(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]

def getDate(t):
    y = t.year
    m = t.month
    d = t.day
    return f'{y} {m} {d} '

def getTime(t):
    h = int(t.hour)
    m = int(t.minute)
    s = int(t.second)
    return h, m, s

# 跳跃，不留痕迹移动
def skip(pen, step):
    pen.pu()
    pen.fd(step)
    pen.pd()

# 画表盘
def drawClock():
    turtle.pensize(7)
    turtle.ht()
    for i in range(60):
        skip(turtle, 100)
        if i % 5 == 0:
            turtle.fd(-10)
            skip(turtle, -90)
        else:
            turtle.dot(5)
            skip(turtle, -100)
        turtle.right(6)


def show():
    t.clear()
    now = datetime.now()
    t.goto(0,-70)
    t.write(f' { getDate(now)}\n   {getWeek(now)}', 
            align='center',
            font=('1', 10, 'bold'))
    h, m, s = getTime(now)
    
    hhand.clear()
    mhand.clear()
    shand.clear()
    hhand.seth(90)
    mhand.seth(90)
    shand.seth(90)
    hhand.right(h*30+m*0.5)
    hhand.fd(40)
    skip(hhand, -40)
    mhand.right(m*6+s*0.1)
    mhand.fd(50)
    skip(mhand, -50)
    shand.right(s*6)
    shand.fd(60)
    skip(shand, -60)

def tick():
    show()
    window.ontimer(tick,1000)

t = turtle.Turtle()
window = turtle.Screen()
t.pu()
t.ht()
turtle.tracer(0)
drawClock()

# 设置时分秒针的画笔
hhand = turtle.Turtle()
mhand = turtle.Turtle()
shand = turtle.Turtle()
hhand.ht()
mhand.ht()
shand.ht()
hhand.pensize(5)
mhand.pensize(3)

tick()
turtle.done()
