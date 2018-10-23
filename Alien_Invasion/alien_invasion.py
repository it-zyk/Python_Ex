# -*- coding: UTF-8 -*-
import sys

import pygame


from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame.sprite import Group

import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.capton)
    ship = Ship(ai_setting, screen)
    bullets_list = Group()
    alien_list = Group()
    play_button = Button(ai_setting, screen, 'Play')
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    # 开始游戏的主循环

    # 创建外星人群
    gf.create_fleet(ai_setting, screen, ship, alien_list)

    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_setting, screen, stats,
                        play_button, ship, alien_list, bullets_list)
        # 键盘移动更新图像位置

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship,
                              alien_list, bullets_list)
            gf.update_alien(ai_setting, stats, screen,
                            ship, alien_list, bullets_list)
            # 更新屏幕上的图像，切换到新屏幕
        gf.update_screen(ai_setting,  screen, stats, sb, ship, alien_list,
                         bullets_list, play_button)


run_game()
