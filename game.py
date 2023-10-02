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

    def logic(self) -> None:
        """fait un tour du jeu"""
        # lancement des projectiles
        for event in pygame.event.get(eventtype=pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                self.launch_projectile()

        # déplacement des projectiles
        self.all_projectiles.update()

        # collision des monstres et des projectiles
        hit_monsters = pygame.sprite.groupcollide(
            self.all_monsters,
            self.all_projectiles,
            False,
            True,
            pygame.sprite.collide_mask,
        )
        for monster in hit_monsters:
            if hit_monsters[monster]:
                monster.damage(self.player.attack)

        if not self.all_monsters:
            self.spawn_monster()

        # déplacement des monstres
        self.all_monsters.update(self.player)

        # collision entre les monstres et le joueur
        monsters = pygame.sprite.spritecollide(
            self.player, self.all_monsters, False, pygame.sprite.collide_mask
        )
        for monster in monsters:
            self.player.damage(monster.attack)
        # TODO fin du jeu lorsque le joueur est mort
        # TODO score ?

        # déplacement du personnage
        self.player.update(self.all_monsters)

    # TODO finir
    def next(self) -> bool:
        """passe à la scène suivante"""
        return self.player.health <= 0

    def draw(self) -> None:
        """affiche tous les éléments du jeu"""
        screen = pygame.display.get_surface()
        screen.blit(self.background, (0, -200))

        screen.blit(self.player.image, self.player.rect)
        self.player.draw_health_bar()

        self.all_projectiles.draw(screen)

        self.all_monsters.draw((screen))
        for monster in self.all_monsters:
            monster.draw_health_bar()

        pygame.display.flip()
