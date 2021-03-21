# noinspection PyUnusedLocal
class Piece:  # the super class for all the pieces on the board
    first_move_counter = 0

    def __init__(self, number, color, start_location, letter):
        number = str(number)
        # setting attributes for each piece
        self.team = color
        self.name = color + letter + number
        self.start_column = start_location[0]
        self.start_row = start_location[-1]
        self.location_me = start_location
        self.alive = True
        self.letter_2_number_association_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        self.number_2_letter_association_list = ["0", "A", "B", "C", "D", "E", "F", "G", "H"]
        self.piece_moved_state = False

    def __str__(self):
        a = self.name + self.location_me
        return a

    '''def __del__(self): \n print("Piece ", self.name, " is no longer in the game.")'''  # didn't work

    def die(self, vars_pieces_dictionary, vars_positions_dictionary, vars_dead_pieces):
        vars_dead_pieces.append(self.name)
        vars_pieces_dictionary.pop(self.name)  # delete from PositionDict, so there is no access to it
        self.alive = False                     # kills it

    def move(self, vars_pieces_dictionary, vars_positions_dictionary, location_goto):
        vars_positions_dictionary[self.location_me].piece_move_away()  # tells the position piece has moved away
        self.location_me = location_goto  # makes the current location of piece
        vars_positions_dictionary[self.location_me].piece_move_on(self.name)  # tells new position abt its arrival
        self.first_move_counter += 1  # Mainly for the pawns, rooks & kings(castling)

    @staticmethod
    def all_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        # same for all pieces
        location_me = piece.location_me
        team = piece.team
        location_goto = vars_positions_dictionary[location_goto_input]
        ''' The arguments this functions can be shortened take note of this '''

        if location_goto_input in vars_positions_dictionary:  # if place is real
            if location_goto_input != location_me:             # location is different from current
                if location_goto.piece_on_me[0] != team:       # not killing a piece of the same team
                    return True
        return False

    @staticmethod
    def specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        pass

    def move_validity(self, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        return Piece.all_move_validity(self, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input)and\
            self.specific_piece_move_validity(self, vars_pieces_dictionary, vars_positions_dictionary,
                                              location_goto_input)



# noinspection PyUnusedLocal
class Pawn(Piece):

    def __init__(self, number, color, start_location):
        super().__init__(number, color, start_location, "P")

    @staticmethod
    def specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        location_goto_object = vars_positions_dictionary[location_goto_input]
        if piece.team == "W":  # checks color of piece
            if int(location_goto_input[-1]) > int(piece.location_me[-1]):  # checks how far it is moving
                location_me = int(piece.location_me[-1])
                location_goto_number = int(location_goto_input[-1])
                location_difference = abs(location_goto_number - location_me)

                loc_me_ltr = piece.location_me[0]
                loc_goto_ltr = location_goto_input[0]
                loc_me_ltr_number = int(piece.letter_2_number_association_dictionary[loc_me_ltr])
                loc_goto_ltr_number = int(piece.letter_2_number_association_dictionary[loc_goto_ltr])
                ltr_num_diff = abs(loc_me_ltr_number - loc_goto_ltr_number)

                if location_goto_input[0] == piece.start_column:
                    if piece.first_move_counter == 0:  # checks if it is the first move
                        if location_difference == 2:  # if 2 spaces
                            if piece.check_path_open(vars_pieces_dictionary, vars_positions_dictionary,
                                                     location_goto_input):  # no piece in font of it
                                return True
                        elif location_difference == 1:  # if difference is 1 space
                            if location_goto_object.piece_on_me == "non":
                                return True
                    else:
                        if location_difference == 1:
                            if location_goto_object.piece_on_me == "non":
                                return True
                elif ltr_num_diff == 1:
                    if location_difference == 1:
                        if not location_goto_object.piece_on_me == "non":
                            piece_now = vars_pieces_dictionary[location_goto_object.piece_on_me]
                            if piece_now.team == "B":
                                return True

        else:  # for black team pieces, rest is similar
            if int(location_goto_input[-1]) < int(piece.location_me[-1]):
                location_me_number = int(piece.location_me[-1])
                location_goto_number = int(location_goto_input[-1])
                location_difference = abs(location_me_number - location_goto_number)

                loc_me_ltr = piece.location_me[0]
                loc_goto_ltr = location_goto_input[0]
                loc_me_ltr_number = int(piece.letter_2_number_association_dictionary[loc_me_ltr])
                loc_goto_ltr_number = int(piece.letter_2_number_association_dictionary[loc_goto_ltr])
                ltr_num_diff = abs(loc_me_ltr_number - loc_goto_ltr_number)
                num_diff = abs(loc_me_ltr_number - loc_goto_ltr_number)

                location_me = int(piece.location_me[-1])
                location_goto_number = int(location_goto_input[-1])
                location_difference = abs(location_goto_number - location_me)

                loc_me_ltr = piece.location_me[0]
                loc_goto_ltr = location_goto_input[0]
                loc_me_ltr_number = int(piece.letter_2_number_association_dictionary[loc_me_ltr])
                loc_goto_ltr_number = int(piece.letter_2_number_association_dictionary[loc_goto_ltr])
                ltr_num_diff = abs(loc_me_ltr_number - loc_goto_ltr_number)
                if location_goto_input[0] == piece.start_column:
                    if piece.first_move_counter == 0:  # checks if it is the first move
                        if location_difference == 2:  # if 2 spaces
                            if piece.check_path_open(vars_pieces_dictionary, vars_positions_dictionary,
                                                     location_goto_input):  # no piece in font of it
                                return True
                        elif location_difference == 1:  # if difference is 1 space
                            if location_goto_object.piece_on_me == "non":
                                return True
                    else:
                        if location_difference == 1:
                            if location_goto_object.piece_on_me == "non":
                                return True
                elif ltr_num_diff == 1:
                    if location_difference == 1:
                        if not location_goto_object.piece_on_me == "non":
                            piece_now = vars_pieces_dictionary[location_goto_object.piece_on_me]
                            if piece_now.team == "W":
                                return True
        return False

    def check_path_open(self, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        location_me = self.location_me
        location_me_num = abs(int(location_me[-1]))
        if self.team == "W":
            location_check1_num = location_me_num + 1
            location_check1 = str(location_me[0]) + str(location_check1_num)
            location_check1_object = vars_positions_dictionary[location_check1]
            if location_check1_object.piece_on_me != "non":
                return False

            location_check2_num = location_me_num + 2
            location_check2 = str(location_me[0]) + str(location_check2_num)
            location_check2_object = vars_positions_dictionary[location_check2]
            if location_check2_object.piece_on_me != "non":
                return False
            return True
        else:
            location_check1_num = location_me_num - 1
            location_check1 = str(location_me[0]) + str(location_check1_num)
            location_check1_object = vars_positions_dictionary[location_check1]
            if not location_check1_object.piece_on_me == "non":
                return False

            location_check2_num = location_me_num - 2
            location_check2 = str(location_me[0]) + str(location_check2_num)
            location_check2_object = vars_positions_dictionary[location_check2]
            if not location_check2_object.piece_on_me == "non":
                return False
            return True


class Rook(Piece):
    def __init__(self, number, color, start_location):
        super().__init__(number, color, start_location, "R")

    @staticmethod  # needed for the queen
    def specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        location_me = piece.location_me
        if location_goto_input[0] == location_me[0] or location_goto_input[-1] == location_me[-1]:
            if piece.check_path_open(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
                return True
        return False

    # not used anywhere rn
    # noinspection PyUnusedLocal
    @staticmethod
    def check_path_open(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        loc_goto_ltr = location_goto_input[0]
        loc_me_ltr = piece.location_me[0]
        loc_goto_number = int(location_goto_input[-1])
        loc_me_number = int(piece.location_me[-1])
        loc_goto_ltr_number = abs(piece.letter_2_number_association_dictionary[loc_goto_ltr])
        loc_me_ltr_number = abs(piece.letter_2_number_association_dictionary[loc_me_ltr])
        counter_ltr = loc_me_ltr_number - loc_goto_ltr_number
        counter_number = loc_goto_number - loc_me_number
        if counter_number >= 0:
            a = 1
        else:
            a = -1

        if counter_ltr >= 0:
            b = 1
        else:
            b = -1
        counter_number = abs(counter_number)
        counter_ltr = abs(counter_ltr)
        counter = 1
        if loc_goto_ltr == loc_me_ltr:
            while counter < counter_number:
                loc_me_number += a
                location_check = str(str(loc_me_ltr) + str(loc_me_number))
                location_check_object = vars_positions_dictionary[location_check]
                counter += 1
                if not location_check_object.piece_on_me == "non":
                    return False
        elif loc_goto_number == loc_me_number:
            while counter > counter_ltr:
                loc_me_ltr_number += b
                print(loc_me_ltr_number)
                loc_me_ltr = piece.number_2_letter_association_list[loc_me_ltr_number]
                location_check = str(str(loc_me_ltr) + str(loc_me_number))
                location_check_object = vars_positions_dictionary[location_check]
                counter += 1
                if not location_check_object.piece_on_me == "non":
                    return False
        return True


class Bishop(Piece):
    def __init__(self, number, color, start_location):
        super().__init__(number, color, start_location, "B")

    @staticmethod  # needed for the queen
    def specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        location_me = piece.location_me
        letter_2_number_association_dictionary = piece.letter_2_number_association_dictionary
        # number_2_letter_association_list = piece.number_2_letter_association_list

        location_me_int = int(letter_2_number_association_dictionary[location_me[0]])
        difference1 = int(letter_2_number_association_dictionary[location_goto_input[0]]) - location_me_int
        difference2 = int(location_goto_input[-1]) - int(location_me[-1])
        if abs(difference1) == abs(difference2):
            return piece.check_path_open(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input)
        return False

    # noinspection PyUnusedLocal
    @staticmethod
    def check_path_open(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        # the comments are for the goto-location B3 and current-location G5
        loc_goto_ltr = location_goto_input[0]  # B - the letter value of the goto location
        loc_me_ltr = piece.location_me[0]  # G - the letter value of the current location
        loc_goto_number = int(location_goto_input[-1])  # 3 - the number value of the goto location
        loc_me_number = int(piece.location_me[-1])  # 5 - the number value of the current location
        loc_goto_ltr_number = abs(int(piece.letter_2_number_association_dictionary[loc_goto_ltr]))
        # 2 - the num equivalent of goto ltr
        loc_me_ltr_number = abs(int(piece.letter_2_number_association_dictionary[loc_me_ltr]))
        # 7 - the num equivalent of current ltr
        counter_ltr = abs(
            loc_me_ltr_number - loc_goto_ltr_number)  # the abs diff. between the num values of the ltr-nums
        counter_number = abs(loc_goto_number - loc_me_number)  # the abs diff. between the num values of the num-nums
        counter2 = counter_number
        counter = 1

        if loc_goto_number > loc_me_number and loc_goto_ltr_number > loc_me_ltr_number:
            while counter2 > counter:
                loc_check_number = str(loc_me_number + 1)
                loc_check_ltr = str(piece.number_2_letter_association_list[loc_me_ltr_number + 1])
                loc_check_value = loc_check_ltr + loc_check_number
                if loc_check_value in vars_positions_dictionary:
                    loc_check = vars_positions_dictionary[loc_check_value]
                    if loc_check.piece_on_me != "non":
                        return False
                    counter += 1

        elif loc_goto_ltr_number < loc_me_ltr_number and loc_goto_number < loc_me_number:
            while counter2 > counter:
                loc_check_number = str(loc_me_number - 1)
                loc_check_ltr = str(piece.number_2_letter_association_list[loc_me_ltr_number - 1])
                loc_check_value = loc_check_ltr + loc_check_number
                if loc_check_value in vars_positions_dictionary:
                    loc_check = vars_positions_dictionary[loc_check_value]
                    if loc_check.piece_on_me != "non":
                        return False
                    counter += 1

        elif loc_goto_ltr_number > loc_me_ltr_number and loc_goto_number < loc_me_number:
            while counter2 > counter:
                loc_check_number = str(loc_me_number - 1)
                loc_check_ltr = str(piece.number_2_letter_association_list[loc_me_ltr_number + 1])
                loc_check_value = loc_check_ltr + loc_check_number
                if loc_check_value in vars_positions_dictionary:
                    loc_check = vars_positions_dictionary[loc_check_value]
                    if loc_check.piece_on_me != "non":
                        return False
                    counter += 1

        elif loc_goto_ltr_number < loc_me_ltr_number and loc_goto_number > loc_me_number:
            while counter2 > counter:
                loc_check_number = str(loc_me_number + 1)
                loc_check_ltr = str(piece.number_2_letter_association_list[loc_me_ltr_number - 1])
                loc_check_value = loc_check_ltr + loc_check_number
                if loc_check_value in vars_positions_dictionary:
                    loc_check = vars_positions_dictionary[loc_check_value]
                    if loc_check.piece_on_me != "non":
                        return False
                    counter += 1
        return True


class Knight(Piece):
    def __init__(self, number, color, start_location):
        super().__init__(number, color, start_location, "K")

    @staticmethod  # not needed for the queen, but uniformity
    def specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        location_me = piece.location_me
        letter_2_number_association_dictionary = piece.letter_2_number_association_dictionary

        location_goto_letter_number = int(letter_2_number_association_dictionary[location_goto_input[0]])
        location_goto_ordinal_number = int(location_goto_input[-1])
        location_me_letter_number = int(letter_2_number_association_dictionary[location_me[0]])
        location_me_ordinal_number = int(location_me[-1])

        if abs(location_goto_ordinal_number - location_me_ordinal_number) == 2 and \
                abs(location_goto_letter_number - location_me_letter_number) == 1:
            return True
        elif abs(location_goto_letter_number - location_me_letter_number) == 2 and \
                abs(location_goto_ordinal_number - location_me_ordinal_number) == 1:
            return True
        return False

    @staticmethod
    def check_path_open(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        return True


class King(Piece):
    def __init__(self, color, start_location):
        super().__init__(0, color, start_location, "K")

    @staticmethod  # not needed for the queen, but uniformity, Again
    def specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        letter_2_number_association_dictionary = piece.letter_2_number_association_dictionary
        location_me = piece.location_me

        location_goto_letter_number = int(letter_2_number_association_dictionary[location_goto_input[0]])
        location_goto_ordinal_number = int(location_goto_input[-1])
        location_me_letter_number = int(letter_2_number_association_dictionary[location_me[0]])
        location_me_ordinal_number = int(location_me[-1])
        difference1 = location_goto_letter_number - location_me_letter_number
        difference2 = location_goto_ordinal_number - location_me_ordinal_number
        if abs(difference2) <= 1 and abs(difference1) <= 1:
            return piece.check_path_open(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input)
        return False

    @staticmethod
    def check_path_open(piece, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        from functions.file_other_functions import king_move_allowed
        location_goto_object = vars_positions_dictionary[location_goto_input]

        if piece.team == "W":
            from modules.all_objects_module import black_pieces_dictionary
            for p in black_pieces_dictionary:
                if not king_move_allowed(vars_pieces_dictionary, vars_positions_dictionary, p, location_goto_object):
                    return False
        else:
            from modules.all_objects_module import white_pieces_dictionary
            for p in white_pieces_dictionary:
                if not king_move_allowed(vars_pieces_dictionary, vars_positions_dictionary, p, location_goto_object):
                    return False
        return True


class Queen(Piece):
    def __init__(self, color, start_location):
        super().__init__(0, color, start_location, "Q")

    @staticmethod
    def specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary,
                                     location_goto_input):
        return Rook.specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary,
                                                 location_goto_input) or\
                Bishop.specific_piece_move_validity(piece, vars_pieces_dictionary, vars_positions_dictionary,
                                                    location_goto_input)

    @staticmethod
    def check_path_open(self, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input):
        return Rook.check_path_open(self, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input) and\
               Bishop.check_path_open(self, vars_pieces_dictionary, vars_positions_dictionary, location_goto_input)
