from classes.file_pieces_classes import *
from classes.file_position_class import *

# defining all the positions on the chessboard.
# All 8s
A8 = Position("A", 8, "BR1", True)
B8 = Position("B", 8, "BK1", False)
C8 = Position("C", 8, "BB1", True)
D8 = Position("D", 8, "BQ0", False)
E8 = Position("E", 8, "BK0", True)
F8 = Position("F", 8, "BB2", False)
G8 = Position("G", 8, "BK2", True)
H8 = Position("H", 8, "BR2", False)
# All 7s
A7 = Position("A", 7, "BP1", False)
B7 = Position("B", 7, "BP2", True)
C7 = Position("C", 7, "BP3", False)
D7 = Position("D", 7, "BP4", True)
E7 = Position("E", 7, "BP5", False)
F7 = Position("F", 7, "BP6", True)
G7 = Position("G", 7, "BP7", False)
H7 = Position("H", 7, "BP8", True)
# All 6s
A6 = Position("A", 6, "non", True)
B6 = Position("B", 6, "non", False)
C6 = Position("C", 6, "non", True)
D6 = Position("D", 6, "non", False)
E6 = Position("E", 6, "non", True)
F6 = Position("F", 6, "non", False)
G6 = Position("G", 6, "non", True)
H6 = Position("H", 6, "non", False)
# All 5s
A5 = Position("A", 5, "non", False)
B5 = Position("B", 5, "non", True)
C5 = Position("C", 5, "non", False)
D5 = Position("D", 5, "non", True)
E5 = Position("E", 5, "non", False)
F5 = Position("F", 5, "non", True)
G5 = Position("G", 5, "non", False)
H5 = Position("H", 5, "non", True)
# All 4s
A4 = Position("A", 4, "non", True)
B4 = Position("B", 4, "non", False)
C4 = Position("C", 4, "non", True)
D4 = Position("D", 4, "non", False)
E4 = Position("E", 4, "non", True)
F4 = Position("F", 4, "non", False)
G4 = Position("G", 4, "non", True)
H4 = Position("H", 4, "non", False)
# All 4s
A3 = Position("A", 3, "non", False)
B3 = Position("B", 3, "non", True)
C3 = Position("C", 3, "non", False)
D3 = Position("D", 3, "non", True)
E3 = Position("E", 3, "non", False)
F3 = Position("F", 3, "non", True)
G3 = Position("G", 3, "non", False)
H3 = Position("H", 3, "non", True)
# All 2s
A2 = Position("A", 2, "WP1", True)
B2 = Position("B", 2, "WP2", False)
C2 = Position("C", 2, "WP3", True)
D2 = Position("D", 2, "WP4", False)
E2 = Position("E", 2, "WP5", True)
F2 = Position("F", 2, "WP6", False)
G2 = Position("G", 2, "WP7", True)
H2 = Position("H", 2, "WP8", False)
# All 1s
A1 = Position("A", 1, "WR1", False)
B1 = Position("B", 1, "WK1", True)
C1 = Position("C", 1, "WB1", False)
D1 = Position("D", 1, "WQ0", True)
E1 = Position("E", 1, "WK0", False)
F1 = Position("F", 1, "WB2", True)
G1 = Position("G", 1, "WK2", False)
H1 = Position("H", 1, "WR2", True)

# The dictionary for accessing all the positions
positions_dictionary = {"A1": A1, "A2": A2, "A3": A3, "A4": A4, "A5": A5, "A6": A6, "A7": A7, "A8": A8,
                        "B1": B1, "B2": B2, "B3": B3, "B4": B4, "B5": B5, "B6": B6, "B7": B7, "B8": B8,
                        "C1": C1, "C2": C2, "C3": C3, "C4": C4, "C5": C5, "C6": C6, "C7": C7, "C8": C8,
                        "D1": D1, "D2": D2, "D3": D3, "D4": D4, "D5": D5, "D6": D6, "D7": D7, "D8": D8,
                        "E1": E1, "E2": E2, "E3": E3, "E4": E4, "E5": E5, "E6": E6, "E7": E7, "E8": E8,
                        "F1": F1, "F2": F2, "F3": F3, "F4": F4, "F5": F5, "F6": F6, "F7": F7, "F8": F8,
                        "G1": G1, "G2": G2, "G3": G3, "G4": G4, "G5": G5, "G6": G6, "G7": G7, "G8": G8,
                        "H1": H1, "H2": H2, "H3": H3, "H4": H4, "H5": H5, "H6": H6, "H7": H7, "H8": H8
                        }
dead_pieces = []  # list for all dead pieces

# All the white pawns
white_pawn1 = Pawn(1, "W", "A2")
white_pawn2 = Pawn(2, "W", "B2")
white_pawn3 = Pawn(3, "W", "C2")
white_pawn4 = Pawn(4, "W", "D2")
white_pawn5 = Pawn(5, "W", "E2")
white_pawn6 = Pawn(6, "W", "F2")
white_pawn7 = Pawn(7, "W", "G2")
white_pawn8 = Pawn(8, "W", "H2")
# All the black pawns
black_pawn1 = Pawn(1, "B", "A7")
black_pawn2 = Pawn(2, "B", "B7")
black_pawn3 = Pawn(3, "B", "C7")
black_pawn4 = Pawn(4, "B", "D7")
black_pawn5 = Pawn(5, "B", "E7")
black_pawn6 = Pawn(6, "B", "F7")
black_pawn7 = Pawn(7, "B", "G7")
black_pawn8 = Pawn(8, "B", "H7")

# White rooks
white_rook1 = Rook(1, "W", "A1")
white_rook2 = Rook(2, "W", "H1")
# Black Rooks
black_rook1 = Rook(1, "B", "A8")
black_rook2 = Rook(2, "B", "H8")

# White knights
white_knight1 = Knight(1, "W", "B1")
white_knight2 = Knight(2, "W", "G1")
# Black Knights
black_knight1 = Knight(1, "B", "B8")
black_knight2 = Knight(2, "B", "G8")

# White Bishops
white_bishop1 = Bishop(1, "W", "C1")
white_bishop2 = Bishop(2, "W", "F1")
# Black Bishops
black_bishop1 = Bishop(1, "B", "C8")
black_bishop2 = Bishop(2, "B", "F8")

white_king = King("W", "E1")
black_king = King("B", "E8")  # The kings
white_queen = Queen("W", "D1")
black_queen = Queen("B", "D8")  # The queens

# the dictionary for all the pieces
pieces_dictionary = {"WP1": white_pawn1, "WP2": white_pawn2, "WP3": white_pawn3, "WP4": white_pawn4, "WP5": white_pawn5,
                     "WP6": white_pawn6, "WP7": white_pawn7, "WP8": white_pawn8,
                     "BP1": black_pawn1, "BP2": black_pawn2, "BP3": black_pawn3, "BP4": black_pawn4, "BP5": black_pawn5,
                     "BP6": black_pawn6, "BP7": black_pawn7, "BP8": black_pawn8,
                     "WR1": white_rook1, "WR2": white_rook2, "BR1": black_rook1, "BR2": black_rook2,
                     "WK1": white_knight1, "WK2": white_knight2, "BK1": black_knight1, "BK2": black_knight2,
                     "WB1": white_bishop1, "WB2": white_bishop2, "BB1": black_bishop1, "BB2": black_bishop2,
                     "WK0": white_king, "WQ0": white_queen, "BK0": black_king, "BQ0": black_queen
                     }

black_pieces_dictionary = {"BP1": black_pawn1, "BP2": black_pawn2, "BP3": black_pawn3, "BP4": black_pawn4,
                           "BP5": black_pawn5, "BP6": black_pawn6, "BP7": black_pawn7, "BP8": black_pawn8,
                           "BR1": black_rook1, "BR2": black_rook2,
                           "BK1": black_knight1, "BK2": black_knight2,
                           "BB1": black_bishop1, "BB2": black_bishop2,
                           "BK0": black_king, "BQ0": black_queen
                           }

white_pieces_dictionary = {"WP1": white_pawn1, "WP2": white_pawn2, "WP3": white_pawn3, "WP4": white_pawn4,
                           "WP5": white_pawn5, "WP6": white_pawn6, "WP7": white_pawn7, "WP8": white_pawn8,
                           "WR1": white_rook1, "WR2": white_rook2,
                           "WK1": white_knight1, "WK2": white_knight2,
                           "WB1": white_bishop1, "WB2": white_bishop2,
                           "WK0": white_king, "WQ0": white_queen,
                           }

both_dictionaries = [pieces_dictionary, positions_dictionary]
