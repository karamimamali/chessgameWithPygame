import pygame
import os
from tools import find_figure



class Piece:
    def __init__(self, color, row, col, img):
        self.color = color
        self.row = row
        self.col = col
        self.img = pygame.image.load(os.path.join('assets',color+'_'+img+'.png'))


    def move(self, row, col):
        self.row = row
        self.col = col


    def is_path_blocked(self, objects, dest_cords):
        dest_row, dest_col = dest_cords

        # Check if the move is vertical, horizontal, or diagonal
        if self.row == dest_row:
            # Check horizontal path
            step = 1 if dest_col > self.col else -1
            for col in range(self.col + step, dest_col, step):
                if find_figure(objects, self.row, col):
                    return True


        elif self.col == dest_col:
            # Check vertical path
            step = 1 if dest_row > self.row else -1
            for row in range(self.row + step, dest_row, step):
                if find_figure(objects, row, self.col):
                    return True


        elif abs(dest_row - self.row) == abs(dest_col - self.col):
            # Check diagonal path
            step_row = 1 if dest_row > self.row else -1
            step_col = 1 if dest_col > self.col else -1
            row, col = self.row + step_row, self.col + step_col
            while row != dest_row and col != dest_col:
                if find_figure(objects, row, col):
                    return True
                row += step_row
                col += step_col

        return False


    
class Pawn(Piece):
    def __init__(self, color, row, col, img):
        super().__init__(color, row, col, img)
        self.first_move = True


    def is_valid_move(self, objects, cords):
        if cords == (self.row, self.col):
            return False

        if self.color == 'w':
            enemy = find_figure(objects, cords[0], cords[1])

            if self.first_move and cords[0] == self.row - 2 and cords[1] == self.col and not enemy:
                self.first_move = False
                return True

            elif cords[0] == self.row - 1 and cords[1] == self.col and not enemy:
                self.first_move = False
                return True

            elif abs(cords[1] - self.col) == 1 and cords[0] == self.row - 1 and enemy and enemy.color == 'b':
                objects.remove(enemy)
                return True

        if self.color == 'b':
            enemy = find_figure(objects, cords[0], cords[1])

            if self.first_move and cords[0] == self.row + 2 and cords[1] == self.col and not enemy:
                self.first_move = False
                return True

            elif cords[0] == self.row + 1 and cords[1] == self.col and not enemy:
                self.first_move = False
                return True

            elif abs(cords[1] - self.col) == 1 and cords[0] == self.row + 1 and enemy and enemy.color == 'w':
                objects.remove(enemy)
                return True

        return False



class Rook(Piece):
    def is_valid_move(self, objects, cords):
        if cords == (self.row, self.col):
            return False

        if cords[0] == self.row or cords[1] == self.col:
            enemy = find_figure(objects, cords[0], cords[1])

            if not self.is_path_blocked(objects, cords):
                if not enemy or enemy.color != self.color:
                    if enemy:
                        objects.remove(enemy)
                    return True

        return False



class Knight(Piece):
    def is_valid_move(self, objects, cords):
        if cords == (self.row, self.col):
            return False

        dest_row, dest_col = cords
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        is_l_shape = (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

        if is_l_shape:
            enemy = find_figure(objects, dest_row, dest_col)

            if not enemy or enemy.color != self.color:
                if enemy:
                    objects.remove(enemy)
                return True

        return False



class Bishop(Piece):
    def is_valid_move(self, objects, cords):
        if cords == (self.row, self.col):
            return False

        dest_row, dest_col = cords
        if abs(dest_row - self.row) == abs(dest_col - self.col):
            enemy = find_figure(objects, dest_row, dest_col)

            if not self.is_path_blocked(objects, cords):
                if not enemy or enemy.color != self.color:
                    if enemy:
                        objects.remove(enemy)
                    return True

        return False



class Queen(Piece):
    def is_valid_move(self, objects, cords):
        if cords == (self.row, self.col):
            return False

        dest_row, dest_col = cords

        # Check for horizontal/vertical movement
        if dest_row == self.row or dest_col == self.col:
            if not self.is_path_blocked(objects, cords):
                enemy = find_figure(objects, dest_row, dest_col)
                if not enemy or enemy.color != self.color:
                    if enemy:
                        objects.remove(enemy)
                    return True

        # Check for diagonal movement
        if abs(dest_row - self.row) == abs(dest_col - self.col):
            if not self.is_path_blocked(objects, cords):
                enemy = find_figure(objects, dest_row, dest_col)
                if not enemy or enemy.color != self.color:
                    if enemy:
                        objects.remove(enemy)
                    return True

        return False



class King(Piece):
    def is_valid_move(self, objects, cords):
        if cords == (self.row, self.col):
            return False

        dest_row, dest_col = cords

        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)

        if row_diff <= 1 and col_diff <= 1:
            enemy = find_figure(objects, dest_row, dest_col)

            if not enemy or enemy.color != self.color:
                if enemy:
                    objects.remove(enemy)
                return True

        return False


    def is_checkmate(self, objects):
        # Check if the king is in check
        if self.is_in_check(objects):
            # Check all possible moves for the king, excluding its own pieces
            for row in range(self.row - 1, self.row + 2):
                for col in range(self.col - 1, self.col + 2):
                    if (row, col) != (self.row, self.col) and 0 <= row < 8 and 0 <= col < 8:
                        destination_piece = find_figure(objects, row, col)
                        if not destination_piece or destination_piece.color != self.color:
                            # The destination square is either empty or occupied by an opponent's piece
                            if not self.is_in_check_after_move(objects, (row, col)):
                                return False  # The king has at least one legal move to get out of check

            # If no legal moves found, the king is in checkmate
            return True

        # If the king is not in check, the game continues
        return False


    def is_in_check(self, objects):
        # Check if the king is under threat from any opponent's piece
        for obj in objects:
            if obj.color != self.color and obj.is_valid_move(objects, (self.row, self.col)):
                return True

        return False


    def is_in_check_after_move(self, objects, move):
        '''
        # Check if the king is under threat after a hypothetical move
        This is used to check if the king can escape check by making a specific move
        '''
        for obj in objects:
            if obj.row == self.row and obj.col == self.col:
                obj.move(move[0], move[1])
                break

        return self.is_in_check(objects)
