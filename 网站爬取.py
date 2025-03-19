#开始
import os.path
import random
import sys
import  time

import pygame
from pygame import  mixer
from mukuai import *
from can import *

#初始化
pygame.init()
mixer.init()
yinyue=r'C:\Users\Administrator\Desktop\had\dylanf - 卡农 (经典钢琴版).mp3'

#建屏幕
screen = pygame.display.set_mode((1000, 600))            #屏幕

#颜色参数
black=0,0,0
white= '#F8F8FF'
red='#FF0000'
orange='#FFA500'

#导入图片
tian_kong=pygame.image.load("tian.jpeg").convert()
add,cdd=tian_kong.get_size()
tian_kong=pygame.transform.smoothscale(tian_kong, (add, cdd * 1.5))

fang_zi=pygame.image.load("小时候房间.jpg").convert()
ss,cs=fang_zi.get_size()
fang_zi=pygame.transform.smoothscale(fang_zi,(ss*1.3, cs * 1.3))
white= '#F8F8FF'

#建立字幕
a=abc('你呱呱坠落到世界上',40,white)
d=abc('你开始对一切感到陌生',40,white)
b=abc('你开始长大',40,white)
c=abc('后来，你决定...',40,white)


#建立菜单信息


time_nian=0
time_yue=0
time_ri=1


old=str(time_nian)+'岁'

number=0

#条件


#music
mixer.music.load(yinyue)

#初始位置
pos_x=0
pos_y=0

#随机属性
zhishi=random.randint(50,150)
jiajing=random.randint(1,500)
qingshang=random.randint(1,150)
yueli=random.randint(1,150)
tinen=random.randint(1,150)
xinqing=random.randint(100,200)



anniu_xue = Button(screen, 100, 500, 40, '学习')
anniu_yue = Button(screen, 250, 500, 40, '乐器')
anniu_kan = Button(screen, 400, 500, 40, '看电视 ')
anniu_duan = Button(screen, 550, 500, 40, '锻炼')
anniu_wai = Button(screen, 700, 500, 40, '外出')
anniu_caidan = Button(screen, 850, 500, 40, '菜单')


anniu_shang = Button(screen, 100, 500, 30, '商店')
anniu_zhengfu = Button(screen, 250, 500, 30, '政府')
anniu_shimao = Button(screen, 400, 500, 30, '商贸市场 ')
anniu_gopiao = Button(screen, 550, 500, 30, '股票市场')
anniu_dagong = Button(screen, 700, 500, 30, '打工')
anniu_huijia = Button(screen, 850, 500, 30, '回家')

anniu_mai_1 = Button(screen, 100, 500, 30, '卖东西')
anniu_mai_2 = Button(screen, 250, 500, 30, '买东西')

anniu_qin = Button(screen, 100, 500, 30, '钢琴 ')
anniu_shu = Button(screen, 250, 500, 30, '百科全书')
anniu_you = Button(screen, 400, 500, 30, '游戏机')
anniu_ya = Button(screen, 550, 500, 30, '哑铃')

anniu_huijia_1= Button(screen, 850, 500, 30, '回家')
anniu_huijia_2= Button(screen, 850, 500, 30, '回家')
anniu_huan_1=Button(screen,100,500,30,"100资金")
anniu_huan_2=Button(screen,250,500,30,'1000资金')
anniu_huan_3=Button(screen,400,500,30,'10000资金')
money_now = 0
while True:
    # 属性建立

    money_str = "资金:" + str(money_now)

    money_z = abc(money_str, 35, orange)
    time_str = str(time_nian) + '年' + str(time_yue) + '月' + str(time_ri) + '日'
    time_now = abc(time_str, 35, orange)
    old_now = abc(old, 35, orange)



    zhishi_str_1 = '你的基础知识为(最高150):' + str(zhishi)
    jiajing_str_1 = '你的基础家境为(最高500):' + str(jiajing)
    qingshang_str_1 = '你的基础情商为(最高150):' + str(qingshang)
    yueli_str_1 = '你的基础乐理为(最高150):' + str(yueli)
    tinen_1 = '你的基础体能为(最高150):' + str(tinen)
    xinqing_1 = '你的心情为:' + str(xinqing)

    zhishi_str_2 = '知识:' + str(zhishi)
    qingshang_str_2 = '情商:' + str(qingshang)
    yueli_str_2 = '乐理:' + str(yueli)
    xinqing_2 = '心情:' + str(xinqing)
    tinen_2 = '体能:' + str(tinen)


    zhishi_str_3 = abc(zhishi_str_2, 35, orange)
    qingshang_str_3 = abc(qingshang_str_2, 35, orange)
    yueli_str_3 = abc(yueli_str_2, 35, orange)
    tinen_3 = abc(tinen_2, 35, orange)
    xinqing_3 = abc(xinqing_2, 35, orange)
    #music

    def ditushuxing():
        screen.blit(money_z, (350, 30))
        screen.blit(old_now, (250, 30))
        screen.blit(time_now, (20, 30))

        screen.blit(yueli_str_3, (20, 150))
        screen.blit(qingshang_str_3, (200, 150))
        screen.blit(zhishi_str_3, (430, 150))
        screen.blit(xinqing_3, (610, 150))
        screen.blit(tinen_3, (800, 150))

    if mixer.music.get_busy()==False:
        mixer.music.play()


    #屏幕
    if tiao_zimu:
        screen.blit(tian_kong,(0,0))

    #时间逻辑
    if time_ri/12==1:
        time_ri=0
        time_yue+=1
    if time_yue/12==1:
        time_yue=0
        time_nian+=1





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                number+=1


        if event.type == pygame.MOUSEBUTTONDOWN:

            pos_x, pos_y = pygame.mouse.get_pos()

    if number==3:
        tiao_zimu=False

    if number==0 and tiao_zimu:
        screen.blit(a, (200, 200))

    if number==1 and tiao_zimu:
        screen.blit(b, (200, 200))
        screen.blit(d,(200,300))


    if number==2 and tiao_zimu:
        screen.blit(c,(350,50))
        bcd(screen,jiajing_str_1,(30,200))
        bcd(screen, zhishi_str_1, (30, 300))
        bcd(screen, qingshang_str_1, (30, 400))
        bcd(screen, yueli_str_1, (500, 200))
        bcd(screen,xinqing_1,(500,300))
        bcd(screen,tinen_1,(500,400))


    if number>=3 and ditu_1:


        screen.blit(fang_zi,(0,0))

        ditushuxing()



        anniu_jian(anniu_wai)
        anniu_jian(anniu_xue)
        anniu_jian(anniu_yue)
        anniu_jian(anniu_kan)
        anniu_jian(anniu_duan)
        anniu_jian(anniu_caidan)


        #学习的事件
        if anniu_xue.peng(pos_x,pos_y) or f_xue :
            screen.blit(tian_kong, (0, 0))
            if tiao_2:
                xue_sui=random.randint(1,11)
                tiao_2=False


            if xue_sui>5:
                bcd(screen, '你很累但很充实的过了一天', (50, 300))
                bcd(screen, '知识＋2', (50, 200))
                bcd(screen, '心情-1', (50, 100))
            else :
                bcd(screen, '你心不在焉的学了一天', (50, 300))
                bcd(screen, '知识+1', (50, 200))
                bcd(screen, '心情-1', (50, 100))

            if anniu_xue.peng(pos_x,pos_y):
                f_xue=True

            else:
                if xue_sui>5:
                    zhishi+=2
                    xinqing-=1
                else:
                    zhishi+=1
                    xinqing-=1
                time_ri+=1
                print(zhishi)
                f_xue=False
                tiao_2=True




        #乐理的事件
        if  anniu_yue.peng(pos_x,pos_y) or f_yueli :
            screen.blit(tian_kong, (0, 0))
            if jiajing>500:
                bcd(screen,'你很喜欢妈妈给你买的钢琴' , (50, 300))
                bcd(screen, '乐理＋3', (50, 200))

            if jiajing<250:
                bcd(screen,'没有什么好的乐器' , (50, 300))
                bcd(screen, '乐理＋1', (50, 200))

            if 250<=jiajing<500:
                bcd(screen,'妈妈心情好给你买了几本书',(50, 300))
                bcd(screen, '乐理＋2', (50, 200))

            if anniu_yue.peng(pos_x,pos_y):
                f_yueli=True

            else:
                if jiajing < 250:
                    yueli=yueli+1

                elif 500>=jiajing>=250:
                    yueli+=2
                else:
                    yueli+=3

                time_ri+=1
                f_yueli=False


        #看电视
        if  anniu_kan.peng(pos_x,pos_y) or f_kan:
            screen.blit(tian_kong, (0, 0))
            if tiao_kan:
                kan_sui=random.randint(1,11)
                tiao_kan=False


            if kan_sui>5:
                bcd(screen, '你发现你看都看不懂', (50, 300))
                bcd(screen, '情商＋1', (50, 200))
                bcd(screen, '心情＋1', (50, 100))
            else :
                bcd(screen, '你好像懂了些什么', (50, 300))
                bcd(screen, '情商＋2', (50, 200))
                bcd(screen, '心情＋2', (50, 100))

            if anniu_kan.peng(pos_x,pos_y):
                f_kan=True

            else:
                if kan_sui>5:
                    qingshang+=1
                    xinqing+=1
                else:
                    qingshang+=2
                    xinqing+=2
                time_ri+=1
                f_kan=False
                tiao_kan=True

        #锻炼
        if  anniu_duan.peng(pos_x,pos_y) or f_duan :
            screen.blit(tian_kong, (0, 0))
            if tiao_duan:
                duan_sui=random.randint(1,11)
                tiao_duan=False


            if duan_sui>5:
                bcd(screen, '你觉得你这小身板练不出什么', (50, 300))
                bcd(screen, '体能＋2', (50, 200))
                bcd(screen, '心情-1', (50, 100))
            else :
                bcd(screen, '你觉得你可以打倒一头牛', (50, 300))
                bcd(screen, '体能＋3', (50, 200))
                bcd(screen, '心情-1', (50, 100))

            if anniu_duan.peng(pos_x,pos_y):
                f_duan=True

            else:
                if duan_sui>5:
                    tinen+=2
                    xinqing-=1
                else:
                    tinen+=3
                    xinqing-=1
                time_ri+=1
                f_duan=False
                tiao_duan=True

    #外出参数

        if  anniu_wai.peng(pos_x,pos_y) :
            ditu_1 = False
            ditu_2=True
            pos_x=0
            pos_y=0



    ############################################################################################################################


    if ditu_2:

        screen.blit(jiedao, (0, 0))
        ditushuxing()

        anniu_jian(anniu_shang)
        anniu_jian(anniu_shimao)
        anniu_jian(anniu_zhengfu)
        anniu_jian(anniu_gopiao)
        anniu_jian(anniu_dagong)
        anniu_jian(anniu_huijia)

        if anniu_dagong.peng(pos_x,pos_y) or dagong_1:

            screen.blit(tian_kong,(0,0))

            if time_nian<18:
                bcd(screen,'你还太小，只能做家务',(200,200))
                bcd(screen, '妈妈给了你10块钱', (200, 400))

            else:
                bcd(screen, '感觉要累死了', (200, 200))
                bcd(screen, '老板给了你100块钱', (200, 400))

            if anniu_dagong.peng(pos_x,pos_y):


                dagong_1=True
            else:
                if  time_nian<18:
                    money_now+=10
                else:
                    money_now+=100
                dagong_1=False

        if anniu_shang.peng(pos_x,pos_y):

            ditu_1 = False
            ditu_2 = False
            ditu_3 = True
            pos_x = 0
            pos_y = 0

    if  ditu_3:
        screen.blit(shangdian, (0, 0))

        anniu_jian(anniu_mai_2)
        anniu_jian(anniu_mai_1)
        anniu_jian(anniu_huijia_1)


        if anniu_mai_2.peng(pos_x,pos_y) :
            ditu_2 = False
            ditu_3 = False
            ditu_1 =False
            ditu_4 = True
            di_1=True
            pos_x = 0
            pos_y = 0

        if anniu_mai_1.peng(pos_x, pos_y):
            ditu_2 = False
            ditu_3 = False
            ditu_1 = False
            ditu_4 = True
            di_2=True
            pos_x = 0
            pos_y = 0

    if ditu_4 :
        screen.blit(shangdian,(0,0))








        if di_1:
            anniu_jian(anniu_shu)
            anniu_jian(anniu_you)
            anniu_jian(anniu_qin)
            anniu_jian(anniu_ya)
            anniu_jian(anniu_huijia_2)

        if di_2:
            bcd(screen,'你的家境为:'+str(jiajing),(100,200),40,red)
            bcd(screen, '1 家境= 10资金',  (500, 200), 40, red)
            anniu_jian(anniu_huan_1)
            anniu_jian(anniu_huan_2)
            anniu_jian(anniu_huan_3)

            screen.blit(money_z, (350, 30))
            anniu_jian(anniu_huijia_2)

            if anniu_huan_1.peng(pos_x,pos_y):
                if jiajing//10>=1 and t_1:

                    jiajing=jiajing-10
                    money_now=money_now+100
                    t_1=False

            if anniu_huan_2.peng(pos_x,pos_y):
                if jiajing//100>=1 and t_2:

                    jiajing=jiajing-100
                    money_now=money_now+1000
                    t_2=False

            if anniu_huan_3.peng(pos_x,pos_y):
                if jiajing//1000>=1 and t_3:

                    jiajing=jiajing-1000
                    money_now=money_now+10000
                    t_3=False

    if anniu_huijia_1.peng(pos_x,pos_y):
        ditu_3 =False
        ditu_2 = True
        t_1=True
        t_2 = True
        t_3 = True
    if anniu_huijia_2.peng(pos_x,pos_y):
        ditu_4=False
        ditu_3 =False
        ditu_2 =False
        ditu_1=True
        t_1 = True
        t_2 = True
        t_3 = True
    if anniu_huijia.peng(pos_x, pos_y):
        ditu_3=False
        ditu_2 = False
        ditu_1 = True
        t_1 = True
        t_2 = True
        t_3 = True
    pygame.display.update()