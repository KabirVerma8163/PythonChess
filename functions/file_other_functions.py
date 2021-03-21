# function to check if chosen piece is of the right color for the move
def colour_validity(team, vars_team_current):
    if team == vars_team_current:
        return True
    else:
        return False


def piece_moves_availability(vars_pieces_dictionary, vars_positions_dictionary, piece_to_be_moved):
    if piece_to_be_moved in vars_pieces_dictionary:
        piece_to_be_moved_object = vars_pieces_dictionary[piece_to_be_moved]
        possible_moves = 0

        for i in vars_positions_dictionary:
            if piece_to_be_moved_object.move_validity(vars_pieces_dictionary, vars_positions_dictionary, i):
                possible_moves += 1
                return True
    return False


# self explanatory
def print_dead_pieces(vars_dead_pieces):
    white_dead_pieces = []
    black_dead_pieces = []

    for dead_piece in vars_dead_pieces:
        if dead_piece[0] == "W":
            white_dead_pieces.append(dead_piece)
        else:
            black_dead_pieces.append(dead_piece)

    for dead_piece in white_dead_pieces:
        dead_piece = str(dead_piece)
        print(dead_piece, end=" ")
    for dead_piece in black_dead_pieces:
        dead_piece = str(dead_piece)
        print(dead_piece, end=" ")

    print("\n")


def king_move_allowed(vars_pieces_dictionary, vars_positions_dictionary, piece, place_to_be_moved_input):
    place_to_be_moved_input = str(place_to_be_moved_input.letter + str(place_to_be_moved_input.number))
    if place_to_be_moved_input in vars_positions_dictionary:
        piece_object = vars_pieces_dictionary[piece]
        if piece_object.move_validity(vars_pieces_dictionary, vars_positions_dictionary, place_to_be_moved_input):
            return False
    return True
