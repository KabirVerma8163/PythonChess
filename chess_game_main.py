# print('''
# |               |   ||||||||||||||||   ||              ||               ||||||||||||||
# |               |   |||                ||              ||               ||          ||
# |               |   |||                ||              ||               ||          ||
# |||||||||||||||||   |||||||||||||||    ||              ||               ||          ||
# |||||||||||||||||   |||||||||||||||    ||              ||               ||          ||
# |               |   |||                ||              ||               ||          ||
# |               |   |||                ||              ||               ||          ||
# |               |   |||||||||||||||    ||||||||||||||  ||||||||||||||   ||||||||||||||
# ''')
# input("\n\n press enter to exit")
from modules.all_objects_module import *
from functions.file_main_functions import chessboard
from functions.file_main_functions import piece_move_input
from functions.file_other_functions import print_dead_pieces
"""
Some ground rules,
1. Whenever u need a dictionary from a program, use the the both_dictionaries list
2. When u need to add something in a function, make it in the following order
    a.Dictionaries/lists - Array
    b.Objects
    c.Boolean
    d.Integers
    e.Strings
"""


teams = ["W", "B"]
counter_move = 0
if counter_move % 2 == 0:
    counter_team = 0
else:
    counter_team = 1
team_current = teams[counter_team]

print(
    """
Here are some ground rules for the game, for now you are gonna have to the honours of killing the king
    """
)


# the loop that is meant to keep printing the chessboard again and again till either king dies
while white_king.alive and black_king.alive:
    team_current = chessboard(counter_move, 8, A8, B8, C8, D8, E8, F8, G8, H8,
                              A7, B7, C7, D7, E7, F7, G7, H7,
                              A6, B6, C6, D6, E6, F6, G6, H6,
                              A5, B5, C5, D5, E5, F5, G5, H5,
                              A4, B4, C4, D4, E4, F4, G4, H4,
                              A3, B3, C3, D3, E3, F3, G3, H3,
                              A2, B2, C2, D2, E2, F2, G2, H2,
                              A1, B1, C1, D1, E1, F1, G1, H1, " ")

    # to ask the player to move a piece to some place
    piece_move_input(pieces_dictionary, positions_dictionary, team_current, dead_pieces)
    counter_move += 1

# thi final chess board after one side wins
chessboard(counter_team, 8, A8, B8, C8, D8, E8, F8, G8, H8,
           A7, B7, C7, D7, E7, F7, G7, H7,
           A6, B6, C6, D6, E6, F6, G6, H6,
           A5, B5, C5, D5, E5, F5, G5, H5,
           A4, B4, C4, D4, E4, F4, G4, H4,
           A3, B3, C3, D3, E3, F3, G3, H3,
           A2, B2, C2, D2, E2, F2, G2, H2,
           A1, B1, C1, D1, E1, F1, G1, H1, " ")

# the statement that prints the name of thw winner
if "WK0" in pieces_dictionary:
    print("A king, the black king, has died and so the game has ended, therefore white wins")
else:
    print("A king, the white king, has died and so the game has ended, therefore black wins")

print_dead_pieces(dead_pieces)

input("\n\n\nPress enter to exit ")
