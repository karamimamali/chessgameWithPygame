import pygame
from const import *



def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            color = Dark if (row + col) % 2 == 0 else Light
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, objects):
    for obj in objects:
        screen.blit(obj.img, ((obj.col-1) * SQUARE_SIZE + 8, (obj.row-1) * SQUARE_SIZE + 10))

    
def find_figure(objects, row, col):
    for obj in objects:
        if obj.row == row and obj.col ==col:
            return obj
            break
    else:
        return False


def update_display(screen, objects):
    draw_board(screen)
    draw_pieces(screen, objects)
    pygame.display.update()