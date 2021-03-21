import pygame


class Position:
    letter_association_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}  # for later
    letters = ["0", "A", "B", "C", "D", "E", "F", "G", "H"]  # idk at the moment

    def __init__(self, letter_value, ordinal_value, piece, color):
        self.letter2number_association_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        # This gives the values to the position
        self.letter = str(letter_value)
        self.number = int(ordinal_value)
        self.piece_on_me = piece
        if color:
            self.image = pygame.image.load('pictures/square_light.png')
        else:
            self.image = pygame.image.load('pictures/square_dark.png')

        self.number_reverse_value = 8 - self.number
        self.pic_x_cord = self.number_reverse_value * 80 + 10
        self.pic_y_cord = (self.letter2number_association_dictionary[letter_value] - 1) * 80 + 10

    def __str__(self):
        # Defines what should be printed when piece is printed
        if self.piece_on_me == "non":
            a1 = "|   | "
            return a1
        else:
            a1 = "|" + self.piece_on_me + "| "
            return a1

    def piece_move_away(self):
        self.piece_on_me = "non"  # makes sure that when a piece moves away, it has nothing on it

    def piece_move_on(self, piece_name):
        self.piece_on_me = piece_name  # makes sure name of piece is noted in position attributes

    def kill(self, vars_pieces_dictionary, vars_positions_dictionary, vars_dead_pieces):
        to_kill = vars_pieces_dictionary[self.piece_on_me]  # the piece that has to die
        to_kill.die(vars_pieces_dictionary, vars_positions_dictionary, vars_dead_pieces)  # calls die function of piece
