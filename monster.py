"""classe Monster
Enemis qui apparaissent à la droite de l'écran
"""

import pygame


class Monster(pygame.sprite.Sprite):
    """monstre
    midbottom_origin: position originale de l'ennemi (du milieu de ses pieds)
    """

    def __init__(self, midbottom_origin: tuple[int, int]) -> None:
        super().__init__()
        self.max_health: int = 100
        self.health: int = self.max_health
        self.attack: int = 5
        self.image = pygame.image.load("assets/mummy.png").convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect(
            midbottom=midbottom_origin
        )
        self.velocity: int = 2

    def update(self, player) -> None:
        """déplacement du monstre"""
        if not pygame.sprite.spritecollide(
            self,
            pygame.sprite.Group(player),
            False,
            pygame.sprite.collide_mask,
        ):
            self.rect.x -= self.velocity
