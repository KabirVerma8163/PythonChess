import pygame
import os


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
pygame.init()

screenwidth = 500
screenheight = 500

win = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("Ghetto Chess")

x = 50
y = 50
char1width = 40
char1height = 60

IsJump = False
JumpCount = 10
JumpCountCounter = -10

run = True
while run:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()
    vel = 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not keys[pygame.K_d]:
        win.fill((0, 0, 0))
    if keys[pygame.K_s]:
        vel = 15
    # if keys[pygame.K_j]:
    #     JumpCount = 20
    #     JumpCountCounter = -20

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenwidth - char1width:
        x += vel
    if not IsJump:
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenheight - char1height:
            y += vel
        if keys[pygame.K_SPACE]:
            IsJump = True
    else:
        if JumpCount >= JumpCountCounter:
            y -= (JumpCount * abs(JumpCount)) * 0.5
            JumpCount -= 1
        else:
            JumpCount = 10
            IsJump = False

    pygame.draw.rect(win, (255, 255, 0), (x, y, char1width, char1height))
    pygame.display.update()

pygame.quit()
