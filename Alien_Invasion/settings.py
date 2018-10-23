# coding=utf-8
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.capton = "Alien Invasion"

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移，为-1表示向左移动
        self.fleet_direction = 1

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 记分
        self.alien_point = 50
