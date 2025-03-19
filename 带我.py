import pygame
import sys
import random
import datetime

pygame.init()

clock = pygame.time.Clock()                     # 设置帧率
clock.tick(40)

size = width, height = 600, 500  # 屏幕大小
screen = pygame.display.set_mode(size)  # 创建屏幕
white = 255,255,255  # 字体颜色

def ziti(size,color,why):
    myfont = pygame.font.Font(None, size)  # 设置字体
    ha = myfont.render( why, True,color )
    return ha
pygame.display.set_caption("贪吃蛇")



# 循环进行屏幕卡死

a = False
b = False
c = False
d = False
x = 100
y = 100

clock = pygame.time.Clock()
print(clock)
bbb=pygame.time.get_ticks()
print(bbb)

a=ziti(160,white,'clock')
# 屏幕字体建立位置
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print('右边')
                x = x + 10
            if event.key == pygame.K_a:
                print('左边')
                x = x - 10
            if event.key == pygame.K_w:
                print('上边')
                y = y - 10
            if event.key == pygame.K_s:
                print('下边')
                y = y + 10

    cd = [x, y]

screen.blit(a, cd)
blue=100,200,100
screen.fill(blue)
pygame.display.flip()
pygame.display.update()

