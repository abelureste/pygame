import pygame, sys
from player import *
from map import map_tileset
from pygame.locals import *

# --- initialize pygame ---
pygame.init()
pygame.display.set_caption('game')
screen = pygame.display.set_mode((1200, 1200),0,32)
display = pygame.Surface((450, 450))
clock = pygame.time.Clock()

# --- load assets ---
tile_img = pygame.image.load('isometric/assets/isometric-tile2.png').convert()
tile_img_tree = pygame.image.load('isometric/assets/isometric-tile2-tree.png').convert()
tile_img_bridge = pygame.image.load('isometric/assets/isometric-tile2-bridge.png').convert()

# --- set asset transparency ---
tile_img.set_colorkey((0, 0, 0))
tile_img_tree.set_colorkey((0, 0, 0))
tile_img_bridge.set_colorkey((0, 0, 0))

# --- import map tileset ---
game_map = map_tileset

# --- import and initialize player class ---
player = Player(250, 250, 'isometric/assets/isometric-player.png')

def playGame():
    while True:
        # --- fill background ---
        display.fill((174,204,208))

        # --- draw 2D map ---
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):

                screen.blit(player.image, (209 + x * 16 - y * 16, 150 + x * 8 + y * 8))

                if tile >= 5:
                    display.blit(tile_img, (209 + x * 16 - y * 16, 150 + x * 8 + y * 8))             
                if tile == 4:
                    display.blit(tile_img_tree, (209 + x * 16 - y * 16, 150 + x * 8 + y * 8 - 16))

        # --- draw player model ---
        display.blit(player.image, player.rect.topleft)

        # --- listener to exit program ---
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
        pygame.display.update()
        player.update()
        clock.tick(60)

playGame()