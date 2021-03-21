from functions.file_other_functions import colour_validity
from functions.file_other_functions import piece_moves_availability


# printing the chessboard
def chessboard(vars_counter_team, w, *args):
    counter_chessboard_newline = 0
    counter_number2 = w
    '''# global counter_team;  list_position = []; z = [""]
    # changes the side of the board.
    if counter_team % 2 != 0:
        for anything in list_position[::-1]:
            z.append(anything)
        del z[-1]
        list_position.clear()
        for anything2 in z:
            list_position.append(anything2)
    for items in args:
        list_position.append(items)'''

    # for printing the chessboard actually
    for i in args:
        item = str(i)
        if (counter_chessboard_newline % w) != 0:
            print(item, end="")
        else:
            # printing the number before the line
            print("\n")
            x = counter_number2
            if x > 0:
                print(" ", x, end=" ")
            else:
                continue
            print(item, end="")
        counter_chessboard_newline += 1
        if counter_chessboard_newline % 8 == 0:
            counter_number2 -= 1
        else:
            continue

    # prints the letter guide for the player
    print("    | A | | B | | C | | D | | E | | F | | G | | H |")
    print("This is the current chessboard")
    teams = ["W", "B"]
    if vars_counter_team % 2 == 0:
        counter_team = 0
    else:
        counter_team = 1
    vars_team_current = teams[counter_team]

    return vars_team_current


# this is to check whether th piece chosen is valid or not, returns valid piece
def piece_allowed(vars_pieces_dictionary, vars_positions_dictionary, vars_team_current, piece_to_move_input):
    while not (piece_to_move_input in vars_pieces_dictionary and
               colour_validity(piece_to_move_input[0], vars_team_current) and
               piece_moves_availability(vars_pieces_dictionary, vars_positions_dictionary, piece_to_move_input)):

        if piece_to_move_input not in vars_pieces_dictionary:  # is the piece real?
            print("Sorry there is no such piece, Please Try Again. ")
            piece_to_move_input = input("Which piece to move? ").upper().strip()

        elif not colour_validity(piece_to_move_input[0], vars_team_current):  # is the piece from thr right side
            print("Sorry the colour is wrong, Please Try Again. ")
            piece_to_move_input = input("Which piece to move? ").upper().strip()

        elif not piece_moves_availability(vars_pieces_dictionary, vars_positions_dictionary, piece_to_move_input):
            # does the piece have any valid moves?
            print("Sorry there are no available moves for this piece, Please Try Again. ")
            piece_to_move_input = input("Which piece to move? ").upper().strip()

    return piece_to_move_input


# this is to check after the piece has been verified if the move entered has been verified, to make code neater
def move_allowed(vars_pieces_dictionary, vars_positions_dictionary, piece_object, place_to_be_moved_input,
                 vars_team_current):
    while not (place_to_be_moved_input in vars_positions_dictionary and
               piece_object.move_validity(vars_pieces_dictionary, vars_positions_dictionary, place_to_be_moved_input)):

        if place_to_be_moved_input not in vars_positions_dictionary:
            print("Sorry there is no such place, Please Try Again. ")
            place_to_be_moved_input = input("Where to? ").upper().strip()

        elif not piece_object.move_validity(vars_pieces_dictionary, vars_positions_dictionary,
                                            place_to_be_moved_input):
            print("Sorry the move is invalid, Please Try Again. ")
            place_to_be_moved_input = input("Where to? ").upper().strip()

    return place_to_be_moved_input


def piece_move_input(vars_pieces_dictionary, vars_positions_dictionary, vars_team_current, vars_dead_pieces):
    piece_to_move_input = input("Which piece to move? ").upper().strip()
    piece_to_move_input = piece_allowed(vars_pieces_dictionary, vars_positions_dictionary, vars_team_current,
                                        piece_to_move_input)
    piece_object = vars_pieces_dictionary[piece_to_move_input]

    place_to_be_moved_input = str(input("Where to? ")).upper().strip()

    if place_to_be_moved_input == "CHANGEPIECE" or place_to_be_moved_input == "CP":
            piece_to_move_input = input("Which piece to move? ").upper().strip()
            piece_allowed(vars_pieces_dictionary, vars_positions_dictionary, vars_team_current, piece_to_move_input)

    place_to_be_moved_input = move_allowed(vars_pieces_dictionary, vars_positions_dictionary, piece_object,
                                           place_to_be_moved_input, vars_team_current)

    to_move = vars_positions_dictionary[place_to_be_moved_input]
    if to_move.piece_on_me == "non":
        piece_to_move = vars_pieces_dictionary[piece_to_move_input]
        piece_to_move.move(place_to_be_moved_input, vars_positions_dictionary, place_to_be_moved_input)

    else:
        to_move.kill(vars_pieces_dictionary, vars_positions_dictionary, vars_dead_pieces)
        piece_to_move = vars_pieces_dictionary[piece_to_move_input]
        piece_to_move.move(place_to_be_moved_input, vars_positions_dictionary, place_to_be_moved_input)
