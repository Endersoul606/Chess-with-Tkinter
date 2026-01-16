#=================================================================
# TO DO LIST
#=================================================================
# - En Passant
# - Make Promoting Look nicer
# - Make Command Prompt look nicer
# - Actual way to win a game rather than taking the king
# - Stalemate
# - Colour Palletes in CMD Prompt
#=================================================================
import tkinter as tk, random, time

# Variables
gm = ""
TEMP = "#FFFFFF"
COLOUR = "#FFFFFF"
selected = "#FFFFFF"
highligted = "#FFFFFF"
THEME = 0
special = 0
SIZE = 0
chess960 = False

def print_colour(text, colour="default"):
    """A way to use colours in VS CODE print statements"""
    # Colour Options
    fg_map = {"black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,}
    # Prints without colour
    if colour not in fg_map:
        print(text)
        return
    # Output
    esc, reset = f"\033[{fg_map[colour]}m", "\033[0m"
    print(f"{esc}{text}{reset}")

# Colour Functions
def ice_theme(TEMP, COLOUR, selected, highligted):
    """A toggle to change to ice theme"""
    TEMP = "#CCDEE6"
    COLOUR = "#367C8B"
    selected = "#0BA5E2"
    highligted = "#85C3EF"
    return TEMP, COLOUR, selected, highligted

def forest_theme(TEMP, COLOUR, selected, highligted):
    """A toggle to change to forest theme"""
    TEMP = "#EAEADC"
    COLOUR = "#75645D"
    selected = "#D83DE9"
    highligted = "#DF94D3"
    return TEMP, COLOUR, selected, highligted

def default_theme(TEMP, COLOUR, selected, highligted):
    """A toggle to change to default theme"""
    TEMP = "#DDDDDD"
    COLOUR = "#568B5A"
    selected = "#9BE09E"
    highligted = "#C6D37C"
    return TEMP, COLOUR, selected, highligted

def marble_theme(TEMP, COLOUR, selected, highligted):
    """A toggle to change to marble theme"""
    TEMP = "#FFFFFF"
    COLOUR = "#BCBCBC"
    selected = "#45BED1"
    highligted = "#A2E5E9"
    return TEMP, COLOUR, selected, highligted

def validate():
    """A function that checks the validation of the starting input"""

    print_colour("Enter Game Code", "cyan")
    time.sleep(0.1)
    gm = input("\033[36m>\033[0m play/live/")

    # Toggle Chess960
    if "chess960" in gm: chess960 = True
    else: chess960 = False

    # Size
    if "eS" in gm: s = 10
    elif "sS" in gm: s = 50
    elif "nS" in gm: s = 70
    elif "lS" in gm: s = 100
    else: s = 70

    # Toggle Endgame Practice
    if "endgame1" in gm: special = 1
    elif "endgame2" in gm: special = 2
    elif "endgame3" in gm: special = 3
    elif "endgame4" in gm: special = 4
    elif "endgame5" in gm: special = 5

    # Experimental Features
    elif "experimental1" in gm: special = 6
    elif "experimental2" in gm: special = 7

    else: special = 0

    # Toggle Theme
    if "ice" in gm: return 1, chess960, special, s
    elif "forest" in gm: return 2, chess960, special, s
    elif "default" in gm: return 3, chess960, special, s
    elif "marble" in gm: return 4, chess960, special, s
    else: return 0, chess960, special, s


while THEME == 0:
    try: THEME, chess960, special, SIZE = validate()
    except: pass

# Size Validation
if SIZE % 2 != 0: SIZE = 70

# Colour Pallettes
if THEME == 1: TEMP, COLOUR, selected, highligted = ice_theme(TEMP, COLOUR, selected, highligted)
elif THEME == 2: TEMP, COLOUR, selected, highligted = forest_theme(TEMP, COLOUR, selected, highligted)
elif THEME == 3: TEMP, COLOUR, selected, highligted = default_theme(TEMP, COLOUR, selected, highligted)
elif THEME == 4: TEMP, COLOUR, selected, highligted = marble_theme(TEMP, COLOUR, selected, highligted)

# Custom Positions
if special == 1:
    # Rook and King vs Rook and King
    START_POS = [
        [ 0,  0,  0,  0,  0, -4,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0, -6,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  4,  0,  0,  0,  0,  6,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],]
elif special == 2:
    # Pawn and King vs King
    START_POS = [
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0, -6,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  6,  0,  1,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],]
elif special == 3:
    # Rook and Bishop vs King
    START_POS = [
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0, -6,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  3],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  6,  0,  2,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],]
elif special == 4:
    # Rook and Bishop vs King
    START_POS = [
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0, -6,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  4],
        [ 0, -5,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  6,  1,  2,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],]
elif special == 5:
    # King and Pawns vs King and Pawns
    START_POS = [
        [ 0,  0,  0, -6,  0,  0,  0,  0],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 1,  1,  1,  1,  1,  1,  1,  1],
        [ 0,  0,  0,  0,  6,  0,  0,  0],]
elif special == 6:
    # Normal Chess against Archer
    START_POS = [
        [-4, -2, -3, -7, -6, -3, -2, -4],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 1,  1,  1,  1,  1,  1,  1,  1],
        [ 4,  2,  3,  5,  6,  3,  2,  4],]
elif special == 7:
    # Archer vs Queen
    START_POS = [
        [ 0,  0,  0,  0,  0,  0,  0,  5],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0, -6,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0, -7,  0,  0,  0,  0,  6,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],]

elif chess960:
# Initialisation
    back = [0] * 8
# Bishops (Alternate Colours)
    dark = random.choice([i for i in range(0, 8, 2)])
    light = random.choice([i for i in range(1, 8, 2)]) 
    back[dark], back[light] = -3, -3
# Queen
    empty = [i for i, p in enumerate(back) if p == 0]
    back[random.choice(empty)] = -5
# Knights
    empty = [i for i, p in enumerate(back) if p == 0]
    for _ in range(2):
        idx = random.choice(empty)
        back[idx] = -2
        empty.remove(idx)
# King (inbetween rooks)
    empty = [i for i, p in enumerate(back) if p == 0]
    empty.sort()
    back[empty[1]] = -6
# Rooks
    for i in empty:
        if back[i] == 0: back[i] = -4
# Making the board
    black_back = back
    white_back = [-p for p in black_back]
    START_POS = [black_back, [-1] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8, [1] * 8, white_back,]

else:
    # Normal Chess
    START_POS = [
        [-4, -2, -3, -5, -6, -3, -2, -4],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 1,  1,  1,  1,  1,  1,  1,  1],
        [ 4,  2,  3,  5,  6,  3,  2,  4],]

# Every piece has a custom ascii charecter
PIECE_UNICODE = {
    1:  "♙", -1: "♟",
    2:  "♘", -2: "♞",
    3:  "♗", -3: "♝",
    4:  "♖", -4: "♜",
    5:  "♕", -5: "♛",
    6:  "♔", -6: "♚",
    7:  "#", -7: "👾", # Archer (Custom Piece)
}

def on_board(r, c):
    """Returns if the piece is on the board"""; 
    return 0 <= r < 8 and 0 <= c < 8

def same_color(a, b):
    """Returns if the two pieces are same colour"""
    return a * b > 0

def pawn_moves(board, r, c):
    """All the legal moves a pawn can make"""
    piece, moves = board[r][c], []
    direction = -1 if piece > 0 else 1          # White moves up, Black moves down
    start_row = 6 if piece > 0 else 1

    # Adds the move in front of it if it is a legit move
    if on_board(r + direction, c) and board[r + direction][c] == 0:
        moves.append((r + direction, c))
        # Doublemoving
        if r == start_row and board[r + 2 * direction][c] == 0:
            moves.append((r + 2 * direction, c))

    # Capturing
    for dc in (-1, 1):
        nr, nc = r + direction, c + dc
        if on_board(nr, nc) and board[nr][nc] != 0 and not same_color(piece, board[nr][nc]):
            moves.append((nr, nc))
    # Returns all legit moves
    return moves

def knight_moves(board, r, c):
    """All the legal moves a knight can make"""
    piece = board[r][c]
    # Deltas are the offsets that the piece can move to
    deltas, moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)], []
    # For each offset, check if it is a possible move (not moving onto one of your pieces and it being on the board)
    for dr, dc in deltas:
        nr, nc = r+dr, c+dc
        if on_board(nr, nc) and (board[nr][nc] == 0 or not same_color(piece, board[nr][nc])): moves.append((nr, nc))
    # Return all legit moves
    return moves

def sliding_moves(board, r, c, directions):
    """A function that calculates all the moves you can make in a given direction"""
    piece, moves = board[r][c], []
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        while on_board(nr, nc):
            if board[nr][nc] == 0: moves.append((nr, nc))
            elif not same_color(piece, board[nr][nc]):
                moves.append((nr, nc))
                break
            else: break
            nr += dr; nc += dc
    return moves

def bishop_moves(board, r, c):
    """All the legal moves a bishop can make"""
    # Goes through sliding_moves with diagonal delti
    return sliding_moves(board, r, c, [(-1,-1),(-1,1),(1,-1),(1,1)])

def rook_moves(board, r, c):
    """All the legal moves a rook can make"""
    # Goes through sliding_moves with horizontal and vertical delti
    return sliding_moves(board, r, c, [(-1,0),(1,0),(0,-1),(0,1)])

def queen_moves(board, r, c):
    """All the legal moves a queen can make"""
    # Queen has the list of moves the rook can move to and the bishop
    return bishop_moves(board, r, c) + rook_moves(board, r, c)

def archer_moves(board, r, c):
    """All the legal moves an archer can make"""
    # Archer has the list of moves the rook can move to and the knight
    return knight_moves(board, r, c) + rook_moves(board, r, c)

def king_moves(board, r, c):
    """All the legal moves a king can make"""
    piece = board[r][c]
    # Deltas are the offsets that the piece can move to
    deltas, moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)], []
    # For each offset, check if it is a possible move (not moving onto one of your pieces and it being on the board)
    for dr, dc in deltas:
        nr, nc = r+dr, c+dc
        if on_board(nr, nc) and (board[nr][nc] == 0 or not same_color(piece, board[nr][nc])): moves.append((nr, nc))
    # Return all legit moves
    return moves

def legal_moves(board, r, c):
    """All the legal moves that a piece can make"""
    piece = board[r][c]
    if piece == 0: return []
    t = abs(piece)
    if t == 1: return pawn_moves(board, r, c)
    if t == 2: return knight_moves(board, r, c)
    if t == 3: return bishop_moves(board, r, c)
    if t == 4: return rook_moves(board, r, c)
    if t == 5: return queen_moves(board, r, c)
    if t == 6: return king_moves(board, r, c)
    if t == 7: return archer_moves(board, r, c)

def find_king(board, color):
    """Scans through squares on the board till it finds the king"""
    king_code = 6 * color
    for r in range(8):
        for c in range(8):
            if board[r][c] == king_code: return r, c
    # Only triggers if there is no king, so the other side wins
    try: root.destroy()
    # Invalid Position means no king so there would be an error as no tkinter window would exist
    except: print_colour("Not a valid position", "red")
    time.sleep(0.1)
    print_colour(f"{"White" if color == -1 else "Black"} Wins", "magenta")  
    time.sleep(3)


def is_in_check(board, color):
    """A function to find out if you are in check"""
    king_pos = find_king(board, color)
    if not king_pos: return False
    kr, kc = king_pos
    opponent = -color
    # For each opponent piece, if taking king is a legit move for them then it is in check
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != 0 and (piece * opponent) > 0:
                if (kr, kc) in legal_moves(board, r, c): return True
    return False


class ChessGUI:

    def toggledoubleLock(self, event):
        """A toggle for toggling cheats"""
        self.doublelocked = not(self.doublelocked)

    def toggleLock(self, event):
        """A toggle for cheats"""
        if self.doublelocked == False: self.locked = not(self.locked)
        return

    def cmdPrompt(self, event):
        """A Command Pannel that lets you input commands"""
        # Lock
        if self.doublelocked == True:
            print_colour("No Administrater Commands Available in this Mode", "red")
            return
        elif self.locked == True:
            print_colour("No Administrator Commands Available in this Mode", "red")
            return
        
        # Input
        try:
            print_colour("Enter a command", "green")
            cmd = input("\033[32m> \033[0m")
        except: return

        # Colour Pallete Changing
        if "ice" in cmd:
            print_colour("Ice Theme Selected", "cyan")
            self.toggleIceTheme = True
            self.toggleForestTheme = False
            self.toggleMarbleTheme = False
            self.toggleDefaultTheme = False
            TEMP = COLOUR = selected = highligted = "#FFFFFF"
            TEMP, COLOUR, selected, highligted = ice_theme(TEMP, COLOUR, selected, highligted)
            self.draw_board()

        elif "forest" in cmd:
            print_colour("Forest Theme Selected", "green")
            self.toggleIceTheme = False
            self.toggleForestTheme = True
            self.toggleMarbleTheme = False
            self.toggleDefaultTheme = False
            TEMP = COLOUR = selected = highligted = "#FFFFFF"
            TEMP, COLOUR, selected, highligted = forest_theme(TEMP, COLOUR, selected, highligted)
            self.draw_board()

        elif "default" in cmd:
            print_colour("Default Theme Selected", "magenta")
            self.toggleIceTheme = False
            self.toggleForestTheme = False
            self.toggleMarbleTheme = False
            self.toggleDefaultTheme = True
            TEMP = COLOUR = selected = highligted = "#FFFFFF"
            TEMP, COLOUR, selected, highligted = default_theme(TEMP, COLOUR, selected, highligted)
            self.draw_board()

        elif "marble" in cmd:
            print_colour("Marble Theme Selected", "yellow")
            self.toggleIceTheme = False
            self.toggleForestTheme = False
            self.toggleMarbleTheme = True
            self.toggleDefaultTheme = False
            TEMP = COLOUR = selected = highligted = "#FFFFFF"
            TEMP, COLOUR, selected, highligted = marble_theme(TEMP, COLOUR, selected, highligted)
            self.draw_board()
        else: pass

        # Refresh Castling
        if "refreshCastling" in cmd:
            if cmd[0] == "-": self.has_castled2 = False
            elif cmd[0] == "+": self.has_castled = False
            else: return

        # Validation
        if len(cmd) < 4: return
        else:
            # Piece Colour
            if cmd[0] == "-": colMultiply = -1
            elif cmd[0] == "+": colMultiply = 1
            else: return
            # Piece Used
            if cmd[1] == "K": p = (6 * colMultiply)
            elif cmd[1] == "Q": p = (5 * colMultiply)
            elif cmd[1] == "R": p = (4 * colMultiply)
            elif cmd[1] == "B": p = (3 * colMultiply)
            elif cmd[1] == "N": p = (2 * colMultiply)
            elif cmd[1] == "P": p = (1 * colMultiply)
            elif cmd[1] == "A": p = (7 * colMultiply)
            # No Piece = Blank Space (Delete Square)
            else: p = 0
            # Coords
            try:
                l = cmd[2]
                # String to Int Converter
                if l == "a": l = 0
                elif l == "b": l = 1
                elif l == "c": l = 2
                elif l == "d": l = 3
                elif l == "e": l = 4
                elif l == "f": l = 5
                elif l == "g": l = 6
                elif l == "h": l = 7             
                else: return

                r = 7 - (int(cmd[3]) - 1)
                self.board[r][l] = p
                self.draw_board()
            # Validation
            except: return

    # Castling
    def castle_wk(self, event):
        """White Castling Kingside"""
        # Once per game
        if (self.has_castled == False) and (self.board[7][4]==6)and(self.board[7][5]==0)and(self.board[7][6]==0)and(self.board[7][7]==4):
            self.has_castled = True
            # Updates the position
            self.board[7][4] = 0
            self.board[7][5] = 4
            self.board[7][6] = 6
            self.board[7][7] = 0
            # Renders the board
            self.draw_board()
            return
        else: return

    def castle_bk(self, event):
        """Black Castling Kingside"""
        # Once per game
        if (self.has_castled2 == False) and (self.board[0][4]==-6)and(self.board[0][5]==0)and(self.board[0][6]==0)and(self.board[0][7]==-4):
            self.has_castled2 = True
            # Updates the position
            self.board[0][4] = 0
            self.board[0][5] = -4
            self.board[0][6] = -6
            self.board[0][7] = 0
            # Renders the board
            self.draw_board()
            return
        else: return

    def castle_wq(self, event):
        """White Castling Queenside"""
        # Once per game
        if (self.has_castled == False) and (self.board[7][4]==6)and(self.board[7][3]==0)and(self.board[7][2]==0)and(self.board[7][1]==0)and(self.board[7][0]==4):
            self.has_castled = True
            # Updates the position
            self.board[7][0] = 0
            self.board[7][1] = 0
            self.board[7][2] = 6
            self.board[7][3] = 4
            self.board[7][4] = 0
            # Renders the board
            self.draw_board()
            return
        else: return

    def castle_bq(self, event):
        """Black Castling Queenside"""
        # Once per game
        if (self.has_castled2 == False) and (self.board[0][4]==-6)and(self.board[0][3]==0)and(self.board[0][2]==0)and(self.board[0][1]==0)and(self.board[0][0]==-4):
            self.has_castled2 = True
            # Updates the position
            self.board[0][0] = 0
            self.board[0][1] = 0
            self.board[0][2] = -6
            self.board[0][3] = -4
            self.board[0][4] = 0
            # Renders the board
            self.draw_board()
            return
        else: return

    def __init__(self, master):
        """Initialisation"""
        self.master = master

        # Toggle Themes
        self.toggleIceTheme = False
        self.toggleDefaultTheme = False
        self.toggleMarbleTheme = False
        self.toggleForestTheme = False

        # Drawing the Chess Board
        self.board = [row[:] for row in START_POS]
        self.selected = None
        self.squares = [[None]*8 for _ in range(8)]
        self.canvas = tk.Canvas(master, width = SIZE*8, height = SIZE*8)
        self.canvas.pack()
        self.locked = False
        self.doublelocked = False
        self.draw_board()

        # Binding
        self.canvas.bind("<Button-1>", self.on_click)
        root.bind("<[>", self.toggledoubleLock)
        root.bind("<]>", self.toggleLock)
        root.bind("<#>", self.cmdPrompt)

        # Castling
        self.has_castled = False
        self.has_castled2 = False
        root.bind("<o>", self.castle_bk)
        root.bind("<l>", self.castle_wk)
        root.bind("<i>", self.castle_bq)
        root.bind("<k>", self.castle_wq)

    def draw_board(self):
        """A function that uses renders the chessboard"""
        self.canvas.delete("all")
        size = SIZE
        # Makes the boxes
        for r in range(8):
            for c in range(8):
                x1, y1 = c*size, r*size
                x2, y2 = x1+size, y1+size
                colour = str(TEMP) if (r+c) % 2 == 0 else str(COLOUR)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=colour, tags="sq")
                # Makes the pieces using text
                piece = self.board[r][c]
                if piece != 0: self.canvas.create_text(x1+size/2, y1+size/2, text=PIECE_UNICODE[piece], font=("Helvetica", int((SIZE + 4) / 2)), tags="piece")
        
        # When the piece is selected to move
        if self.selected:
            r, c = self.selected
            # Highlights the piece
            self.highlight_square(r, c, str(selected))
            # Highlights all legal squares in a dif colour
            for nr, nc in self.legal: self.highlight_square(nr, nc, str(highligted))
        
        # Is white king in check?
        if is_in_check(self.board, 1):
            kr, kc = find_king(self.board, 1)
            self.highlight_square(kr, kc, "#E55151")

        # Is black king in check?
        if is_in_check(self.board, -1):
            kr, kc = find_king(self.board, -1)
            self.highlight_square(kr, kc, "#E55151")

    # Function that highlights the squares with the colour
    def highlight_square(self, r, c, colour):
        size = SIZE
        x1, y1 = c*size, r*size
        x2, y2 = x1+size, y1+size
        self.canvas.create_rectangle(x1, y1, x2, y2, outline=colour, width=3, tags="highlight")

    def on_click(self, event):
        size = SIZE
        col = event.x // size
        row = event.y // size
        if not on_board(row, col): return

        if self.selected:
            # If you are trying to move a piece
            if (row, col) in self.legal:
                sr, sc = self.selected
                moving_piece = self.board[sr][sc]
                self.board[row][col] = moving_piece
                self.board[sr][sc] = 0

            # Promotes to a piece
                if (abs(moving_piece) == 1) or (abs(moving_piece) == -1):                     
                    if (moving_piece > 0 and row == 0) or (moving_piece < 0 and row == 7):
                        # colourMultiplier is Black / White
                        if moving_piece < 0: colourMultiplier = -1
                        else: colourMultiplier = 1
                        # Input
                        print_colour("What piece do u want to promote to? ", "cyan")
                        promote = input("\033[36m> \033[0m")
                        # Promotion
                        if promote == "Rook": self.board[row][col] = (4 * colourMultiplier)
                        elif promote == "Bishop": self.board[row][col] = (3 * colourMultiplier)
                        elif promote == "Knight": self.board[row][col] = (2 * colourMultiplier)
                        elif promote == "Queen": self.board[row][col] = (5 * colourMultiplier)
                        # Archer should only be a valid option if you are playing with it
                        elif (promote == "Archer") and (colourMultiplier < 0) and (special == 6): self.board[row][col] = (-7)
                        # Else is just a random piece
                        else: self.board[row][col] = (random.randint(2,5) * colourMultiplier)

            self.selected = None
            self.legal = []
            self.draw_board()

        else:
            # Before you select a piece
            piece = self.board[row][col]
            if piece == 0: return
            self.selected = (row, col)
            self.legal = legal_moves(self.board, row, col)
            self.draw_board()

root = tk.Tk()
root.title("Tkinter Chess")
ChessGUI(root)
root.mainloop()