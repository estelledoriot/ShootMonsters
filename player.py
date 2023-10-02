"""classe Player
Joueur principal du jeu
Peut se déplacer à droite et à gauche
"""

import pygame

from health_bar import HealthBar


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
        self.health_bar: HealthBar = HealthBar(self.health / self.max_health)

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

    def damage(self, amount: int) -> None:
        """dégâts infligés au joueur"""
        self.health -= amount

    def update(self, all_monsters: pygame.sprite.Group) -> None:
        """mise à jour de la position du personnage"""
        # déplacements
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and not pygame.sprite.spritecollide(
            self, all_monsters, False, pygame.sprite.collide_mask
        ):
            self.move_right()
        elif pressed[pygame.K_LEFT]:
            self.move_left()

        # mise à jour de la barre de vie
        self.health_bar.update(
            self.health / self.max_health,
            (self.rect.centerx, self.rect.top + 20),
        )

    def draw_health_bar(self) -> None:
        """dessine la barre de vie"""
        self.health_bar.draw()
