# -*- coding: UTF-8 -*-

import pygame.font


class Scoreboard():
    """初始化得分涉及的属性"""

    def __init__(self, ai_setting, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        # 显示得分信息时使用的字体设置

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始化得分图像
        self.prep_score()

    def prep_score(self):
        """将得分转换为一福渲染的图像"""
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_setting.bg_color)

        # 将得分放在屏幕右下角

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
