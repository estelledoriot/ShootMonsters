"""classe Game"""
import pygame

from monster import Monster
from player import Player
from projectile import Projectile


class Game:
    """jeu"""

    def __init__(self) -> None:
        self.background: pygame.Surface = pygame.image.load(
            "assets/bg.jpg"
        ).convert_alpha()
        self.player: Player = Player((400, 700))
        self.all_projectiles: pygame.sprite.Group = pygame.sprite.Group()
        self.all_monsters: pygame.sprite.Group = pygame.sprite.Group()
        self.spawn_monster()

    def check_collision(
        self, sprite: Player | Monster | Projectile, group: pygame.sprite.Group
    ) -> list:
        """vérifie si un sprite entre en collision avec un groupe de sprites"""
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask
        )

    def spawn_monster(self) -> None:
        """crée un nouveau monstre"""
        self.all_monsters.add(Monster((1000, 670)))

    def launch_projectile(self) -> None:
        """ajoute un nouveau projectile"""
        self.all_projectiles.add(Projectile(self.player.center))

    def game_logic(self) -> None:
        """fait un tour du jeu"""
        self.all_projectiles.update()

        for monster in self.all_monsters:
            if not self.check_collision(
                monster, pygame.sprite.Group(self.player)
            ):
                monster.forward()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            if not self.check_collision(self.player, self.all_monsters):
                self.player.move_right()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()

    def draw(self) -> None:
        """affiche tous les éléments du jeu"""
        screen = pygame.display.get_surface()
        screen.blit(self.background, (0, -200))
        screen.blit(self.player.image, self.player.rect)
        self.all_projectiles.draw(screen)
        self.all_monsters.draw((screen))
        pygame.display.flip()
