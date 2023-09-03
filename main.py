"""Jeu Shoot Monsters"""

import pygame

from game import Game


class Fenetre:
    """Gestion de la fenêtre du jeu"""

    def __init__(self) -> None:
        pygame.init()
        width = 1080
        height = 720
        self.screen: pygame.Surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Shoot monsters")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.game = Game()

    def run(self) -> None:
        """Fait tourner le jeu"""
        while True:
            self.game.game_logic()
            self.game.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.clock.tick(60)


if __name__ == "__main__":
    jeu = Fenetre()
    jeu.run()
    pygame.quit()
