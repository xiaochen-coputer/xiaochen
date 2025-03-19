from mukuai import *

pygame.init()
jiedao = pygame.image.load('街道.webp')
f_shang = False
tiao_shang = True
shangdian = pygame.image.load('商店.jpg')
zz, zzz = shangdian.get_size()
shangdian = pygame.transform.smoothscale(shangdian, (zz * 1.2, zzz * 1.2))

sui_1 = 1
xiao_xue_1 = 1
xiao_xue_2 = 2
xiao_yu_1 = 1
xiao_yu_2 = 2
xiao_qing_1 = 1
xiao_qing_2 = 2
xiao_duan_1 = 1
xiao_duan_2 = 2

ditu_1 = True
ditu_2 = False
f_hujia = False
ditu_3 = False

f_xue = False
tiao_zimu = True
f_zhishi = False
f_yueli = False
f_kan = False
f_duan = False
ditu_4 = False
f_100 = False
t_99 = True
f_gu = False

t_1 = True
t_2 = True
di_1 = False
di_2 = False
t_3 = True
t_4 = True
dagong_1 = False
dagong_2 = False

dei_1 = True
money_geng_1 = True
money_geng_2 = True
money_geng = 1200
caidan_f = False
jiajing_t = True
fumu_t = True
ditu_5 = False
ditu_6 = False
ditu_7 = False
f_shimao = False
f_xian = False
f_zhengfu = False
f_gupiao = False
f_99 = False
f_xuexiao = False

fen_yu = 0
f_kao = False
T_kao_1 = True
t_kaoshi = True
t_xue = True
xuexiao = pygame.image.load('学校.jpg')
cc, ccc = xuexiao.get_size()
xuexiao = pygame.transform.smoothscale(xuexiao, (cc * 1.6, ccc * 1.2))
f_xue_1 = False
jiaoshi = pygame.image.load('教室.jpg')

bb, bbb = jiaoshi.get_size()
jiaoshi = pygame.transform.smoothscale(jiaoshi, (bb * 1.6, bbb * 1.3))

f_shi = True
f_su1 = False
f_su2 = False
f_x = False
f_xue_2 = False
f_xue_3 = False
f_xue_4 = False
f_xue_5 = False
f_xue_6 = False
f_xue_7 = False
shitang = pygame.image.load('食堂.jpg')
dd, ddd = jiaoshi.get_size()
shitang = pygame.transform.smoothscale(shitang, (dd * 1, ddd * 1))


def tu(tupian, c, k):
    add, cdd = tupian.get_size()
    tupian = pygame.transform.smoothscale(tupian, (add * c, cdd * k))
    return tupian


zoulang_1 = pygame.image.load('走廊.jpg')
zoulang_1 = tu(zoulang_1, 2.2, 2.1)
sushe = pygame.image.load('宿舍男.jpg')
sushe=tu(sushe, 2.2, 2.1)
shimao=pygame.image.load('世贸.jpg')
f_shimao_1=False
t_shimao_2=True
t_shimao_3=True
t_kong=True
t_meishi=True
t_hulain=True
t_fu=True
t_youxi=True
f_shimao_4=False
f_shimao_5=False
f_shimao_6=False
f_shimao_7=False
f_shimao_8=False
f_shimao_9=False
t_shimao_6=True
f_shimao_5=False
f_shimao_a=False
f_shimao_b=False
f_shimao_c=False
f_shimao_d=False
f_shimao_e=False
you_1='无'
you_2='无'
you_3='无'
you_4='无'
you_5='无'
t_shimao_10= True
f_as_1=False
f_hui=False
f_as_2=False
f_as_3=False
f_as_4=False
f_as_5=False
f_as_6=False

yu_a=1
yu_b=1
yu_c=1
yu_d=1
yu_e=1
yu_f=1
f_bdbd=False
t_bdbd=True
x=5
g=5
q=5
w=5
e=5
r=5
m=False
m2=False
shuliang=1
f_30=False
f_50=False
n=False
f_fuqing=False
yiyuan_1=False
life=1000
money_fu=5000
bili=1.2
pp=True
d_1=1
d_2=1
d_3=1
d_4=1
d_5=1