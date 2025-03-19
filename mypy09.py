import turtle


while True:
    text=turtle.textinput('爬山','往上爬')
    if text=='我累了'or text=='到达山顶':
        print(text+'休息')
        break
    else:
        print('继续爬吧......')
