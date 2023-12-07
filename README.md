# chessgameWithPygame

Chess Game Documentation:
1. Constants (const.py):
1.1 WIDTH and HEIGHT:
Width and height of the game window.
1.2 ROWS and COLS:
Number of rows and columns on the chessboard.
1.3 SQUARE_SIZE:
Size of each square on the chessboard.
1.4 Colors:
BLUE: Color for the chessboard squares.
Dark: Dark color for pieces and board.
Light: Light color for pieces and board.
2. Pieces (pieces.py):
2.1 Class: Piece
Base class for all chess pieces.
Attributes:
color: Color of the piece ('w' for white, 'b' for black).
row: Current row position on the chessboard.
col: Current column position on the chessboard.
img: Image of the chess piece.
2.2 Class: Pawn (inherits from Piece)
Represents the pawn chess piece.
Attributes:
first_move: Flag to track the first move of the pawn.
Methods:
is_valid_move: Check if a move is valid for the pawn.
2.3 Class: Rook (inherits from Piece)
Represents the rook chess piece.
Methods:
is_valid_move: Check if a move is valid for the rook.
2.4 Class: Knight (inherits from Piece)
Represents the knight chess piece.
Methods:
is_valid_move: Check if a move is valid for the knight.
2.5 Class: Bishop (inherits from Piece)
Represents the bishop chess piece.
Methods:
is_valid_move: Check if a move is valid for the bishop.
2.6 Class: Queen (inherits from Piece)
Represents the queen chess piece.
Methods:
is_valid_move: Check if a move is valid for the queen.
2.7 Class: King (inherits from Piece)
Represents the king chess piece.
Methods:
is_valid_move: Check if a move is valid for the king.
is_checkmate: Check if the king is in checkmate.
is_in_check: Check if the king is in check.
is_in_check_after_move: Check if the king is in check after a hypothetical move.
3. Run Script (run.py):
3.1 Function: pieces_luncher
Initializes and returns a list of chess pieces.
3.2 Function: main
Main function to execute the chess game.
Manages player turns and game flow.
3.3 Function: end_screen
Displays the end screen with the winner and an option to play again.
3.4 Function: draw_menu
Draws the main menu screen with a start button.
3.5 Function: main_menu
Main menu loop to start the game when the start button is clicked.
3.6 __main__ Block:
Calls the main menu and then the main function.
4. Tools (tools.py):
4.1 Function: draw_board
Draws the chessboard on the screen.
4.2 Function: draw_pieces
Draws the chess pieces on the screen.
4.3 Function: find_figure
Finds a chess piece at a given row and column on the chessboard.
4.4 Function: update_display
Updates the display with the current state of the chessboard.
