"""Jeu Shoot Monsters"""

import pygame

from game import Game

pygame.init()

pygame.display.set_caption("Shoot monsters")
WIDTH = 1080
HEIGHT = 720
screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()


game = Game()

RUNNING = True

while RUNNING:
    game.game_logic()
    game.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.launch_projectile()

    clock.tick(60)

pygame.quit()
