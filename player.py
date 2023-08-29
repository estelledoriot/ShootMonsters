"""classe Player
Joueur principal du jeu
Peut se déplacer à droite et à gauche
"""

import pygame


class Player(pygame.sprite.Sprite):
    """joueur
    midtbottom_origin: position originale de l'ennemi (du milieu de ses pieds)
    """

    def __init__(self, midtbottom_origin: tuple[int, int]) -> None:
        super().__init__()

        self.image: pygame.Surface = pygame.image.load(
            "assets/player.png"
        ).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect(
            midbottom=midtbottom_origin
        )

        self.max_health: int = 100
        self.health: int = self.max_health
        self.attack: int = 10
        self.velocity: int = 5

    @property
    def center(self) -> tuple[int, int]:
        """position du centre du personnage"""
        return self.rect.center

    def move_right(self) -> None:
        """déplacement vers la droite"""
        self.rect.x += self.velocity
        largeur, _ = pygame.display.get_window_size()
        self.rect.right = min(self.rect.right, largeur)

    def move_left(self) -> None:
        """déplacement vers la gauche"""
        self.rect.x -= self.velocity
        self.rect.left = max(self.rect.left, 0)
