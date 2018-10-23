# -*- coding: UTF-8 -*-


class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self, ai_setting):
        """初始化统计信息"""
        self.ai_setting = ai_setting
        self.game_active = True
        self.reset_starts()
        self.score = 0

        self.game_active = False

    def reset_starts(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_setting.ship_limit
