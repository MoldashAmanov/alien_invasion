import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Назначение цвета фона
        self.bg_color = (230, 230, 230)

        self.ship = Ship(screen)


    def run_game(self):
        """Запуск основного цикла игры"""
        
        while True:
            # Отслеживание событий с клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Отображение последнего прорисованного экрана
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра класса и запуск игры
    ai = AlienInvasion()
    ai.run_game()
