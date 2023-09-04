"""classe StartScreen"""

import pygame


class StartScreen:
    """gestion de l'écran d'acceuil"""

    def __init__(self) -> None:
        width, height = pygame.display.get_window_size()
        self.background: pygame.Surface = pygame.image.load(
            "assets/bg.jpg"
        ).convert_alpha()
        self.banner: pygame.Surface = pygame.image.load(
            "assets/banner.png"
        ).convert_alpha()
        self.banner = pygame.transform.scale_by(
            self.banner, 400 / self.banner.get_width()
        )
        self.banner_rect = self.banner.get_rect(
            center=(width // 2, height // 2 - 70)
        )
        self.button: pygame.Surface = pygame.image.load(
            "assets/button.png"
        ).convert_alpha()
        self.button = pygame.transform.scale_by(
            self.button, 300 / self.button.get_width()
        )
        self.button_rect = self.button.get_rect(
            center=(width // 2, height // 2 + 70)
        )

    def logic(self) -> None:
        """déroulement des actions"""
        return

    def next(self) -> bool:
        """passe à la sène suivante"""
        return (
            self.button_rect.collidepoint(pygame.mouse.get_pos())
            and pygame.mouse.get_pressed()[0]
        )

    def draw(self) -> None:
        """dessine les éléments de l'écran d'accueil"""
        screen = pygame.display.get_surface()
        screen.blit(self.background, (0, -200))
        screen.blit(self.button, self.button_rect)
        screen.blit(self.banner, self.banner_rect)
        pygame.display.flip()
