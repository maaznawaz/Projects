import pygame, random

class Player:
    def __init__(self, color:str):
        self.color = color
        self.in_check = False


class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    
    def make_move(self, game, coordinates):
        en_passant_moves_list = []
        if self.color == "white":
            for piece in game.piece_list:
                if game.selection.__str__().endswith("King") and abs(game.selection.pos[0] - coordinates[0]) == 200 and coordinates == [600, 800]: # white king side castle
                    if piece.__str__().endswith("Rook") and piece.pos == [700, 800]:
                        piece.pos = [500, 800]
                if game.selection.__str__().endswith("King") and abs(game.selection.pos[0] - coordinates[0]) == 200 and coordinates == [200, 800]: # white queen side castle
                    if piece.__str__().endswith("Rook") and piece.pos == [0, 800]:
                        piece.pos = [300, 800]
                if piece.__str__().endswith("Pawn"):
                    # checking if any pawns are able to be captured via en_passant
                    if piece.color == "black" and piece.en_passant_available == True:
                        en_passant_moves_list.append(piece)
                if coordinates == piece.pos and piece.color == "black":
                    piece.captured = True
                    piece.pos = None
                    game.captured_list.append(piece)
                    game.piece_list.remove(piece)
        if self.color == "black":
            for piece in game.piece_list:
                if game.selection.__str__().endswith("King") and abs(game.selection.pos[0] - coordinates[0]) == 200 and coordinates == [600, 100]: # black king side castle
                    if piece.__str__().endswith("Rook") and piece.pos == [700, 100]:
                        piece.pos = [500, 100]
                if game.selection.__str__().endswith("King") and abs(game.selection.pos[0] - coordinates[0]) == 200 and coordinates == [200, 100]: # black queen side castle
                    if piece.__str__().endswith("Rook") and piece.pos == [0, 100]:
                        piece.pos = [300, 100]
                if piece.__str__().endswith("Pawn"):
                    if piece.color == "white" and piece.en_passant_available == True:
                        en_passant_moves_list.append(piece)
                if coordinates == piece.pos and piece.color == "white":
                    piece.captured = True
                    piece.pos = None
                    game.captured_list.append(piece)
                    game.piece_list.remove(piece)
        if game.selection.__str__().endswith("Pawn"): # checking for pawns for en passant moves
            if self.color == "white" and game.selection.pos[1] == 400 and abs(coordinates[0] - game.selection.pos[0]) == 100:
                for piece in en_passant_moves_list:
                    if piece.pos[1] == 400 and piece.pos[0] == coordinates[0]:
                        piece.captured = True
                        piece.pos = None
                        game.captured_list.append(piece)
                        game.piece_list.remove(piece)
            if self.color == "black" and game.selection.pos[1] == 500 and abs(coordinates[0] - game.selection.pos[0]) == 100:
                for piece in en_passant_moves_list:
                    if piece.pos[1] == 500 and piece.pos[0] == coordinates[0]:
                        piece.captured = True
                        piece.pos = None
                        game.captured_list.append(piece)
                        game.piece_list.remove(piece)
            if abs(game.selection.pos[1] - coordinates[1]) == 200:
                game.selection.en_passant_available = True

        game.selection.pos = coordinates

        for piece in en_passant_moves_list:
            piece.en_passant_available = False
        if game.selection.__str__().endswith("King") or game.selection.__str__().endswith("Rook"):
            game.selection.castle = False

    def player_selection(self, coordinates, game):
        if self.color == "white":
            for piece in game.piece_list:
                if coordinates == piece.pos and piece.color == "white":
                    game.selection = piece
                    
        if self.color == "black":
            for piece in game.piece_list:
                if coordinates == piece.pos and piece.color == "black":
                    game.selection = piece


class RandomComputerPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    
    def make_move(self, game):
        pass

class SmartComputerPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    
    def make_move(self):
        pass