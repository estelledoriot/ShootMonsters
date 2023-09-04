"""Jeu Shoot Monsters"""

import pygame

from game import Game
from start import StartScreen


class Fenetre:
    """Gestion de la fenêtre du jeu"""

    def __init__(self) -> None:
        pygame.init()
        width = 1080
        height = 720
        self.screen: pygame.Surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Shoot monsters")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.scene = StartScreen()

    def change_scene(self) -> None:
        """Passe à la scène suivante"""
        if isinstance(self.scene, StartScreen):
            self.scene = Game()
        elif isinstance(self.scene, Game):
            self.scene = StartScreen()

    def run(self) -> None:
        """Fait tourner le jeu"""
        while True:
            if self.scene.next():
                self.change_scene()

            self.scene.logic()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.scene.draw()
            self.clock.tick(60)


if __name__ == "__main__":
    jeu = Fenetre()
    jeu.run()
    pygame.quit()
