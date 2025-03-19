import turtle



score_system={'萧骏佑':369,'何周攀':200,'沈煜嘉':0}
#主循环while，退出循环命令：breakwhile true:
while True:
    name=turtle.textinput('查分系统','请输入查询人的名字(退出请输入Q):')
    if score_system.get(name):
            s='姓名'+name+'分数:'+str(score_system.get(name))
            print(s)
    #退出循环
    elif name=="Q"or name=="Q":
        break
    else:
        print("查无此学生，请重新输入!")
