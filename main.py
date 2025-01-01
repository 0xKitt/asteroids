import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_obj = pygame.time.Clock()
    dt = 0
    player_obj = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        player_obj.update(dt)

        screen.fill("black")
        player_obj.draw(screen)

        pygame.display.flip()
        dt = clock_obj.tick(60)/1000


if __name__ == "__main__":
    main()
