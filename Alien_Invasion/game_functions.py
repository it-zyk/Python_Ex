# coding=utf-8

import sys

import pygame

from time import sleep
from alien import Alien
from bullet import Bullet


def check_alien_bottom(ai_setting, stars, screen, ship, alien_list, bullets_list):
    screen_rect = screen.get_rect()
    for alien in alien_list.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stars, screen, ship, alien_list, bullets_list)
            break


def change_fleet_direction(ai_setting, alien_list):
    for alien in alien_list.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def check_fleet_edge(ai_setting, alien_list):
    for alien in alien_list.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, alien_list)
            break


def ship_hit(ai_setting, stars, screen, ship, alien_list, bullets_list):
    if stars.ship_left > 0:
        stars.ship_left -= 1

        alien_list.empty()
        bullets_list.empty()

        create_fleet(ai_setting, screen, ship, alien_list)
        ship.center_ship()
        sleep(0.5)
    else:
        stars.game_active = False
        pygame.mouse.set_visible(True)


def update_alien(ai_setting, stars, screen, ship, alien_list, bullets_list):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edge(ai_setting, alien_list)
    alien_list.update()
    check_alien_bottom(ai_setting, stars, screen,
                       ship, alien_list, bullets_list)
    if pygame.sprite.spritecollideany(ship, alien_list):
        ship_hit(ai_setting, stars, screen, ship, alien_list, bullets_list)


def get_number_rows(ai_setting, ship_height, alien_height):
    """计算屏幕可容纳多少外星人"""
    available_space_y = (ai_setting.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_setting, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_setting, screen, alien_list, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien_list.add(alien)


def create_fleet(ai_setting, screen, ship, alien_list):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(
        ai_setting, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, alien_list,
                         alien_number, row_number)


def check_keydown_events(event, ai_setting, screen, ship, bullets_list):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # 向右移动飞船
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_setting, screen, ship, bullets_list)


def fire_bullet(ai_setting, screen, ship, bullets_list):
    if len(bullets_list) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets_list.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_setting, screen, stats, play_button, ship, alien_list, bullets_list, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # 隐藏光标
        pygame.mouse.set_visible(False)
        stats.reset_starts()
        stats.game_active = True

        # 清空外星人列表和子弹列表
        alien_list.empty()
        bullets_list.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_setting, screen, ship, alien_list)
        ship.center_ship()


def check_events(ai_setting, screen, stats, play_button, ship, alien_list, bullets_list):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats,
                              play_button, ship, alien_list, bullets_list, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets_list)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(ai_setting, screen, stats, sb, ship, alien_list, bullets_list):
    #    bullets.update()
    # bullets_list.update()
    for bullet in bullets_list.copy():
        # 更新子弹的位置
        bullet.update()
        if bullet.rect.bottom <= 0:
            # 删除已消失的子弹
            bullets_list.remove(bullet)
    collisions = pygame.sprite.groupcollide(
        bullets_list, alien_list, True, True)
    if collisions:
        stats.score += ai_setting.alien_point
        sb.prep_score()
    if len(alien_list) == 0:
        bullets_list.empty()
        create_fleet(ai_setting, screen, ship, alien_list)


def update_screen(ai_setting, screen, stats, sb, ship, alien_list, bullets_list, play_button):
    """更新屏幕上的图像，切换到新屏幕"""
    # 每次循环时重绘屏幕

    screen.fill(ai_setting.bg_color)
    for bullet in bullets_list.sprites():
        bullet.draw_bullect()
    # 在指定位置绘制飞船
    ship.blitme()
    # alien.blitme()
    alien_list.draw(screen)
    # 让最近绘制的屏幕可见
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()
