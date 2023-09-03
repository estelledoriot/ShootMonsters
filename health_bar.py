"""Classe HealthBar
gère les barres de vie du joueur et des monstres
"""

import pygame


class HealthBar:
    """barre de vie"""

    def __init__(
        self,
        ratio: float,
    ) -> None:
        self.ratio: float = ratio
        self.rect: pygame.Rect = pygame.Rect(0, 0, 100, 5)
        self.health_bar: pygame.Rect = pygame.Rect(0, 0, self.ratio * 100, 5)

    def update(self, ratio: float, midtop: tuple[int, int]) -> None:
        """mise à jour de la barre de vie"""
        self.ratio = ratio
        self.health_bar.width = int(self.ratio * 100)
        self.rect.midbottom = midtop[0], midtop[1] - 10
        self.health_bar.topleft = self.rect.topleft

    def draw(self) -> None:
        """affiche la barre de vie"""
        fenetre = pygame.display.get_surface()
        if self.ratio >= 0.5:
            bar_color = pygame.Color(111, 210, 46)
        elif self.ratio >= 0.1:
            bar_color = pygame.Color(252, 222, 53)
        else:
            bar_color = pygame.Color(252, 56, 53)
        back_color = pygame.Color(60, 60, 60)
        pygame.draw.rect(fenetre, back_color, self.rect)
        pygame.draw.rect(fenetre, bar_color, self.health_bar)
