# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:48:41 2018

@author: wuzhiqiang
"""

class Settings():
    """存储项目的所有设置的类"""
    
    def __init__(self):
        """初始化"""
        #屏幕设置
        self.screen_width = 800
        self.screen_heigh = 600
        self.bg_color = (230, 230, 230)
        
        #飞船的设置
        self.ship_speed_factor = 1.5
        
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60