# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:56:27 2018

@author: wuzhiqiang
"""

import pygame
from pygame.sprite import Group

from setting import Settings 
from ship import Ship

import game_fuctions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个拥有存储子弹的编组
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #开始游戏的主循环
    while True:
        
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
                
run_game()