"""classe Projectile
Projectiles lancés par le joueur
"""

import pygame


class Projectile(pygame.sprite.Sprite):
    """projectile
    center_origin: position initale du centre de l'image
    """

    def __init__(self, center_origin: tuple[int, int]) -> None:
        super().__init__()

        self.original_image: pygame.Surface = pygame.image.load(
            "assets/projectile.png"
        ).convert_alpha()
        self.original_image = pygame.transform.scale(
            self.original_image, (50, 50)
        )

        self.image: pygame.Surface = self.original_image
        self.rect: pygame.Rect = self.image.get_rect(center=center_origin)
        self.angle: int = 0

        self.velocity: int = 7
        self.angular_velocity: int = 8

    def rotate(self) -> None:
        """fait tourner l'image sur elle-même"""
        self.angle += self.angular_velocity
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self) -> None:
        """déplacement des projectiles"""
        self.rotate()
        self.rect.x += self.velocity
        width, _ = pygame.display.get_window_size()
        if self.rect.right > width:
            self.kill()
