# coding=utf-8
import pygame


class Ship():

    def __init__(self, ai_setting, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen
        self.ai_setting = ai_setting

        # 加载飞船图像并获取其外接矩形
        self.ship_image = pygame.image.load("images/ship.bmp")
        self.rect = self.ship_image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数
        self.ceter = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.ship_image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ceter += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.ceter -= self.ai_setting.ship_speed_factor

        #  根据self.center 更新 ship.rect
        self.rect.centerx = self.ceter

    def center_ship(self):
        self.center = self.screen_rect.centerx
