# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.rect.Rect(600, 580, 20, 40)


    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.rect.move_ip(0, -3)
        if key[pygame.K_s]:
            self.rect.move_ip(0, 3)
        if key[pygame.K_a]:
            self.rect.move_ip(-3, 0)
        if key[pygame.K_d]:
            self.rect.move_ip(3, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, 'white', self.rect)


player = Player(600, 580)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    floor = pygame.draw.rect(screen, 'red', pygame.Rect(0, 620, 1280, 100))

    player.input()
    player.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()