"""classe Monster
Enemis qui apparaissent à la droite de l'écran
"""

import pygame

from health_bar import HealthBar


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
        self.health_bar: HealthBar = HealthBar(self.health / self.max_health)

    def damage(self, amount: int) -> None:
        """perd des vies"""
        self.health -= amount

    def forward(self, player: pygame.sprite.Sprite) -> None:
        """déplacement du monstre"""
        if not pygame.sprite.spritecollide(
            self,
            pygame.sprite.Group(player),
            False,
            pygame.sprite.collide_mask,
        ):
            self.rect.x -= self.velocity

    def update(self, player: pygame.sprite.Sprite) -> None:
        """mise à jour du monstre"""
        self.forward(player)
        if self.health <= 0:
            self.kill()
        self.health_bar.update(
            self.health / self.max_health,
            (self.rect.centerx, self.rect.top - 10),
        )

    def draw_health_bar(self) -> None:
        """dessine la barre de vie"""
        self.health_bar.draw()
