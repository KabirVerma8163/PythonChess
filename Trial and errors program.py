import pygame
from modules.all_objects_module import positions_dictionary
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)
pygame.init()

screenwidth = 850
screenheight = 750

win = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Ghetto Chess")


# printing the chessboard
def graphic_chessboard(window, position_dict):
    for i in position_dict:
        position_object = positions_dictionary[i]
        window.blit(position_object.image, (position_object.pic_x_cord, position_object.pic_y_cord))
        # print(position_object.letter, position_object.number, position_object.pic_x_cord, position_object.pic_y_cord)

    pygame.display.update()


graphic_chessboard(win, positions_dictionary)

run = True
while run:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()
    vel = 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
