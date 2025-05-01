import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 1

    def getInput(self):
        keys = pygame.key.get_pressed()

        self.direction.x = 0
        self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
        if keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_w]:
            self.direction.y = -1

    def update(self):
        self.getInput()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed