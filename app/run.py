import pygame
import random
from tools import *
from pieces import *
import sys

pygame.init()
pygame.font.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
font = pygame.font.SysFont('Comic Sans MS', 30)
chess_font = pygame.font.SysFont('Comic Sans MS', 50)


chess_text = chess_font.render("Welcome to Chess", True, Dark)
text = font.render("Start", True, Light)

def pieces_luncher():
    objects = []

    # Pawns
    for i in range(1, 9):
        objects.append(Pawn('b', 2, i, 'pawn'))
    for i in range(1, 9):
        objects.append(Pawn('w', 7, i, 'pawn'))

    # Rooks
    objects.append(Rook('b', 1, 1, 'rook'))
    objects.append(Rook('b', 1, 8, 'rook'))
    objects.append(Rook('w', 8, 1, 'rook'))
    objects.append(Rook('w', 8, 8, 'rook'))

    # Knights
    objects.append(Knight('b', 1, 2, 'knight'))
    objects.append(Knight('b', 1, 7, 'knight'))
    objects.append(Knight('w', 8, 2, 'knight'))
    objects.append(Knight('w', 8, 7, 'knight'))

    # Bishops
    objects.append(Bishop('b', 1, 3, 'bishop'))
    objects.append(Bishop('b', 1, 6, 'bishop'))
    objects.append(Bishop('w', 8, 3, 'bishop'))
    objects.append(Bishop('w', 8, 6, 'bishop'))

    # Queens
    objects.append(Queen('b', 1, 5, 'queen'))
    objects.append(Queen('w', 8, 5, 'queen'))

    # Kings
    objects.append(King('b', 1, 4, 'king'))
    objects.append(King('w', 8, 4, 'king'))

    return objects


def main():
    objects = pieces_luncher()
    first_click = True
    current_figure = None
    color = 'w'
    turn = 1
    winner = None
    runing = True
    while runing:
        if turn % 2 == 0:
            color = 'b'
        else:
            color = 'w'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_click:
                    row1, col1 = (event.pos[1] // SQUARE_SIZE) + 1 , (event.pos[0] // SQUARE_SIZE) + 1
                    if find_figure(objects, row1, col1) and find_figure(objects, row1, col1).color == color:
                        current_figure = find_figure(objects, row1, col1)
                        first_click = False
                            
                else:
                    first_click = True
                    row2, col2 = (event.pos[1] // SQUARE_SIZE) +1 , (event.pos[0] // SQUARE_SIZE)+1
                    if current_figure.is_valid_move(objects, (row2,col2)):
                        current_figure.move(row2, col2)
                        current_figure = None
                        turn += 1
                        

        if objects[-1].is_checkmate(objects):
            winner = "Blacks"
            runing = False
            break
        elif objects[-2].is_checkmate(objects):
            winner = "Whites"
            runing = False
            break

        update_display(screen, objects)

    end_screen(winner)


def end_screen(who):
    win_text = chess_font.render(f"{who} Win!", True, Light)
    again_text = font.render("Play Again", True, Light)
    again_button = pygame.draw.rect(screen, Dark, (WIDTH // 2 - 120, HEIGHT // 2 , 200, 100))

    again_rect = text.get_rect(center=again_button.center)

    clock = pygame.time.Clock()
    time = 0
    while time < 5:
        clock.tick(60)
        time += 1/60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if again_button.collidepoint(event.pos):
                    # If the start button is clicked, exit the menu loop
                    return main()

        screen.fill(Dark)
        screen.blit(win_text, (WIDTH//2 - 150, HEIGHT//2 - 40))
        screen.blit(again_text, again_rect)
        pygame.display.update()


def draw_menu():

    screen.fill(Light)
    start_button = pygame.draw.rect(screen, Dark, (WIDTH // 2 - 100, HEIGHT // 2 - 50 , 200, 100))

    
    # Display text on the button
    text_rect = text.get_rect(center=start_button.center)
    screen.blit(text, text_rect)
    screen.blit(chess_text, (WIDTH//2 - 200 , 100))

    pygame.display.flip()

    return start_button



def main_menu():
    while True:
        start_button = draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    # If the start button is clicked, exit the menu loop
                    return

        

if __name__ == "__main__":
    main_menu()
    main()

    pygame.quit()
    sys.exit()