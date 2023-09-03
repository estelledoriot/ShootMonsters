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

    def spawn_monster(self) -> None:
        """crée un nouveau monstre"""
        self.all_monsters.add(Monster((1000, 670)))

    def launch_projectile(self) -> None:
        """ajoute un nouveau projectile"""
        self.all_projectiles.add(Projectile(self.player.center))

    def game_logic(self) -> None:
        """fait un tour du jeu"""
        # lancement des projectiles
        for event in pygame.event.get(eventtype=pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                self.launch_projectile()

        # déplacement des projectiles
        self.all_projectiles.update()

        # déplacement des monstres
        self.all_monsters.update(self.player)

        # collision des monstres et des projectiles
        pygame.sprite.groupcollide(
            self.all_monsters,
            self.all_projectiles,
            False,
            True,
            pygame.sprite.collide_mask,
        )

        # déplacement du personnage
        self.player.update(self.all_monsters)

    def draw(self) -> None:
        """affiche tous les éléments du jeu"""
        screen = pygame.display.get_surface()
        screen.blit(self.background, (0, -200))
        screen.blit(self.player.image, self.player.rect)
        self.all_projectiles.draw(screen)
        self.all_monsters.draw((screen))
        pygame.display.flip()
