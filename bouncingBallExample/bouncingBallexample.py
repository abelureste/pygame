import sys, pygame
pygame.init()

size = width, height = (640, 480)
speed = [5, 5]
black = 0, 0, 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

ball = pygame.image.load("bouncingBallExample/intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    clock.tick(60)
    screen.fill((139,242,255))
    screen.blit(ball, ballrect)
    pygame.display.flip()
