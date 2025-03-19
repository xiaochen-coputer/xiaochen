import pygame

pygame.init()

orange = '#FFA500'
def bcd(screen, why, weizhi, size=30, color=orange):
    myfont = pygame.font.SysFont('kaiti', size)
    woaini = '{}'.format(why)
    ha = myfont.render(woaini, True, color)
    screen.blit(ha, weizhi)


def abc(why, size, color):
    myfont = pygame.font.SysFont('kaiti', size)
    woaini = '{}'.format(why)
    ha = myfont.render(woaini, True, color)
    return ha


class Button():
    def __init__(self, screen, x, y, size, msg):
        """initialize button attrributes"""

        self.ff = pygame.image.load('按钮.png').convert_alpha()
        self.w, self.h = self.ff.get_size()
        self.ff = pygame.transform.smoothscale(self.ff, (self.w // 3, self.h // 3))
        # set the dimesions and properties of the button

        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('kaiti', size)

        # build the button's rect object and center it

        self.msg = msg
        # the button message needs to be prepped only once
        self.screen = screen
        self.x = x
        self.y = y
        self.weizhi = [x, y]
        self.size = size

    @property
    def chuang_wen(self):
        """turn msg into a rendered image and center text on the button"""
        self.woaini = '{}'.format(self.msg)
        self.msg_image = self.font.render(self.woaini, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.weizhi

        self.ff_rect = self.ff.get_rect()

        self.ff_rect.center = self.weizhi

        self.x = self.ff_rect.x
        self.y = self.ff_rect.y

    @property
    def draw_button(self):
        self.screen.blit(self.ff, self.ff_rect)

        self.screen.blit(self.msg_image, self.msg_image_rect)

    def peng(self, x, y):
        if self.x + 130 > x > self.x and self.y < y < self.y + 60:
            return True


def anniu_jian(why):
    why.chuang_wen
    why.draw_button



if __name__ == '__main__':
    print('a')
