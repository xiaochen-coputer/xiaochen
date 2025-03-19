import random
import sys

import pygame
from pygame import mixer
from can import *
from mukuai import *



# 初始化
pygame.init()
mixer.init()
yinyue = r'dylanf - 卡农 (经典钢琴版).mp3'

# 建屏幕
screen = pygame.display.set_mode((1000, 600))  # 屏幕

# 颜色参数
black = 0, 0, 0
white = '#F8F8FF'
red = '#FF0000'
orange = '#FFA500'

# 导入图片
tian_kong = pygame.image.load("tian.jpeg").convert()

def tu(tupian,c,k):
    add, cdd = tupian.get_size()
    tupian = pygame.transform.smoothscale(tupian, (add*c, cdd * k))
    return tupian
tian_kong=tu(tian_kong,1,1.5)

# 开始
fang_zi = pygame.image.load("客厅.jpg").convert()
ss, cs = fang_zi.get_size()
fang_zi = pygame.transform.smoothscale(fang_zi, (ss * 1.1, cs * 1.1))
white = '#F8F8FF'

# 建立字幕
a = abc('你呱呱坠落到世界上（按空格以继续）', 50, white)
d = abc('你开始对一切感到陌生', 50, white)
b = abc('你开始长大', 50, white)
c = abc('后来，你决定...', 50, white)

# 建立菜单信息


time_nian = 0
time_yue = 0
time_ri = 1

old = str(time_nian) + '岁'

number = 0

# 条件


# music
mixer.music.load(yinyue)

# 初始位置
pos_x = 0
pos_y = 0

money_now = 0


a_1='小熊布偶 '
a_2='天趣科技 '
a_3='宝娃子不锈钢'
a_4='豪爵摩托 '
a_5='开罗'
a_6='旭升传媒'
a_7='川东水泥 '
a_8='民生医院'
a_9='繁华街市'
a_10='泽川工厂'

# 随机属性
zhishi = random.randint(50, 150)
jiajing = random.randint(1, 1000)
qingshang = random.randint(1, 150)
yueli = random.randint(1, 150)
tinen = random.randint(1, 150)
xinqing = random.randint(100, 200)

anniu_huijia_3 = Button(screen, 850, 500, 40, '回家')
anniu_xue = Button(screen, 100, 500, 40, '学习')


anniu_yue = Button(screen, 250, 500, 40, '乐器')
anniu_kan = Button(screen, 400, 500, 40, '看电视 ')
anniu_duan = Button(screen, 550, 500, 40, '锻炼')
anniu_wai = Button(screen, 700, 500, 40, '外出')
anniu_caidan = Button(screen, 850, 500, 40, '任务')

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

anniu_huijia_1 = Button(screen, 850, 500, 30, '回家')
anniu_huijia_2 = Button(screen, 850, 500, 30, '回家')
anniu_huan_1 = Button(screen, 100, 500, 30, "100资金")
anniu_huan_2 = Button(screen, 250, 500, 30, '1000资金')
anniu_huan_3 = Button(screen, 400, 500, 30, '10000资金')
anniu_huan_4 = Button(screen, 550, 500, 30, '10家境')
anniu_huan_5 = Button(screen, 700, 500, 30, '100家境')



anniu_ji_xu= Button(screen, 100, 500, 30, '继续')
anniu_shoushu=Button(screen,500,400,30,"手术")


anniu_ji_gou= Button(screen, 100, 500, 30, '购买')
anniu_ji_fan= Button(screen, 500, 500, 30, '返回')
anniu_ji_mai= Button(screen,400,500,30,"卖出")
anniu_ji_yijian_m = Button(screen,250,500,30,"一键买入")
anniu_ji_yijian_m2 = Button(screen,700,500,30,"一键卖出")




anniu_ji_xuexiao=Button(screen,800,100,30,'学校')
anniu_ji_xuexiao_shi=Button(screen,100,500,30,'食堂')
anniu_ji_xuexiao_su1=Button(screen,250,500,30,'宿舍(男)')
anniu_ji_xuexiao_su2=Button(screen,400,500,30,'宿舍(女)')
anniu_ji_xuexiao_zou=Button(screen,550,500,30,'走廊')
anniu_ji_jiaoshi=Button(screen,700,500,30,'教室')
anniu_ji_kaoshi_1=Button(screen,800,100,30,'考试')
anniu_ji_kaoshi=Button(screen,800,100,30,'考试')

anniu_ji_zizhu=Button(screen,100,500,30,'自主创业')
anniu_ji_shougou=Button(screen,250,500,30,'收购')
anniu_ji_geren=Button(screen,400,500,30,'个人情况')
anniu_ji_paimai=Button(screen,550,500,30,'拍卖会')
anniu_ji_guanli=Button(screen,700,500,30,'公司管理')
anniu_ji_shougou_1=Button(screen,800,100,30,'收购')

anniu_ji_fu=Button(screen,100,500,30,'服装公司')
anniu_ji_youxi=Button(screen,250,500,30,'游戏公司')
anniu_ji_meishi=Button(screen,400,500,30,'美食公司')
anniu_ji_kongtiao=Button(screen,550,500,30,'空调公司')
anniu_ji_hulian=Button(screen,700,500,30,'互联网公司')

anniu_ji_xiang=Button(screen,800,100,30,'详细')
annniu_ji_guyong1=Button(screen,100,500,30,'雇佣')
annniu_ji_guyong2=Button(screen,250,500,30,'解雇')
annniu_ji_kuoz=Button(screen,400,500,30,'扩张')
anniu_ji_chu=Button(screen,550,500,30,'出售')
anniu_ji_yiyuan=Button(screen,100,300,30,'医院')


fu=500000
fu_1=50000
youxi=1000000
youxi_1=80000
meishi=2000000
meishi_1=100000
kongtiao=5000000
kongtiao_1=200000
hulian=10000000
hulian_1=500000



anniu_ji_a= Button(screen, 100, 50, 30, a_1)
anniu_ji_b= Button(screen, 100, 150, 30, a_2)
anniu_ji_c= Button(screen, 100, 250, 30, a_3)
anniu_ji_d= Button(screen, 100, 350, 30, a_4)
anniu_ji_e= Button(screen, 100, 450, 30, a_5)
anniu_ji_f= Button(screen, 500, 50, 30, a_6)
anniu_ji_g= Button(screen, 500, 150, 30, a_7)
anniu_ji_h= Button(screen, 500, 250, 30, a_8)
anniu_ji_i= Button(screen, 500, 350, 30, a_9)
anniu_ji_j= Button(screen, 500, 450, 30, a_10)











gupiao_tu = pygame.image.load('股票.jpg')
gupiao_tu=tu(gupiao_tu,1.2,1.2)

sui_a = random.randint(255, 500)
sui_b = random.randint(250, 600)
sui_c = random.randint(800, 1000)
sui_d = random.randint(200, 400)
sui_e = random.randint(100, 300)
sui_f = random.randint(100, 200)
sui_g = random.randint(100, 700)
sui_h = random.randint(300, 600)
sui_i = random.randint(499, 1000)
sui_j= random.randint (11, 300)
sui_k = random.randint(256, 500)
sui_l = random.randint(1, 400)
sui_m = random.randint(134, 420)

gu_a=0
gu_b=0
gu_c=0
gu_d=0
gu_e=0
gu_f=0
gu_g=0
gu_h=0
gu_i=0
gu_j=0



icon=pygame.image.load("a.jpeg")
money_now=0
while True:
    pygame.display.set_caption('人生模拟器')
    pygame.display.set_icon(icon)
    # 属性建立
    key=pygame.key.get_pressed()
    if money_now>10000:
        money_str = "资金:" + str(money_now//10000)+'w'
    else:
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


    # music

    def ditushuxing():

        screen.blit(money_z, (350, 30))
        screen.blit(old_now, (250, 30))
        screen.blit(time_now, (20, 30))

        screen.blit(yueli_str_3, (20, 150))
        screen.blit(qingshang_str_3, (200, 150))
        screen.blit(zhishi_str_3, (430, 150))
        screen.blit(xinqing_3, (610, 150))
        screen.blit(tinen_3, (800, 150))


    if mixer.music.get_busy() == False:
        mixer.music.play()

    # 屏幕
    if tiao_zimu:
        screen.blit(tian_kong, (0, 0))

    # 时间逻辑
    if time_ri / 13 >= 1:
        if time_nian<=3:
            jiajing-=10
        if 3<=time_nian:
            money_now-=money_fu
            money_fu+=5000*bili-money_fu
            life-=50
            bili+=0.2
        time_ri = 1
        time_yue += 1
        if t_kong==False:
            money_now+=kongtiao_1
        if t_fu==False:
            money_now+=fu_1
        if t_meishi==False:
            money_now+=meishi_1
        if t_hulain==False:
            money_now+=hulian_1
        if t_youxi==False:
            money_now+=youxi_1

        sui_a = random.randint(500, 1000)
        sui_b = random.randint(2000, 2500)
        sui_c = random.randint(100, 600)
        sui_d = random.randint(200, 400)
        sui_e = random.randint(120, 300)
        sui_f = random.randint(30, 50)
        sui_g = random.randint(20, 45)
        sui_h = random.randint(100, 500)
        sui_i = random.randint(498, 500)
        sui_j= random.randint (123, 300)
        sui_k = random.randint(145, 400)
        sui_l = random.randint(590, 1000)
        sui_m = random.randint(100, 5008)


    if time_yue / 13 == 1:
        time_yue = 1
        time_nian += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                number += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()

    if number == 3:
        tiao_zimu = False

    if number == 0 and tiao_zimu:
        screen.blit(a, (200, 200))
        pos_x = 0
        pos_y = 0
    if number == 1 and tiao_zimu:
        screen.blit(b, (200, 200))
        screen.blit(d, (200, 300))
        pos_x = 0
        pos_y = 0
    if number == 2 and tiao_zimu:
        screen.blit(c, (350, 50))
        bcd(screen, jiajing_str_1, (30, 200))
        bcd(screen, zhishi_str_1, (30, 300))
        bcd(screen, qingshang_str_1, (30, 400))
        bcd(screen, yueli_str_1, (500, 200))
        bcd(screen, xinqing_1, (500, 300))
        bcd(screen, tinen_1, (500, 400))
        pos_x = 0
        pos_y = 0
    if number >= 3 and ditu_1:

        screen.blit(fang_zi, (0, 0))

        ditushuxing()

        anniu_jian(anniu_wai)
        anniu_jian(anniu_xue)
        anniu_jian(anniu_yue)
        anniu_jian(anniu_kan)
        anniu_jian(anniu_duan)
        anniu_jian(anniu_caidan)
#############################################################################################################
        # 学习的事件
        if anniu_xue.peng(pos_x, pos_y) or f_xue:
            screen.blit(tian_kong, (0, 0))

            if sui_1 > 5:
                bcd(screen, '你很累但很充实的过了一天', (50, 300))
                bcd(screen, '知识++', (50, 200))
                bcd(screen, '心情-', (50, 100))
            else:
                bcd(screen, '你心不在焉的学了一天', (50, 300))
                bcd(screen, '知识+', (50, 200))
                bcd(screen, '心情-', (50, 100))

            if anniu_xue.peng(pos_x, pos_y):
                f_xue = True

            else:
                if sui_1 > 5:
                    zhishi += xiao_xue_2
                    xinqing -= 1
                else:
                    zhishi += xiao_xue_1
                    xinqing -= 1

                time_ri += 1
                sui_1 = random.randint(1, 11)
                pos_x = 0
                pos_y = 0
                print(zhishi)
                f_xue = False


        # 乐理的事件
        if anniu_yue.peng(pos_x, pos_y) or f_yueli:
            screen.blit(tian_kong, (0, 0))
            if jiajing > 500:
                bcd(screen, '你很喜欢这首曲子', (50, 300))
                bcd(screen, '乐理++', (50, 200))

            if jiajing < 250:
                bcd(screen, '没有什么好的乐器', (50, 300))
                bcd(screen, '乐理+', (50, 200))

            if 250 <= jiajing < 500:
                bcd(screen, '妈妈心情好给你买了几本书', (50, 300))
                bcd(screen, '乐理++', (50, 200))

            if xiao_yu_2>3:
                bcd(screen, '你太喜欢这架钢琴了', (50, 300))
                bcd(screen, '乐理+++', (50, 200))

            if anniu_yue.peng(pos_x, pos_y):
                f_yueli = True

            else:
                if jiajing < 250:
                    yueli = yueli + xiao_yu_1

                elif 500 >= jiajing >= 250:
                    yueli += xiao_yu_2
                else:
                    yueli += xiao_yu_2

                sui_1 = random.randint(1, 11)
                time_ri += 1
                pos_x = 0
                pos_y = 0
                f_yueli = False


        # 看电视
        if anniu_kan.peng(pos_x, pos_y) or f_kan:
            screen.blit(tian_kong, (0, 0))

            if sui_1 > 5:
                bcd(screen, '你发现你看都看不懂', (50, 300))
                bcd(screen, '情商＋', (50, 200))
                bcd(screen, '心情＋', (50, 100))
            else:
                bcd(screen, '你好像懂了些什么', (50, 300))
                bcd(screen, '情商 ++', (50, 200))
                bcd(screen, '心情+', (50, 100))

            if anniu_kan.peng(pos_x, pos_y):
                f_kan = True

            else:
                if sui_1 > 5:
                    qingshang += xiao_qing_1
                    xinqing += 1
                else:
                    qingshang += xiao_qing_2
                    xinqing += 2
                time_ri += 1
                sui_1 = random.randint(1, 11)
                pos_x = 0
                pos_y = 0

                f_kan = False


        # 锻炼
        if anniu_duan.peng(pos_x, pos_y) or f_duan:
            screen.blit(tian_kong, (0, 0))

            if sui_1 > 5:
                bcd(screen, '你觉得你这小身板练不出什么', (50, 300))
                bcd(screen, '体能＋', (50, 200))
                bcd(screen, '心情-', (50, 100))
            else:
                bcd(screen, '你觉得你可以打倒一头牛', (50, 300))
                bcd(screen, '体能++', (50, 200))
                bcd(screen, '心情-', (50, 100))

            if anniu_duan.peng(pos_x, pos_y):
                f_duan = True

            else:
                if sui_1 > 5:
                    tinen += xiao_duan_2
                    xinqing -= 1
                else:
                    tinen += xiao_duan_1
                    xinqing -= 1
                time_ri += 2
                sui_1 = random.randint(1, 11)
                pos_x = 0
                pos_y = 0
                f_duan = False

        if  anniu_caidan.peng(pos_x, pos_y) or caidan_f:
            screen.blit(tian_kong,(0,0))
            if time_nian<3:
                screen.blit(tian_kong,(0,0))
                bcd(screen,'你的任务为：',(50,50),40,red)
                bcd(screen, '撑过3岁,上幼儿园', (150, 150), 40, red)
                bcd(screen, '建议多学习，幼儿园毕业考好小学', (150, 250), 40, red)
                bcd(screen, '家境每月 -10', (150, 350), 40, red)
                bcd(screen, '父母死了每月1200生活费也没了喔', (150, 450), 40, red)
            if time_nian >= 3:
                screen.blit(tian_kong, (0, 0))
                bcd(screen, '你的任务为：', (50, 50), 40, red)
                bcd(screen, '多学习', (150, 150), 40, red)
                bcd(screen, '多赚钱', (150, 250), 40, red)
                bcd(screen, '家境每月 -1000', (150, 350), 40, red)
                bcd(screen, '别让家人死了喔', (150, 450), 40, red)

            if anniu_caidan.peng(pos_x, pos_y):
                caidan_f = True

            else:
                caidan_f = False
                pos_x = 0
                pos_y = 0















        # 外出参数

        if anniu_wai.peng(pos_x, pos_y):
            ditu_1 = False
            ditu_2 = True
            pos_x = 0
            pos_y = 0

    ############################################################################################################################

    if ditu_2:


        screen.blit(jiedao, (0, 0))
        ditushuxing()
        anniu_jian(anniu_ji_yiyuan)
        anniu_jian(anniu_shang)
        anniu_jian(anniu_shimao)
        anniu_jian(anniu_zhengfu)
        anniu_jian(anniu_gopiao)
        anniu_jian(anniu_dagong)
        anniu_jian(anniu_huijia)
        if time_nian >=3 and t_kaoshi:
            anniu_jian(anniu_ji_kaoshi)
            if anniu_ji_kaoshi.peng(pos_x, pos_y) or f_kao:
                T_kao_1 = False
                screen.blit(tian_kong, (0, 0))
                bcd(screen, '语文' + str(yu), (100, 200), 40, orange)
                bcd(screen, '数学' + str(shu), (500, 200), 40, orange)
                bcd(screen, '体育' + str(ti), (100, 300), 40, orange)
                bcd(screen, '总分' + str(zong), (300, 400), 40, red)
                if anniu_ji_kaoshi.peng(pos_x, pos_y):
                    f_kao = True
                else:
                    f_kao = False
                    t_kaoshi = False
                    pos_x = 0
                    pos_y = 0

            if  T_kao_1:
                if zhishi>200:
                    shu=random.randint(90,100)
                    yu=random.randint(90,100)
                elif 200>zhishi>100:
                    shu=random.randint(60,80)
                    yu=random.randint(60,80)
                else:
                    shu = random.randint(0, 60)
                    yu = random.randint(0, 60)

                if tinen>200:
                    ti=random.randint(90,100)
                elif 200>tinen>100:
                    ti=random.randint(60, 80)
                else:
                    ti = random.randint(0, 60)

                zong=ti+shu+yu



        if t_kaoshi==False:
            anniu_jian(anniu_ji_xuexiao)

        if anniu_ji_xuexiao.peng(pos_x, pos_y):
            ditu_2=False
            ditu_6=True
            pos_x=0
            pos_y=0



        if anniu_huijia.peng(pos_x, pos_y):
            pos_x = 0
            pos_y = 0
            ditu_5 = False
            di_1 = False
            di_2 = False
            pp=True
            yiyuan_1=False

            ditu_4 = False
            ditu_3 = False
            ditu_2 = False
            ditu_1 = True

        if anniu_ji_yiyuan.peng(pos_x,pos_y) or yiyuan_1:
            yiyuan_1=True
            pp=False
            screen.blit(tian_kong, (0, 0))
            anniu_jian(anniu_huijia)
            if time_nian<3:
                bcd(screen,"你父亲的状况： 良好",(100,100),40,red)
                bcd(screen, "生命 :1000", (100, 250), 40, red)
                bcd(screen, "每月费用:无", (100, 100), 40, red)
            if time_nian>=3:
                bcd(screen, "你父亲的状况：植物人", (100, 100), 40, red)
                bcd(screen, "生命 :"+str(life), (100, 200), 40, red)
                bcd(screen, "每月费用:"+str(money_fu), (100, 300), 40, red)
                bcd(screen, "手术费用:" + str(money_fu), (100, 400), 40,red)
                anniu_jian(anniu_shoushu)
                if anniu_shoushu.peng(pos_x,pos_y):
                    if money_now>money_fu:
                        money_now-=money_fu
                        if life<=1000 :
                            life+=100
                            if life>=1000:
                                life=1000


        if anniu_dagong.peng(pos_x, pos_y) or dagong_1:

            screen.blit(tian_kong, (0, 0))

            if time_nian < 18:
                if fumu_t:
                    bcd(screen, '你还太小，只能做家务', (200, 200))
                    bcd(screen, '妈妈给了你100块钱', (200, 300))
                else:
                    bcd(screen, '你还太小，只能做家务', (200, 200))
                    bcd(screen, '但是妈妈已经不在了  呜呜...', (200, 300))
                    bcd(screen, '乞讨到了几块钱', (200, 400))
            else:
                bcd(screen, '感觉要累死了', (200, 200),40)
                bcd(screen, '老板给了你100块钱', (200, 300),40)

            if anniu_dagong.peng(pos_x, pos_y):

                dagong_1 = True
            else:
                if time_nian < 18:
                    if fumu_t:
                        money_now += 100
                    else:
                        money_now+=sui_1
                else:
                    money_now += 1000
                pos_x = 0
                pos_y = 0
                time_ri+=12
                sui_1=random.randint(1,100)
                dagong_1 = False

        if anniu_shang.peng(pos_x, pos_y):
            ditu_1 = False
            ditu_2 = False
            ditu_3 = True
            pos_x = 0
            pos_y = 0

        if anniu_zhengfu.peng(pos_x,pos_y) or f_zhengfu:
            if time_nian < 18:
                screen.blit(tian_kong,(0,0))
                bcd(screen, '你未满18岁被赶出去了', (100, 200),40,orange)
                if anniu_zhengfu.peng(pos_x,pos_y):
                    f_zhengfu=True
                else:
                    pos_x = 0
                    pos_y = 0
                    time_ri+=1
                    f_zhengfu=False




        if anniu_shimao.peng(pos_x,pos_y) or f_shimao:

            if time_nian < 3:
                screen.blit(tian_kong,(0,0))
                bcd(screen, '你未满18岁被赶出去了', (100, 200),40,orange)
                if anniu_shimao.peng(pos_x, pos_y):
                    f_shimao = True
                else:
                    print(1)
                    pos_x = 0
                    pos_y = 0
                    time_ri+=1
                    f_shimao=False
            if anniu_shimao.peng(pos_x, pos_y):
                f_shimao = True
                if time_nian >= 3:
                    ditu_2=False
                    f_shimao_1=True
                    pos_x=0
                    pos_y=0





        if  anniu_gopiao.peng(pos_x, pos_y) :
            ditu_2 = False
            ditu_3 = False
            ditu_1 = False
            ditu_4 = False
            ditu_5 =True
            pos_x=0
            pos_y=0

    if f_shimao_1:
        if t_shimao_2:
            screen.blit(shimao,(0,0))
            anniu_jian(anniu_ji_geren)
            anniu_jian(anniu_ji_zizhu)
            anniu_jian(anniu_ji_paimai)
            anniu_jian(anniu_ji_shougou)
            anniu_jian(anniu_huijia_2)
            anniu_jian(anniu_ji_guanli)

        if anniu_ji_zizhu.peng(pos_x,pos_y) and t_shimao_3:
            t_shimao_2=False
            t_shimao_3=False
            f_shimao_a=True
            pos_x=0
            pos_y=0

        if anniu_ji_geren.peng(pos_x,pos_y) and t_shimao_3:
            t_shimao_2=False
            t_shimao_3=False
            f_shimao_b=True
            pos_x=0
            pos_y=0

        if anniu_ji_guanli.peng(pos_x,pos_y) and t_shimao_3:
            t_shimao_2=False
            t_shimao_3=False
            f_shimao_c=True
            pos_x=0
            pos_y=0









        if f_shimao_b:
            screen.blit(shimao,(0,0))
            if t_kong==False:
                you_1='空调公司'
                bcd(screen,you_1+'每月收益为:' +str(kongtiao_1), (300, 100),35,orange)
            if t_meishi==False:
                you_2='美食公司'
                bcd(screen, you_2+'每月收益为:'+str(meishi_1), (300, 200),35,orange)
            if t_hulain==False:
                you_3='互联网公司'
                bcd(screen, you_3+'每月收益为:' + str(hulian_1), (300, 300),35,orange)
            if t_youxi==False:
                you_4='游戏公司'
                bcd(screen, you_4+'每月收益为:' + str(youxi_1), (300, 400),35,orange)
            if t_fu==False:
                you_5='服装公司'
                bcd(screen, you_5+'每月收益为:' + str(fu_1), (300, 500),35,orange)
            anniu_jian(anniu_huijia_2)
            bcd(screen,'你有的公司为:',(350,30),35,red)
            bcd(screen, you_1, (100, 100), 35, orange)
            bcd(screen, you_2, (100, 200), 35, orange)
            bcd(screen, you_3, (100, 300), 35, orange)
            bcd(screen, you_4, (100, 400), 35, orange)
            bcd(screen, you_5, (100, 500), 35, orange)




        if f_shimao_a:
            if True:
                screen.blit(shimao, (0, 0))
                if t_shimao_6:
                    bcd(screen, '你自主创业的类型为:', (100, 200), 40, red)

                    if t_kong:
                        anniu_jian(anniu_ji_kongtiao)
                    if t_meishi:
                        anniu_jian(anniu_ji_meishi)
                    if t_hulain:
                        anniu_jian(anniu_ji_hulian)
                    if t_fu:
                        anniu_jian(anniu_ji_fu)
                    if t_youxi:
                        anniu_jian(anniu_ji_youxi)
                    anniu_jian(anniu_huijia_2)

                if t_kong:
                    if anniu_ji_kongtiao.peng(pos_x,pos_y) or f_shimao_4 :
                        t_shimao_6=False
                        f_shimao_4=True


                        anniu_jian(anniu_ji_shougou_1)
                        anniu_jian(anniu_huijia_2)
                        bcd(screen, '空调公司价格为:'+str(kongtiao//10000)+'w', (100, 100), 40, red)
                        bcd(screen, '你的资金为:' + str(money_now // 10000) + 'w', (100, 200), 40, red)
                        if anniu_ji_shougou_1.peng(pos_x,pos_y) and t_kong:
                            if money_now>=kongtiao:
                                money_now-=kongtiao
                                f_shimao_4=False
                                t_shimao_6=True
                                t_kong=False
                                pos_x = 0
                                pos_y = 0

                if t_meishi:
                    if anniu_ji_meishi.peng(pos_x,pos_y) or f_shimao_5 :
                        t_shimao_6=False
                        f_shimao_5=True


                        anniu_jian(anniu_ji_shougou_1)
                        anniu_jian(anniu_huijia_2)
                        bcd(screen, '美食公司价格为:'+str(meishi//10000)+'w', (100, 100), 40, red)
                        bcd(screen, '你的资金为:' + str(money_now // 10000) + 'w', (100, 200), 40, red)
                        if anniu_ji_shougou_1.peng(pos_x,pos_y) and t_meishi:
                            if money_now>=meishi:
                                money_now-=meishi
                                f_shimao_5=False

                                t_shimao_6=True
                                t_meishi=False
                                pos_x = 0
                                pos_y = 0

                if t_youxi:
                    if anniu_ji_youxi.peng(pos_x,pos_y) or f_shimao_6 :
                        t_shimao_6=False
                        f_shimao_6=True

                        anniu_jian(anniu_ji_shougou_1)
                        anniu_jian(anniu_huijia_2)
                        bcd(screen, '游戏公司价格为:'+str(youxi//10000)+'w', (100, 100), 40, red)
                        bcd(screen, '你的资金为:' + str(money_now // 10000) + 'w', (100, 200), 40, red)
                        if anniu_ji_shougou_1.peng(pos_x,pos_y) and t_youxi:
                            if money_now>=youxi:
                                money_now-=youxi
                                f_shimao_6=False

                                t_shimao_6=True
                                t_youxi=False
                                pos_x = 0
                                pos_y = 0

                if t_hulain:
                    if anniu_ji_hulian.peng(pos_x,pos_y) or f_shimao_7 :
                        print(1)
                        t_shimao_6=False
                        f_shimao_7=True

                        anniu_jian(anniu_ji_shougou_1)
                        anniu_jian(anniu_huijia_2)
                        bcd(screen, '互联网公司价格为:'+str(hulian//10000)+'w', (100, 100), 40, red)
                        bcd(screen, '你的资金为:' + str(money_now // 10000) + 'w', (100, 200), 40, red)
                        if anniu_ji_shougou_1.peng(pos_x,pos_y) and t_hulain:
                            if money_now>=hulian:
                                money_now-=hulian
                                f_shimao_7=False

                                t_shimao_6=True
                                t_hulain=False
                                pos_x = 0
                                pos_y = 0

                if t_fu:
                    if anniu_ji_fu.peng(pos_x,pos_y) or f_shimao_8 :
                        t_shimao_6=False
                        f_shimao_8=True

                        anniu_jian(anniu_ji_shougou_1)
                        anniu_jian(anniu_huijia_2)
                        bcd(screen, '服装公司价格为:'+str(fu//10000)+'w', (100, 100), 40, red)
                        bcd(screen, '你的资金为:' + str(money_now // 10000) + 'w', (100, 200), 40, red)
                        if anniu_ji_shougou_1.peng(pos_x,pos_y) and t_fu:
                            if money_now>=fu:
                                money_now-=fu
                                f_shimao_8=False

                                t_shimao_6=True
                                t_fu=False
                                pos_x = 0
                                pos_y = 0

        if f_shimao_c:

            if t_shimao_10:
                screen.blit(shimao, (0, 0))
                if t_kong == False:
                    anniu_jian(anniu_ji_kongtiao)
                if t_meishi == False:
                    anniu_jian(anniu_ji_meishi)
                if t_hulain == False:
                    anniu_jian(anniu_ji_hulian)
                if t_youxi == False:
                    anniu_jian(anniu_ji_youxi)
                if t_fu == False:
                    anniu_jian(anniu_ji_fu)
                anniu_jian(anniu_huijia_2)

                if anniu_ji_kongtiao.peng(pos_x, pos_y) :
                    f_as_1=True
                    pos_x=0
                    pos_y=0
                if anniu_ji_fu.peng(pos_x, pos_y) :
                    f_as_2=True
                    pos_x=0
                    pos_y=0
                if anniu_ji_youxi.peng(pos_x, pos_y) :
                    f_as_3=True
                    pos_x=0
                    pos_y=0
                if anniu_ji_hulian.peng(pos_x, pos_y) :
                    f_as_4=True
                    pos_x=0
                    pos_y=0
                if anniu_ji_meishi.peng(pos_x, pos_y):
                    f_as_5 = True
                    pos_x = 0
                    pos_y = 0

            if f_as_1:
                t_shimao_10 = False
                screen.blit(shimao,(0,0))
                bcd(screen, '空调公司每月收益为:' + str(kongtiao_1), (100, 100), 35, red)
                bcd(screen, '你要...', (100, 200), 35, red)
                bcd(screen,'在线员工为'+"最多("+str(x)+")个:"+str(yu_a),(100,300))
                bcd(screen, '规模为：' + str(d_1)+"  级", (100, 400))


                anniu_jian(anniu_ji_chu)
                anniu_jian(annniu_ji_guyong1)
                anniu_jian(annniu_ji_guyong2)
                anniu_jian(anniu_ji_xiang)
                anniu_jian(annniu_ji_kuoz)
                anniu_jian(anniu_huijia_2)

                if anniu_ji_chu.peng(pos_x, pos_y):
                    t_kong = True
                    money_now += kongtiao_1

                    f_hui=True

                if 1<=yu_a<=x:
                    if annniu_ji_guyong1.peng(pos_x, pos_y) :
                        yu_a+=1
                        money_now-=5000
                        mm = (yu_a // 1 - 1) * 500
                        kongtiao_1 += mm
                        pos_x = 0
                        pos_y = 0


                    if annniu_ji_guyong2.peng(pos_x, pos_y) :
                        yu_a-=1
                        money_now+=5000
                        mm = (yu_a // 1 - 1) * 500
                        kongtiao_1 += mm
                        pos_x = 0
                        pos_y = 0

                if x<10:
                    if annniu_ji_kuoz.peng(pos_x, pos_y) :
                        x=10
                        money_now-=200000
                        pos_x = 0
                        pos_y = 0


#################################################
            if f_as_2:
                t_shimao_10 = False
                screen.blit(shimao, (0, 0))
                bcd(screen, '服装公司每月收益为:' + str(fu_1), (100, 100), 35, red)
                bcd(screen, '你要...', (100, 200), 35, red)
                bcd(screen, '在线员工为:' + str(yu_b), (100, 300))


                anniu_jian(anniu_ji_chu)
                anniu_jian(annniu_ji_guyong1)
                anniu_jian(annniu_ji_guyong2)
                anniu_jian(anniu_ji_xiang)
                anniu_jian(annniu_ji_kuoz)
                anniu_jian(anniu_huijia_2)

                if anniu_ji_chu.peng(pos_x, pos_y):
                    t_fu = True
                    money_now += fu_1
                    f_hui = True

                if 0 < yu_b <= g:
                    if annniu_ji_guyong1.peng(pos_x, pos_y) :
                        yu_b += 1
                        money_now -= 5000
                        qq = (yu_b // 1 - 1) * 500
                        fu_1 += qq
                        pos_x=0
                        pos_y=0


                    if annniu_ji_guyong2.peng(pos_x, pos_y) :
                        yu_b -= 1
                        money_now += 5000
                        qq = (yu_b // 1 - 1) * 500
                        fu_1 += qq
                        pos_x = 0
                        pos_y = 0

            if g < 10:
                    if annniu_ji_kuoz.peng(pos_x, pos_y) :
                        g = 10
                        money_now -= 200000

                        pos_x = 0
                        pos_y = 0

            ############################################
            if f_as_3:
                t_shimao_10 = False
                screen.blit(shimao, (0, 0))
                bcd(screen, '游戏公司每月收益为:' + str(youxi_1), (100, 100), 35, red)
                bcd(screen, '你要...', (100, 200), 35, red)
                bcd(screen, '在线员工为' + "最多(" + str(q) + ")个:" + str(yu_c), (100, 300))
                bcd(screen, '规模为：' + str(d_3) + "  级", (100, 400))


                anniu_jian(anniu_ji_chu)
                anniu_jian(annniu_ji_guyong1)
                anniu_jian(annniu_ji_guyong2)
                anniu_jian(anniu_ji_xiang)
                anniu_jian(annniu_ji_kuoz)
                anniu_jian(anniu_huijia_2)


                if anniu_ji_chu.peng(pos_x, pos_y):
                    t_kong = True
                    money_now += youxi_1

                    f_hui = True

                if 0<= yu_c <= q:

                    if annniu_ji_guyong1.peng(pos_x, pos_y) :
                        yu_c += 1
                        money_now -= 5000
                        ii = (yu_c // 1 - 1) * 500
                        youxi_1 += ii
                        pos_x=0
                        pos_y=0

                    if annniu_ji_guyong2.peng(pos_x, pos_y) :
                        yu_c -= 1
                        money_now += 5000
                        ii = (yu_c // 1 - 1) * 500
                        youxi_1 += ii
                        pos_x = 0
                        pos_y = 0

                if q < 10:
                    if annniu_ji_kuoz.peng(pos_x, pos_y) :
                        q = 10
                        d_4+=1
                        money_now -= 100000
                        pos_x = 0
                        pos_y = 0


###################################################
            if f_as_4:
                t_shimao_10 = False
                screen.blit(shimao, (0, 0))
                bcd(screen, '互联网公司每月收益为:' + str(hulian_1), (100, 100), 35, red)
                bcd(screen, '你要...', (100, 200), 35, red)
                bcd(screen, '在线员工为' + "最多(" + str(w) + ")个:" + str(yu_d), (100, 300))
                bcd(screen, '规模为：' + str(d_4) + "  级", (100, 400))


                anniu_jian(anniu_ji_chu)
                anniu_jian(annniu_ji_guyong1)
                anniu_jian(annniu_ji_guyong2)
                anniu_jian(anniu_ji_xiang)
                anniu_jian(annniu_ji_kuoz)
                anniu_jian(anniu_huijia_2)
                t_bdbd = True
                if anniu_ji_chu.peng(pos_x, pos_y):
                    t_kong = True
                    money_now += hulian_1

                    f_hui = True

                if 0 < yu_d <= w:
                    if annniu_ji_guyong1.peng(pos_x, pos_y):
                        yu_d += 1
                        money_now -= 5000
                        oo = (yu_d // 1 - 1) * 500
                        kongtiao_1 += oo
                        pos_x = 0
                        pos_y = 0

                    if annniu_ji_guyong2.peng(pos_x, pos_y) :
                        yu_d -= 1
                        money_now += 5000
                        pos_x = 0
                        pos_y = 0

                if w< 10:
                    if annniu_ji_kuoz.peng(pos_x, pos_y) :
                        w = 10
                        money_now -= 200000

                        pos_x = 0
                        pos_y = 0

            if f_as_5:
                t_shimao_10 = False
                screen.blit(shimao, (0, 0))
                bcd(screen, '美食公司每月收益为:' + str(meishi_1), (100, 100), 35, red)
                bcd(screen, '你要...', (100, 200), 35, red)
                bcd(screen, '在线员工为' + "最多(" + str(e) + ")个:" + str(yu_e), (100, 300))
                bcd(screen, '规模为：' + str(d_5) + "  级", (100, 400))

                anniu_jian(anniu_ji_chu)
                anniu_jian(annniu_ji_guyong1)
                anniu_jian(annniu_ji_guyong2)
                anniu_jian(anniu_ji_xiang)
                anniu_jian(annniu_ji_kuoz)
                anniu_jian(anniu_huijia_2)
                t_bdbd = True
                if anniu_ji_chu.peng(pos_x, pos_y):
                    t_kong = True
                    money_now += meishi_1
                    f_as = False
                    f_hui = True

                if 0 < yu_e <= e:
                    if annniu_ji_guyong1.peng(pos_x, pos_y):
                        fu_e += 1
                        money_now -= 5000
                        eed = (yu_e // 1 - 1) * 500
                        kongtiao_1 += eed

                        pos_x = 0
                        pos_y = 0

                    if annniu_ji_guyong2.peng(pos_x, pos_y) :
                        fu_e -= 1
                        money_now += 5000
                        pos_x = 0
                        pos_y = 0

                if e < 10:
                    if annniu_ji_kuoz.peng(pos_x, pos_y) :
                        e = 10
                        money_now -= 200000

                        pos_x = 0
                        pos_y = 0
    if ditu_6:
        screen.blit(tian_kong,(0,0))
        if  t_xue:
            if 270 > zong > 180:
                che = '高等幼儿园'
            elif zong < 180:
                che = '初级幼儿园'
            else:
                che = '超级幼儿园'

            bcd(screen,'你幼儿园开学考试总分为:'+str(zong),(100,100),30,red)
            bcd(screen, '你考上的幼儿园为:' + che, (100, 200),30,red)
            bcd(screen, '开启你的学习之旅吧...', (100, 300), 30, red)

        if key[pygame.K_SPACE]:
            t_xue=False
            f_xue_1=True
        if f_xue_1:

            if f_shi:
                screen.blit(xuexiao,(0,0))
                ditushuxing()
                anniu_jian(anniu_ji_xuexiao_shi)
                anniu_jian(anniu_ji_xuexiao_su1)
                anniu_jian(anniu_ji_xuexiao_zou)
                anniu_jian(anniu_ji_xuexiao_su2)
                anniu_jian(anniu_ji_jiaoshi)
                anniu_jian(anniu_ji_kaoshi_1)
                anniu_jian(anniu_huijia_2)
                ditushuxing()

            if anniu_ji_jiaoshi.peng(pos_x,pos_y) or f_xue_2:
                f_shi=False

                screen.blit(jiaoshi,(0,0))
                bcd(screen,'愉快的学习了一天',(100,100),40,red)
                bcd(screen, '知识+5,乐理+5', (100, 200), 40, red)
                if anniu_ji_jiaoshi.peng(pos_x, pos_y):
                    f_xue_2=True
                    print('1')
                else:
                    pos_x = 0
                    pos_y = 0
                    zhishi+=5
                    yueli+=5
                    time_ri+=1
                    f_xue_2=False
                    f_shi=True

            if anniu_ji_xuexiao_shi.peng(pos_x, pos_y) or f_xue_3:
                f_shi = False
                screen.blit(shitang, (0, 0))

                bcd(screen, '吃了一顿不算美味的东西', (100, 100), 40, red)
                bcd(screen, '心情+10', (100, 200), 40, red)
                if anniu_ji_xuexiao_shi.peng(pos_x, pos_y):
                    f_xue_3 = True

                else:
                    f_xue_3 = False
                    f_shi = True
                    xinqing+=10
                    pos_x = 0
                    pos_y = 0
                    time_ri+=1

            if anniu_ji_xuexiao_zou.peng(pos_x, pos_y) or f_xue_4:

                f_shi = False
                screen.blit(zoulang_1, (0, 0))
                bcd(screen,'你并没有见到丁香一样的姑娘,你还太小', (100, 200), 40, red)
                if anniu_ji_xuexiao_zou.peng(pos_x, pos_y):
                    f_xue_4 = True


                else:
                    f_xue_4 = False
                    f_shi = True
                    time_ri+=1
                    pos_x = 0
                    pos_y = 0

            if anniu_ji_xuexiao_su1.peng(pos_x, pos_y) or f_xue_5:
                screen.blit(sushe, (0, 0))
                f_shi = False
                bcd(screen,'跟室友打了一架', (100, 200), 40, red)
                bcd(screen, '情商+5', (100, 200), 40, red)
                if anniu_ji_xuexiao_su1.peng(pos_x, pos_y):
                    f_xue_5 = True

                else:
                    f_xue_5 = False
                    f_shi = True
                    qingshang+=5
                    time_ri+=1
                    pos_x = 0
                    pos_y = 0

            if anniu_ji_xuexiao_su2.peng(pos_x, pos_y) or f_xue_6:
                screen.blit(tian_kong, (0, 0))
                f_shi = False
                bcd(screen, '你被赶了出去', (100, 200), 40, red)
                if anniu_ji_xuexiao_su2.peng(pos_x, pos_y):
                    f_xue_6 = True

                else:
                    f_xue_6 = False
                    f_shi = True
                    time_ri+=1
                    pos_x = 0
                    pos_y = 0

    if ditu_5:




        if t_99:


            screen.blit(gupiao_tu, (0, 0))

            bcd(screen, '小熊布偶  股价 : ' + str(sui_a), (50, 10), 30, white)
            bcd(screen, '天趣科技  股价 : ' + str(sui_b), (50, 80), 30, white)
            bcd(screen, '宝娃子不锈钢  股价 : ' + str(sui_c), (50, 160), 30, white)
            bcd(screen, '豪爵摩托  股价 : ' + str(sui_d), (50, 240), 30, white)
            bcd(screen, '开罗  股价 : ' + str(sui_e), (50, 320), 30, white)
            bcd(screen, '旭升传媒  股价 : ' + str(sui_f), (500, 10), 30, white)
            bcd(screen, '川东水泥  股价 : ' + str(sui_g), (500, 80), 30, white)
            bcd(screen, '民生医院  股价 : ' + str(sui_h), (500, 160), 30, white)
            bcd(screen, '繁华街市  股价 : ' + str(sui_i), (500, 240), 30, white)
            bcd(screen, '泽川工厂  股价 : ' + str(sui_j), (500, 320), 30, white)
            anniu_jian(anniu_ji_gou)
            anniu_jian(anniu_huijia)
            anniu_jian(anniu_ji_mai)
            anniu_jian(anniu_ji_yijian_m)
            anniu_jian(anniu_ji_yijian_m2)

            if anniu_huijia.peng(pos_x, pos_y):
                pos_x = 0
                pos_y = 0
                ditu_5 = False
                di_1 = False
                di_2 = False
                ditu_4 = False
                ditu_3 = False
                ditu_2 = False
                ditu_1 = True

        ######################################################购买############################################
        if anniu_ji_gou.peng(pos_x, pos_y) or f_100 or anniu_ji_yijian_m.peng(pos_x,pos_y) :
            screen.blit(gupiao_tu, (0, 0))
            t_99=False
            f_99=False
            f_30=False
            f_50=False
            if anniu_ji_gou.peng(pos_x, pos_y):
                f_100 = True
                t_99 = False

            if anniu_ji_yijian_m.peng(pos_x, pos_y):
                f_100 = True
                t_99 = False
                m=True
            anniu_jian(anniu_ji_a)
            anniu_jian(anniu_ji_b)
            anniu_jian(anniu_ji_c)
            anniu_jian(anniu_ji_d)
            anniu_jian(anniu_ji_e)
            anniu_jian(anniu_ji_f)
            anniu_jian(anniu_ji_g)
            anniu_jian(anniu_ji_h)
            anniu_jian(anniu_ji_i)
            anniu_jian(anniu_ji_j)
            bcd(screen, '持股 :' + str(gu_a), (250, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_b), (250, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_c), (250, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_d), (250, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_e), (250, 450), 30, white)
            bcd(screen, '持股 :' + str(gu_f), (700, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_g), (700, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_h), (700, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_i), (700, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_j), (700, 450), 30, white)


            anniu_jian(anniu_ji_a)
            anniu_jian(anniu_ji_b)
            anniu_jian(anniu_ji_c)
            anniu_jian(anniu_ji_d)
            anniu_jian(anniu_ji_e)
            anniu_jian(anniu_ji_f)
            anniu_jian(anniu_ji_g)
            anniu_jian(anniu_ji_h)
            anniu_jian(anniu_ji_i)
            anniu_jian(anniu_ji_j)
            bcd(screen, '持股 :' + str(gu_a), (250, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_b), (250, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_c), (250, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_d), (250, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_e), (250, 450), 30, white)
            bcd(screen, '持股 :' + str(gu_f), (700, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_g), (700, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_h), (700, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_i), (700, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_j), (700, 450), 30, white)



            anniu_jian(anniu_huijia_3)

            if anniu_ji_a.peng(pos_x,pos_y) or f_gu:
                f_gu=True
                if anniu_ji_a.peng(pos_x,pos_y):
                    if m:
                        shuliang= money_now//sui_a

                    if sui_a< money_now:


                        gu_a += shuliang


                        money_now -= sui_a*shuliang
                        shuliang=1
                        if m:
                            m=False

                    pos_x = 0
                    pos_y = 0

                    f_gu = False
            if anniu_ji_b.peng(pos_x,pos_y) or f_gu:

                f_gu = True
                if m:
                    shuliang = money_now // sui_b

                if sui_b < money_now:
                    gu_b += shuliang
                    money_now -= sui_b*shuliang
                    shuliang=1
                pos_x = 0
                pos_y = 0
                m=False
                f_gu = False

            if anniu_ji_c.peng(pos_x,pos_y) or f_gu:

                f_gu = True
                if m:
                    shuliang = money_now // sui_c
                m=False
                if sui_c < money_now:
                    gu_c += shuliang
                    money_now -= sui_c*shuliang
                shuliang=1
                pos_x = 0
                pos_y = 0
                m=False
                f_gu = False

            if anniu_ji_d.peng(pos_x,pos_y) or f_gu:

                f_gu = True

                if m:
                    shuliang = money_now // sui_d
                m = False
                if sui_d < money_now:
                    gu_d += shuliang
                    money_now -= sui_d * shuliang
                shuliang = 1
                pos_x = 0
                pos_y = 0
                f_gu = False

            if anniu_ji_e.peng(pos_x,pos_y) or f_gu:

                f_gu = True

                if m:
                    shuliang = money_now // sui_e
                m = False
                if sui_e < money_now:
                    gu_e += shuliang
                    money_now -= sui_e * shuliang
                shuliang = 1
                pos_x = 0
                pos_y = 0
                f_gu = False

            if anniu_ji_f.peng(pos_x,pos_y) or f_gu:

                f_gu = True

                if m:
                    shuliang = money_now // sui_f
                m = False
                if sui_f < money_now:
                    gu_f += shuliang
                    money_now -= sui_f * shuliang
                shuliang = 1
                pos_x = 0
                pos_y = 0
                f_gu = False

            if anniu_ji_g.peng(pos_x,pos_y) or f_gu:

                f_gu = True

                if m:
                    shuliang = money_now // sui_g
                m = False
                if sui_g < money_now:
                    gu_g += shuliang
                    money_now -= sui_g * shuliang
                shuliang = 1
                pos_x = 0
                pos_y = 0
                f_gu = False

            if anniu_ji_h.peng(pos_x,pos_y) or f_gu:

                f_gu = True

                if m:
                    shuliang = money_now // sui_h
                m = False
                if sui_h < money_now:
                    gu_h += shuliang
                    money_now -= sui_h * shuliang
                shuliang = 1
                pos_x = 0
                pos_y = 0
                f_gu = False

            if anniu_ji_j.peng(pos_x,pos_y) or f_gu:

                f_gu = True

                if m:
                    shuliang = money_now // sui_j
                m = False
                if sui_j < money_now:
                    gu_j += shuliang
                    money_now -= sui_j * shuliang
                shuliang = 1
                pos_x = 0
                pos_y = 0
                f_gu = False

            if anniu_ji_i.peng(pos_x,pos_y) or f_gu:

                f_gu = True

                if m:
                    shuliang = money_now // sui_i
                m = False
                if sui_i < money_now:
                    gu_i += shuliang
                    money_now -= sui_i * shuliang
                shuliang = 1
                pos_x = 0
                pos_y = 0
                f_gu = False



        ###############################################################################$$$$$$$$$$$$$$$$$$$$$$$$##############################
        if anniu_ji_yijian_m2.peng(pos_x,pos_y) or f_30 or anniu_ji_mai.peng(pos_x,pos_y):

            print('3')
            f_100=False
            f_99=False
            screen.blit(gupiao_tu, (0, 0))
            if anniu_ji_mai.peng(pos_x, pos_y):
                f_100=False
                m=False
                f_30 = True
                t_99 = False

            if anniu_ji_yijian_m2.peng(pos_x, pos_y):
                f_100=False
                m=True
                f_30 = True
                t_99 = False



            anniu_jian(anniu_ji_a)
            anniu_jian(anniu_ji_b)
            anniu_jian(anniu_ji_c)
            anniu_jian(anniu_ji_d)
            anniu_jian(anniu_ji_e)
            anniu_jian(anniu_ji_f)
            anniu_jian(anniu_ji_g)
            anniu_jian(anniu_ji_h)
            anniu_jian(anniu_ji_i)
            anniu_jian(anniu_ji_j)
            bcd(screen, '持股 :' + str(gu_a), (250, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_b), (250, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_c), (250, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_d), (250, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_e), (250, 450), 30, white)
            bcd(screen, '持股 :' + str(gu_f), (700, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_g), (700, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_h), (700, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_i), (700, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_j), (700, 450), 30, white)

            anniu_jian(anniu_ji_a)
            anniu_jian(anniu_ji_b)
            anniu_jian(anniu_ji_c)
            anniu_jian(anniu_ji_d)
            anniu_jian(anniu_ji_e)
            anniu_jian(anniu_ji_f)
            anniu_jian(anniu_ji_g)
            anniu_jian(anniu_ji_h)
            anniu_jian(anniu_ji_i)
            anniu_jian(anniu_ji_j)
            bcd(screen, '持股 :' + str(gu_a), (250, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_b), (250, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_c), (250, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_d), (250, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_e), (250, 450), 30, white)
            bcd(screen, '持股 :' + str(gu_f), (700, 50), 30, white)
            bcd(screen, '持股 :' + str(gu_g), (700, 150), 30, white)
            bcd(screen, '持股 :' + str(gu_h), (700, 250), 30, white)
            bcd(screen, '持股 :' + str(gu_i), (700, 350), 30, white)
            bcd(screen, '持股 :' + str(gu_j), (700, 450), 30, white)

            anniu_jian(anniu_huijia_3)


            if anniu_ji_a.peng(pos_x,pos_y) or f_50:
                f_50=True
                if anniu_ji_a.peng(pos_x,pos_y):
                    if m:
                        shuliang= gu_a

                    if gu_a>0:
                        gu_a -= shuliang
                        money_now +=shuliang*sui_a
                        shuliang=1
                        if m:
                            m=False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False
            if anniu_ji_b.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_b.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_b

                    if gu_b > 0:
                        gu_b -= shuliang
                        money_now += shuliang * sui_b
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False

            if anniu_ji_c.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_c.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_c

                    if gu_c > 0:
                        gu_c -= shuliang
                        money_now += shuliang * sui_c
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False

            if anniu_ji_d.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_d.peng(pos_x, pos_y):
                    if m:
                        shuliang =gu_d

                    if gu_d > 0:
                        gu_d -= shuliang
                        money_now += shuliang * sui_d
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False

            if anniu_ji_e.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_e.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_e

                    if gu_e > 0:
                        gu_e -= shuliang
                        money_now += shuliang * sui_e
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False

            if anniu_ji_f.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_f.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_f

                    if gu_f > 0:
                        gu_f -= shuliang
                        money_now += shuliang * sui_f
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False

            if anniu_ji_g.peng(pos_x,pos_y) or f_50:
                f_50 = True
                if anniu_ji_g.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_g

                    if gu_g > 0:
                        gu_g -= shuliang
                        money_now += shuliang * sui_g
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False


            if anniu_ji_h.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_h.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_h

                    if gu_h > 0:
                        gu_h -= shuliang
                        money_now += shuliang * sui_h
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False


            if anniu_ji_j.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_j.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_j

                    if gu_j > 0:
                        gu_j -= shuliang
                        money_now += shuliang * sui_j
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False

            if anniu_ji_i.peng(pos_x,pos_y) or f_50:

                f_50 = True
                if anniu_ji_i.peng(pos_x, pos_y):
                    if m:
                        shuliang = gu_i

                    if gu_i > 0:
                        gu_i -= shuliang
                        money_now += shuliang * sui_i
                        shuliang = 1
                        if m:
                            m = False

                    pos_x = 0
                    pos_y = 0
                    f_50 = False




        if anniu_huijia_3.peng(pos_x, pos_y):

            ditu_5 = False
            f_100=False
            f_99=False
            t_99 = True
            f_30=False
            f_50=False
            m=False
            ditu_2 = False
            ditu_3 = False
            ditu_1 = True
            ditu_4=False
            pos_x=0
            pos_y=0






    if ditu_3:
        screen.blit(shangdian, (0, 0))

        anniu_jian(anniu_mai_2)
        anniu_jian(anniu_mai_1)
        anniu_jian(anniu_huijia_1)

        if anniu_mai_2.peng(pos_x, pos_y):

            ditu_2 = False
            ditu_3 = False
            ditu_1 = False
            ditu_4 = True
            di_1 = True
            pos_x = 0
            pos_y = 0



        if anniu_mai_1.peng(pos_x, pos_y):


            ditu_2 = False
            ditu_3 = False
            ditu_1 = False
            ditu_4 = True
            di_2 = True
            pos_x = 0
            pos_y = 0


        if anniu_huijia_1.peng(pos_x, pos_y):

            pos_x = 0
            pos_y = 0
            ditu_5 = False
            di_1 = False
            di_2 = False
            ditu_4 = False
            ditu_3 = False
            ditu_2 = False
            ditu_1 = True







    if ditu_4 and pp:
        screen.blit(shangdian, (0, 0))
        if di_1:
            bcd(screen, '一律一千元', (200, 200), 40, red)
            bcd(screen, '可以加强学习效率', (200, 300), 40, red)

            if t_1:
                anniu_jian(anniu_shu)
            if t_2:

                anniu_jian(anniu_you)
            if t_3:
                anniu_jian(anniu_qin)
            if t_4:
                anniu_jian(anniu_ya)

            anniu_jian(anniu_huijia_2)


            if anniu_shu.peng(pos_x,pos_y) :
                if money_now >= 1000:
                    money_now-=1000
                    xiao_xue_1+=2
                    xiao_xue_2+=2
                    pos_x = 0
                    pos_y = 0
                    t_1=False

            if anniu_you.peng(pos_x,pos_y) :
                if money_now >= 1000:
                    money_now-=1000
                    xiao_qing_1+=2
                    xiao_qing_2+=2
                    pos_x = 0
                    pos_y = 0
                    t_2=False

            if anniu_qin.peng(pos_x,pos_y) :
                if money_now >= 1000:
                    money_now-=1000
                    xiao_yu_1+=2
                    xiao_yu_2+=2
                    pos_x = 0
                    pos_y = 0
                    t_3=False

            if anniu_ya.peng(pos_x,pos_y) :
                if money_now >= 1000:
                    money_now-=1000
                    xiao_duan_1+=2
                    xiao_duan_2+=2
                    pos_x = 0
                    pos_y = 0
                    t_4=False



        if di_2:

            bcd(screen, '你的家境为:' + str(jiajing), (100, 100), 40, red)
            bcd(screen, '1 家境= 10资金', (500, 100), 40, red)
            bcd(screen, '家境低于50,父母死亡·', (500, 200), 40, red)

            anniu_jian(anniu_huan_1)
            anniu_jian(anniu_huan_2)
            anniu_jian(anniu_huan_3)
            anniu_jian(anniu_huan_4)
            anniu_jian(anniu_huan_5)


            screen.blit(money_z, (350, 30))
            anniu_jian(anniu_huijia_2)

            if anniu_huan_1.peng(pos_x, pos_y):

                if jiajing // 10 >= 1 :
                    jiajing = jiajing - 10
                    money_now = money_now + 100
                    pos_x = 0
                    pos_y = 0

            if anniu_huan_2.peng(pos_x, pos_y):
                if jiajing // 100 >= 1 :
                    jiajing = jiajing - 100
                    money_now = money_now + 1000
                    pos_x = 0
                    pos_y = 0

            if anniu_huan_3.peng(pos_x, pos_y):
                if jiajing // 1000 >= 1 :
                    jiajing = jiajing - 1000
                    money_now = money_now + 10000
                    pos_x = 0
                    pos_y = 0

            if anniu_huan_4.peng(pos_x, pos_y):
                if money_now // 100 >= 1 :
                    jiajing = jiajing + 10
                    money_now = money_now - 100
                    pos_x = 0
                    pos_y = 0

            if anniu_huan_5.peng(pos_x, pos_y):
                if money_now // 1000 >= 1 :
                    jiajing = jiajing + 100
                    money_now = money_now - 1000
                    pos_x = 0
                    pos_y = 0












    if jiajing<=50 and dei_1 :
        di_1 = False
        di_2 = False
        ditu_4 = False
        ditu_3 = False
        ditu_2 = False
        ditu_1 = False
        screen.blit(tian_kong,(0,0))
        bcd(screen, '你父母太穷饿死了', (200, 200), 40, red)
        anniu_jian(anniu_ji_xu)

        if anniu_ji_xu.peng(pos_x, pos_y) :
            pos_x=0
            pos_y=0
            money_geng_1=False
            fumu_t=False
            dei_1 = False
            ditu_1=True


    if money_geng_1 and money_geng_2:
        if time_ri==1 and time_yue % 1 ==0 and not time_yue/1==0:
            money_now+=money_geng
            money_geng_2=False








    if anniu_huijia_2.peng(pos_x, pos_y) or f_hui:
        pos_x = 0
        pos_y = 0
        ditu_6 = False
        ditu_5 = False
        di_1 = False
        di_2 = False
        ditu_4 = False
        ditu_3 = False
        ditu_2 = False
        ditu_1 = True

        t_shimao_6=True
        f_shimao_1=False
        t_shimao_2 = True
        t_shimao_3 = True
        f_shimao_5 =False
        f_shimao_a=False
        f_shimao_b = False
        f_shimao_c=False
        f_shimao_d=False
        f_shimao_e=False
        f_hui=False
        t_shimao_10=True
        f_as_1=False
        f_as_2=False
        f_as_3 = False
        f_as_4 = False
        f_as_5 = False
        f_as_6 = False


    if jiajing<=0:
        f_hui
        screen.blit(tian_kong,(0,0))
        bcd(screen,'你饿死了',(450,300),60,red)
    if f_fuqing:
        screen.blit(tian_kong,(0,0))
        bcd(screen,"父亲死亡，全剧终",(200,200),30,red)


    pygame.display.update()
