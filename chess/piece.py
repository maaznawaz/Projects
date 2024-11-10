import pygame


class Piece:
    def __init__(self, color):
        self.color = color
        self.captured = False


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pos = [400, 800] if self.color == "white" else [400, 100]
        self.img = pygame.image.load("data/images/white-king.png") if self.color == "white" else pygame.image.load("data/images/black-king.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.castle = True

    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    
    def search_for_check(self, game):
        return False
    
    def available_moves_in_check(self, game):
        return game.checked_king_moves
    
    def available_move(self, game):
        available_move_list = []
        piece_on_square = []
        attacked_square = []
        queen_side_pieces = []
        king_side_pieces = []
        ks_rook_castle = False
        qs_rook_castle = False

        if self.color == "white":
            for piece in game.piece_list:
                if piece.pos == [self.pos[0] + 100, self.pos[1] - 100]: # right up
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                elif piece.color == "black":
                    if piece.__str__().endswith("King"):
                        pass
                    elif [self.pos[0] + 100, self.pos[1] - 100] in piece.available_move(game):
                        attacked_square.append([self.pos[0] + 100, self.pos[1] - 100])

                if piece.pos == [self.pos[0] + 100, self.pos[1]]: # right
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                    if self.castle == True: # only checking piece positions if castling is still available else leave it as empty list
                        king_side_pieces.append(piece) # if any piece to the immediate right of king then we can't castle
                elif piece.color == "black":
                    if piece.__str__().endswith("King"):
                        pass
                    elif [self.pos[0] + 100, self.pos[1]] in piece.available_move(game):
                        attacked_square.append([self.pos[0] + 100, self.pos[1]])
                        king_side_pieces.append(piece)

                if piece.pos == [self.pos[0] + 100, self.pos[1] + 100]: # right down
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "black":
                    if piece.__str__().endswith("King"):
                        pass
                    elif [self.pos[0] + 100, self.pos[1] + 100] in piece.available_move(game):
                        attacked_square.append([self.pos[0] + 100, self.pos[1] + 100])

                if piece.pos == [self.pos[0], self.pos[1] + 100]: # down
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "black" and piece.__str__().endswith("King") == False and [self.pos[0], self.pos[1] + 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0], self.pos[1] + 100])

                if piece.pos == [self.pos[0] - 100, self.pos[1] + 100]: # left down
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "black" and piece.__str__().endswith("King") == False and [self.pos[0] - 100, self.pos[1] + 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0] - 100, self.pos[1] + 100])

                if piece.pos == [self.pos[0] - 100, self.pos[1]]: # left
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                    if self.castle == True: # only checking piece positions if castling is still available else leave it as empty list
                        queen_side_pieces.append(piece) # if any piece to the immediate left of king then we can't castle
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "black" and piece.__str__().endswith("King") == False and [self.pos[0] - 100, self.pos[1]] in piece.available_move(game):
                    attacked_square.append([self.pos[0] - 100, self.pos[1]])
                    queen_side_pieces.append(piece)

                if piece.pos == [self.pos[0] - 100, self.pos[1] - 100]: # left up
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "black" and piece.__str__().endswith("King") == False and [self.pos[0] - 100, self.pos[1] - 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0] - 100, self.pos[1] - 100])
                
                if piece.pos == [self.pos[0], self.pos[1] - 100]: # up
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "black" and piece.__str__().endswith("King") == False and [self.pos[0], self.pos[1] - 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0], self.pos[1] - 100])
                
                if (self.castle == True and piece.pos == [600, 800]) or self.castle == True and piece.__str__().endswith("King") == False and piece.color == "black" and [600, 800] in piece.available_move(game): # checking for piece two squares to right of king
                    king_side_pieces.append(piece)
                if (self.castle == True and piece.pos == [200, 800]) or self.castle == True and piece.__str__().endswith("King") == False and piece.color == "black" and [200, 800] in piece.available_move(game): # checking for piece two squares to left of king
                    queen_side_pieces.append(piece)
                if self.castle == True and piece.pos == [100, 800]: # checking for piece three squares to left of king
                    queen_side_pieces.append(piece)
                if piece.color == "white" and piece.__str__().endswith("Rook") and piece.pos == [700, 800]:
                    if piece.castle == True:
                        ks_rook_castle = True
                if piece.color == "white" and piece.__str__().endswith("Rook") and piece.pos == [0, 800]:
                    if piece.castle == True:
                        qs_rook_castle = True
                
            # king side castle and queen side castle moves for king only... need to setup rook move on Player.make_move
            if self.castle == True and not king_side_pieces and ks_rook_castle == True:
                available_move_list.append([600, 800])
            if self.castle == True and not queen_side_pieces and qs_rook_castle == True:
                available_move_list.append([200, 800])

            if [self.pos[0] + 100, self.pos[1] - 100] not in piece_on_square and [self.pos[0] + 100, self.pos[1] - 100] not in attacked_square and [self.pos[0] + 100, self.pos[1] - 100] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] + 100, self.pos[1] - 100])
            if [self.pos[0] + 100, self.pos[1]] not in piece_on_square and [self.pos[0] + 100, self.pos[1]] not in attacked_square and [self.pos[0] + 100, self.pos[1]] not in available_move_list and self.pos[0] + 100 <= 700:
                available_move_list.append([self.pos[0] + 100, self.pos[1]])
            if [self.pos[0] + 100, self.pos[1] + 100] not in piece_on_square and [self.pos[0] + 100, self.pos[1] + 100] not in attacked_square and [self.pos[0] + 100, self.pos[1] + 100] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] + 100, self.pos[1] + 100])
            if [self.pos[0], self.pos[1] + 100] not in piece_on_square and [self.pos[0], self.pos[1] + 100] not in attacked_square and [self.pos[0], self.pos[1] + 100] not in available_move_list and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0], self.pos[1] + 100])
            if [self.pos[0] - 100, self.pos[1] + 100] not in piece_on_square and [self.pos[0] - 100, self.pos[1] + 100] not in attacked_square and [self.pos[0] - 100, self.pos[1] + 100] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] - 100, self.pos[1] + 100])
            if [self.pos[0] - 100, self.pos[1]] not in piece_on_square and [self.pos[0] - 100, self.pos[1]] not in attacked_square and [self.pos[0] - 100, self.pos[1]] not in available_move_list and self.pos[0] - 100 >= 0:
                available_move_list.append([self.pos[0] - 100, self.pos[1]])
            if [self.pos[0] - 100, self.pos[1] - 100] not in piece_on_square and [self.pos[0] - 100, self.pos[1] - 100] not in attacked_square and [self.pos[0] - 100, self.pos[1] - 100] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] - 100, self.pos[1] - 100])
            if [self.pos[0], self.pos[1] - 100] not in piece_on_square and [self.pos[0], self.pos[1] - 100] not in attacked_square and [self.pos[0], self.pos[1] - 100] not in available_move_list and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0], self.pos[1] - 100])

        if self.color == "black":
            for piece in game.piece_list:
                if piece.pos == [self.pos[0] + 100, self.pos[1] - 100]: # right up
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0] + 100, self.pos[1] - 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0] + 100, self.pos[1] - 100])

                if piece.pos == [self.pos[0] + 100, self.pos[1]]: # right
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                    if self.castle == True: # only checking piece positions if castling is still available else leave it as empty list
                        king_side_pieces.append(piece) # if any piece to the immediate right of king then we can't castle
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0] + 100, self.pos[1]] in piece.available_move(game):
                    attacked_square.append([self.pos[0] + 100, self.pos[1]])
                    king_side_pieces.append(piece)

                if piece.pos == [self.pos[0] + 100, self.pos[1] + 100]: # right down
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0] + 100, self.pos[1] + 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0] + 100, self.pos[1] + 100])

                if piece.pos == [self.pos[0], self.pos[1] + 100]: # down
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0], self.pos[1] + 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0], self.pos[1] + 100])

                if piece.pos == [self.pos[0] - 100, self.pos[1] + 100]: # left down
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0] - 100, self.pos[1] + 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0] - 100, self.pos[1] + 100])

                if piece.pos == [self.pos[0] - 100, self.pos[1]]: # left
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                    if self.castle == True: # only checking piece positions if castling is still available else leave it as empty list
                        queen_side_pieces.append(piece) # if any piece to the immediate left of king then we can't castle
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0] - 100, self.pos[1]] in piece.available_move(game):
                    attacked_square.append([self.pos[0] - 100, self.pos[1]])
                    queen_side_pieces.append(piece)

                if piece.pos == [self.pos[0] - 100, self.pos[1] - 100]: # left up
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0] - 100, self.pos[1] - 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0] - 100, self.pos[1] - 100])
                
                if piece.pos == [self.pos[0], self.pos[1] - 100]: # up
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                #checking to make sure the king isn't moving onto an attacked square
                elif piece.color == "white" and piece.__str__().endswith("King") == False and [self.pos[0], self.pos[1] - 100] in piece.available_move(game):
                    attacked_square.append([self.pos[0], self.pos[1] - 100])
                
                if (self.castle == True and piece.pos == [600, 100]) or self.castle == True and piece.__str__().endswith("King") == False and piece.color == "white" and [600, 100] in piece.available_move(game): # checking for piece two squares to right of king
                    king_side_pieces.append(piece)
                if (self.castle == True and piece.pos == [200, 100]) or self.castle == True and piece.__str__().endswith("King") == False and piece.color == "white" and [200, 100] in piece.available_move(game): # checking for piece two squares to left of king
                    queen_side_pieces.append(piece)
                if self.castle == True and piece.pos == [100, 100]: # checking for piece three squares to left of king
                    queen_side_pieces.append(piece)
                if piece.color == "black" and piece.__str__().endswith("Rook") and piece.pos == [700, 100]:
                    if piece.castle == True:
                        ks_rook_castle = True
                if piece.color == "black" and piece.__str__().endswith("Rook") and piece.pos == [0, 100]:
                    if piece.castle == True:
                        qs_rook_castle = True
                
            # king side castle and queen side castle moves for king only... need to setup rook move on Player.make_move
            if self.castle == True and not king_side_pieces and ks_rook_castle == True:
                available_move_list.append([600, 100])
            if self.castle == True and not queen_side_pieces and qs_rook_castle == True:
                available_move_list.append([200, 100])

            if [self.pos[0] + 100, self.pos[1] - 100] not in piece_on_square and [self.pos[0] + 100, self.pos[1] - 100] not in attacked_square and [self.pos[0] + 100, self.pos[1] - 100] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] + 100, self.pos[1] - 100])
            if [self.pos[0] + 100, self.pos[1]] not in piece_on_square and [self.pos[0] + 100, self.pos[1]] not in attacked_square and [self.pos[0] + 100, self.pos[1]] not in available_move_list and self.pos[0] + 100 <= 700:
                available_move_list.append([self.pos[0] + 100, self.pos[1]])
            if [self.pos[0] + 100, self.pos[1] + 100] not in piece_on_square and [self.pos[0] + 100, self.pos[1] + 100] not in attacked_square and [self.pos[0] + 100, self.pos[1] + 100] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] + 100, self.pos[1] + 100])
            if [self.pos[0], self.pos[1] + 100] not in piece_on_square and [self.pos[0], self.pos[1] + 100] not in attacked_square and [self.pos[0], self.pos[1] + 100] not in available_move_list and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0], self.pos[1] + 100])
            if [self.pos[0] - 100, self.pos[1] + 100] not in piece_on_square and [self.pos[0] - 100, self.pos[1] + 100] not in attacked_square and [self.pos[0] - 100, self.pos[1] + 100] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] - 100, self.pos[1] + 100])
            if [self.pos[0] - 100, self.pos[1]] not in piece_on_square and [self.pos[0] - 100, self.pos[1]] not in attacked_square and [self.pos[0] - 100, self.pos[1]] not in available_move_list and self.pos[0] - 100 >= 0:
                available_move_list.append([self.pos[0] - 100, self.pos[1]])
            if [self.pos[0] - 100, self.pos[1] - 100] not in piece_on_square and [self.pos[0] - 100, self.pos[1] - 100] not in attacked_square and [self.pos[0] - 100, self.pos[1] - 100] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] - 100, self.pos[1] - 100])
            if [self.pos[0], self.pos[1] - 100] not in piece_on_square and [self.pos[0], self.pos[1] - 100] not in attacked_square and [self.pos[0], self.pos[1] - 100] not in available_move_list and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0], self.pos[1] - 100])
        
        return available_move_list
    

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pos = [300, 800] if self.color == "white" else [300, 100]
        self.img = pygame.image.load("data/images/white-queen.png") if self.color == "white" else pygame.image.load("data/images/black-queen.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.captured_img = pygame.transform.scale(self.img, (40, 40))
        
    def search_for_check(self, game):
        piece_in_front = False
        piece_behind = False
        piece_to_right = False
        piece_to_left = False
        piece_front_right = False
        piece_front_left = False
        piece_behind_right = False
        piece_behind_left = False
        if self.color == "white":
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100), 8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_in_front == False and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] - j*100] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_in_front = True
                    if piece_behind == False and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] + j*100] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind = True
                    if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + j*100, self.pos[1]] for j in range(0, (piece.pos[0] - self.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_right = True
                    if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - j*100, self.pos[1]] for j in range(0, (self.pos[0] - piece.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_left = True
                    if piece_in_front and piece_behind and piece_to_right and piece_to_left:
                        return False
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_right = True    
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_left = True
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_right = True
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_left = True
                    if piece_in_front and piece_behind and piece_to_right and piece_to_left and piece_front_right and piece_front_left and piece_behind_right and piece_behind_left:
                        return False
        
        if self.color == "black":
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100), 8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_in_front == False and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] - j*100] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_in_front = True
                    if piece_behind == False and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] + j*100] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind = True
                    if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + j*100, self.pos[1]] for j in range(0, (piece.pos[0] - self.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_right = True
                    if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - j*100, self.pos[1]] for j in range(0, (self.pos[0] - piece.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_left = True
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_right = True    
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_left = True
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_right = True
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_left = True
                    if piece_in_front and piece_behind and piece_to_right and piece_to_left and piece_front_right and piece_front_left and piece_behind_right and piece_behind_left:
                        return False
        
        return False
    
    def available_moves_in_check(self, game):
        available_move_list = []
        if game.double_check == True:
            return available_move_list
        else:
            for move in self.available_move(game):
                if move in game.checked_squares_list:
                    available_move_list.append(move)
            return available_move_list
    
    def available_move(self, game):
        available_move_list = []
        piece_in_front = False
        piece_behind = False
        piece_to_right = False
        piece_to_left = False
        piece_front_right = False
        piece_front_left = False
        piece_behind_right = False
        piece_behind_left = False
        if self.color == "white":
            # using a straight loop out to 8
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100), 8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_in_front == False and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            piece_in_front = True
                    if piece_behind == False and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            piece_behind = True
                    if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            piece_to_right = True
                    if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            piece_to_left = True
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_right = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_left = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_right = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_left = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)

                if piece_in_front == False and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0], self.pos[1] - (i * 100)])
                if piece_behind == False and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0], self.pos[1] + (i * 100)])
                if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1]])
                if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1]])
                if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] - (i * 100)])
                if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] - (i * 100)])
                if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] + (i * 100)])
                if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] + (i * 100)])
                if piece_in_front == True and piece_behind == True and piece_to_right == True and piece_to_left == True and piece_front_right == True and piece_front_left == True and piece_behind_right == True and piece_behind_left == True:
                    return available_move_list

            return available_move_list


        if self.color == "black":
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100), 8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_in_front == False and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                            piece_in_front = True
                    if piece_behind == False and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                            piece_behind = True
                    if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                            piece_to_right = True
                    if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                            piece_to_left = True
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_right = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_left = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_right = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_left = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)

                if piece_in_front == False and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0], self.pos[1] - (i * 100)])
                if piece_behind == False and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0], self.pos[1] + (i * 100)])
                if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1]])
                if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1]])
                if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] - (i * 100)])
                if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] - (i * 100)])
                if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] + (i * 100)])
                if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] + (i * 100)])
                if piece_in_front == True and piece_behind == True and piece_to_right == True and piece_to_left == True and piece_front_right == True and piece_front_left == True and piece_behind_right == True and piece_behind_left == True:
                    return available_move_list

            return available_move_list

    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color)
        self.position = position
        
        if self.position == 'QS' and self.color == "white":
            self.pos = [200, 800]        
        elif self.position == 'QS' and self.color == "black":
            self.pos = [200, 100]
        elif self.position == 'KS' and self.color == "white":
            self.pos = [500, 800]
        elif self.position == 'KS' and self.color == "black":
            self.pos = [500, 100]
        else: # pawn promotion 
            self.pos = []

        self.img = pygame.image.load("data/images/white-bishop.png") if self.color == "white" else pygame.image.load("data/images/black-bishop.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.captured_img = pygame.transform.scale(self.img, (40, 40))

    def search_for_check(self, game):
        piece_front_right = False
        piece_front_left = False
        piece_behind_right = False
        piece_behind_left = False
        if self.color == "white":
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100)) if max(1 + (self.pos[0] // 100), 8 - (self.pos[0] // 100)) > max(self.pos[1] // 100, 9 - (self.pos[1] // 100)) else max(8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_right = True    
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_left = True
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_right = True
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_left = True
                    if piece_front_right and piece_front_left and piece_behind_right and piece_behind_left:
                        return False
        
        if self.color == "black":
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100)) if max(1 + (self.pos[0] // 100), 8 - (self.pos[0] // 100)) > max(self.pos[1] // 100, 9 - (self.pos[1] // 100)) else max(8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_right = True    
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] - (j*100)] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_front_left = True
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_right = True
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - (j*100), self.pos[1] + (j*100)] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind_left = True
                    if piece_front_right and piece_front_left and piece_behind_right and piece_behind_left:
                        return False
        
        return False
    
    def available_moves_in_check(self, game):
        available_move_list = []
        if game.double_check == True:
            return available_move_list
        else:
            for move in self.available_move(game):
                if move in game.checked_squares_list:
                    available_move_list.append(move)
            return available_move_list
    
    def available_move(self, game):
        available_move_list = []
        piece_front_right = False
        piece_front_left = False
        piece_behind_right = False
        piece_behind_left = False
        if self.color == "white":
            # search for diagonal moves... should be able to iterate all 4 directions in one loop
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100)) if max(1 + (self.pos[0] // 100), 8 - (self.pos[0] // 100)) > max(self.pos[1] // 100, 9 - (self.pos[1] // 100)) else max(8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_right = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_left = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_right = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_left = True
                            if piece.color == "black":
                                available_move_list.append(piece.pos)
                            

                if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] - (i * 100)])
                if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] - (i * 100)])
                if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] + (i * 100)])
                if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] + (i * 100)])
                if piece_front_right == True and piece_front_left == True and piece_behind_right == True and piece_behind_left == True:
                    return available_move_list

            return available_move_list

        if self.color == "black":
        # search for diagonal moves... should be able to iterate all 4 directions in one loop
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100)) if max(1 + (self.pos[0] // 100), 8 - (self.pos[0] // 100)) > max(self.pos[1] // 100, 9 - (self.pos[1] // 100)) else max(8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_right = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                    if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] - (i * 100)]:
                            piece_front_left = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                    if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_right = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                    if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1] + (i * 100)]:
                            piece_behind_left = True
                            if piece.color == "white":
                                available_move_list.append(piece.pos)
                if piece_front_right == False and i < 8 - (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] - (i * 100)])
                if piece_front_left == False and i < 1 + (self.pos[0] // 100) and i < self.pos[1] // 100:
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] - (i * 100)])
                if piece_behind_right == False and i < 8 - (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1] + (i * 100)])
                if piece_behind_left == False and i < 1 + (self.pos[0] // 100) and i < 9 - (self.pos[1] // 100):
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1] + (i * 100)])
                if piece_front_right == True and piece_front_left == True and piece_behind_right == True and piece_behind_left == True:
                    return available_move_list

            return available_move_list
        
    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color)
        self.position = position
        
        if self.position == 'QS' and self.color == "white":
            self.pos = [100, 800]        
        elif self.position == 'QS' and self.color == "black":
            self.pos = [100, 100]
        elif self.position == 'KS' and self.color == "white":
            self.pos = [600, 800]
        elif self.position == 'KS' and self.color == "black":
            self.pos = [600, 100]
        else: # leaving position as blank list for pawn promotion
            self.pos = []

        self.img = pygame.image.load("data/images/white-knight.png") if self.color == "white" else pygame.image.load("data/images/black-knight.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.captured_img = pygame.transform.scale(self.img, (40, 40))

    def search_for_check(self, game):
        if self.color == "white":
            for piece in game.piece_list:
                if piece.pos == [self.pos[0] + 100, self.pos[1] - 200]: # up 2, right 1
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] + 100, self.pos[1] + 200]: # down 2, right 1
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] + 200, self.pos[1] - 100]: # up 1, right 2
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] + 200, self.pos[1] + 100]: # down 1, right 2
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 100, self.pos[1] - 200]: # up 2, left 1
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 100, self.pos[1] + 200]: # down 2, left 1
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 200, self.pos[1] - 100]: # up 1, left 2
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 200, self.pos[1] + 100]: # down 1, left 2
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
            return False

        if self.color == "black":
            for piece in game.piece_list:
                if piece.pos == [self.pos[0] + 100, self.pos[1] - 200]: # up 2, right 1
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] + 100, self.pos[1] + 200]: # down 2, right 1
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] + 200, self.pos[1] - 100]: # up 1, right 2
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] + 200, self.pos[1] + 100]: # down 1, right 2
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 100, self.pos[1] - 200]: # up 2, left 1
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 100, self.pos[1] + 200]: # down 2, left 1
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 200, self.pos[1] - 100]: # up 1, left 2
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
                if piece.pos == [self.pos[0] - 200, self.pos[1] + 100]: # down 1, left 2
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        game.checked_squares_list.append(self.pos)
                        return True
            return False
    
    def available_moves_in_check(self, game):
        available_move_list = []
        if game.double_check == True:
            return available_move_list
        else:
            for move in self.available_move(game):
                if move in game.checked_squares_list:
                    available_move_list.append(move)
            return available_move_list
    
    def available_move(self, game):
        available_move_list = []
        piece_on_square = []
        if self.color == "white":
            for piece in game.piece_list:
                if piece.pos == [self.pos[0] + 100, self.pos[1] - 200]: # up 2, right 1
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] + 100, self.pos[1] + 200]: # down 2, right 1
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] + 200, self.pos[1] - 100]: # up 1, right 2
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] + 200, self.pos[1] + 100]: # down 1, right 2
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 100, self.pos[1] - 200]: # up 2, left 1
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 100, self.pos[1] + 200]: # down 2, left 1
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 200, self.pos[1] - 100]: # up 1, left 2
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 200, self.pos[1] + 100]: # down 1, left 2
                    if piece.color == "black":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
            if [self.pos[0] + 100, self.pos[1] - 200] not in piece_on_square and [self.pos[0] + 100, self.pos[1] - 200] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] - 200 >= 100:
                available_move_list.append([self.pos[0] + 100, self.pos[1] - 200])
            if [self.pos[0] + 100, self.pos[1] + 200] not in piece_on_square and [self.pos[0] + 100, self.pos[1] + 200] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] + 200 <= 800:
                available_move_list.append([self.pos[0] + 100, self.pos[1] + 200])
            if [self.pos[0] + 200, self.pos[1] - 100] not in piece_on_square and [self.pos[0] + 200, self.pos[1] - 100] not in available_move_list and self.pos[0] + 200 <= 700 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] + 200, self.pos[1] - 100])
            if [self.pos[0] + 200, self.pos[1] + 100] not in piece_on_square and [self.pos[0] + 200, self.pos[1] + 100] not in available_move_list and self.pos[0] + 200 <= 700 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] + 200, self.pos[1] + 100])
            if [self.pos[0] - 100, self.pos[1] - 200] not in piece_on_square and [self.pos[0] - 100, self.pos[1] - 200] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] - 200 >= 100:
                available_move_list.append([self.pos[0] - 100, self.pos[1] - 200])
            if [self.pos[0] - 100, self.pos[1] + 200] not in piece_on_square and [self.pos[0] - 100, self.pos[1] + 200] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] + 200 <= 800:
                available_move_list.append([self.pos[0] - 100, self.pos[1] + 200])
            if [self.pos[0] - 200, self.pos[1] - 100] not in piece_on_square and [self.pos[0] - 200, self.pos[1] - 100] not in available_move_list and self.pos[0] - 200 >= 0 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] - 200, self.pos[1] - 100])
            if [self.pos[0] - 200, self.pos[1] + 100] not in piece_on_square and [self.pos[0] - 200, self.pos[1] + 100] not in available_move_list and self.pos[0] - 200 >= 0 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] - 200, self.pos[1] + 100])

        if self.color == "black":
            for piece in game.piece_list:
                if piece.pos == [self.pos[0] + 100, self.pos[1] - 200]: # up 2, right 1
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] + 100, self.pos[1] + 200]: # down 2, right 1
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] + 200, self.pos[1] - 100]: # up 1, right 2
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] + 200, self.pos[1] + 100]: # down 1, right 2
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 100, self.pos[1] - 200]: # up 2, left 1
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 100, self.pos[1] + 200]: # down 2, left 1
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 200, self.pos[1] - 100]: # up 1, left 2
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
                if piece.pos == [self.pos[0] - 200, self.pos[1] + 100]: # down 1, left 2
                    if piece.color == "white":
                        available_move_list.append(piece.pos)
                    else:
                        piece_on_square.append(piece.pos)
            if [self.pos[0] + 100, self.pos[1] - 200] not in piece_on_square and [self.pos[0] + 100, self.pos[1] - 200] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] - 200 >= 100:
                available_move_list.append([self.pos[0] + 100, self.pos[1] - 200])
            if [self.pos[0] + 100, self.pos[1] + 200] not in piece_on_square and [self.pos[0] + 100, self.pos[1] + 200] not in available_move_list and self.pos[0] + 100 <= 700 and self.pos[1] + 200 <= 800:
                available_move_list.append([self.pos[0] + 100, self.pos[1] + 200])
            if [self.pos[0] + 200, self.pos[1] - 100] not in piece_on_square and [self.pos[0] + 200, self.pos[1] - 100] not in available_move_list and self.pos[0] + 200 <= 700 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] + 200, self.pos[1] - 100])
            if [self.pos[0] + 200, self.pos[1] + 100] not in piece_on_square and [self.pos[0] + 200, self.pos[1] + 100] not in available_move_list and self.pos[0] + 200 <= 700 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] + 200, self.pos[1] + 100])
            if [self.pos[0] - 100, self.pos[1] - 200] not in piece_on_square and [self.pos[0] - 100, self.pos[1] - 200] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] - 200 >= 100:
                available_move_list.append([self.pos[0] - 100, self.pos[1] - 200])
            if [self.pos[0] - 100, self.pos[1] + 200] not in piece_on_square and [self.pos[0] - 100, self.pos[1] + 200] not in available_move_list and self.pos[0] - 100 >= 0 and self.pos[1] + 200 <= 800:
                available_move_list.append([self.pos[0] - 100, self.pos[1] + 200])
            if [self.pos[0] - 200, self.pos[1] - 100] not in piece_on_square and [self.pos[0] - 200, self.pos[1] - 100] not in available_move_list and self.pos[0] - 200 >= 0 and self.pos[1] - 100 >= 100:
                available_move_list.append([self.pos[0] - 200, self.pos[1] - 100])
            if [self.pos[0] - 200, self.pos[1] + 100] not in piece_on_square and [self.pos[0] - 200, self.pos[1] + 100] not in available_move_list and self.pos[0] - 200 >= 0 and self.pos[1] + 100 <= 800:
                available_move_list.append([self.pos[0] - 200, self.pos[1] + 100])
        
        return available_move_list
    
    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color)
        self.position = position
        self.castle = True
        
        if self.position == 'QS' and self.color == "white":
            self.pos = [0, 800]        
        elif self.position == 'QS' and self.color == "black":
            self.pos = [0, 100]
        elif self.position == 'KS' and self.color == "white":
            self.pos = [700, 800]
        elif self.position == 'KS' and self.color == "black":
            self.pos = [700, 100]
        else: 
            self.pos = [] # leaving the position empty for pawn promotion - will appoint position in game code
        

        self.img = pygame.image.load("data/images/white-rook.png") if self.color == "white" else pygame.image.load("data/images/black-rook.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.captured_img = pygame.transform.scale(self.img, (40, 40))

    def search_for_check(self, game):
        piece_in_front = False
        piece_behind = False
        piece_to_right = False
        piece_to_left = False
        if self.color == "white":
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100), 8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    # scanning for king in front of Rook
                    if piece_in_front == False and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] - j*100] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_in_front = True
                    if piece_behind == False and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] + j*100] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind = True
                    if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + j*100, self.pos[1]] for j in range(0, (piece.pos[0] - self.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_right = True
                    if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                            if piece.color == "black" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - j*100, self.pos[1]] for j in range(0, (self.pos[0] - piece.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_left = True
                    if piece_in_front and piece_behind and piece_to_right and piece_to_left:
                        return False
        
        if self.color == "black":
            for i in range(1, max(9 - (self.pos[1] // 100), (self.pos[1] // 100), 8 - (self.pos[0] // 100), 1 + (self.pos[0] // 100))):
                for piece in game.piece_list:
                    # scanning for king in front of Rook
                    if piece_in_front == False and i < self.pos[1] // 100:
                        if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] - j*100] for j in range(0, (self.pos[1] - piece.pos[1]) // 100)))
                                return True
                            else:
                                piece_in_front = True
                    if piece_behind == False and i < 9 - (self.pos[1] // 100):
                        if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0], self.pos[1] + j*100] for j in range(0, (piece.pos[1] - self.pos[1]) // 100)))
                                return True
                            else:
                                piece_behind = True
                    if piece_to_right == False and i < 8 - (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] + j*100, self.pos[1]] for j in range(0, (piece.pos[0] - self.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_right = True
                    if piece_to_left == False and i < 1 + (self.pos[0] // 100):
                        if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                            if piece.color == "white" and piece.__str__().endswith("King"):
                                game.checked_squares_list.extend(([self.pos[0] - j*100, self.pos[1]] for j in range(0, (self.pos[0] - piece.pos[0]) // 100)))
                                return True
                            else:
                                piece_to_left = True
                    if piece_in_front and piece_behind and piece_to_right and piece_to_left:
                        return False
        
        return False

    def available_moves_in_check(self, game):
        available_move_list = []
        if game.double_check == True:
            return available_move_list
        else:
            for move in self.available_move(game):
                if move in game.checked_squares_list:
                    available_move_list.append(move)
            return available_move_list   
    
    def available_move(self, game):
        available_move_list = []
        piece_in_front = False
        piece_behind = False
        piece_to_right = False
        piece_to_left = False
        if self.color == "white":
            # search for pieces in front of rook
            # I tested the time to see how long the 4 for loops take and it is instantaneous.  
            # I tested this because I was wondering whether it would be better to do one for loop and set bounds using if statements instead
            # such as for i in range(1 to 8)... if pos is < 0 --> no good...etc
            # The code timer is such: 
            # start: 1723985386.3928943
            # end:   1723985386.3928943
            # 0.0
            for i in range(1, self.pos[1] // 100):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                        if piece.color == "black":
                            available_move_list.append(piece.pos)
                        piece_in_front = True
                        break
                if piece_in_front == False:
                    available_move_list.append([self.pos[0], self.pos[1] - (i * 100)])
                else:
                    break
            # search for pieces behind of rook
            for i in range(1, 9 - (self.pos[1] // 100)):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                        if piece.color == "black":
                            available_move_list.append(piece.pos)
                        piece_behind = True
                        break
                if piece_behind == False:
                    available_move_list.append([self.pos[0], self.pos[1] + (i * 100)])
                else:
                    break
            # search for pieces to right of rook
            for i in range(1, 8 - self.pos[0] // 100):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                        if piece.color == "black":
                            available_move_list.append(piece.pos)
                        piece_to_right = True
                        break
                if piece_to_right == False:
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1]])
                else:
                    break
            # search for pieces to left of rook
            for i in range(1, (self.pos[0] // 100) + 1):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                        if piece.color == "black":
                            available_move_list.append(piece.pos)
                        piece_to_left = True
                        break
                if piece_to_left == False: 
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1]])
                else:
                    break
            return available_move_list

        if self.color == "black":
            # search for pieces in front of rook
            for i in range(1, self.pos[1] // 100):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0], self.pos[1] - (i * 100)]:
                        if piece.color == "white":
                            available_move_list.append(piece.pos)
                        piece_in_front = True
                        break
                if piece_in_front == False:
                    available_move_list.append([self.pos[0], self.pos[1] - (i * 100)])
                else:
                    break
            # search for pieces behind of rook
            for i in range(1, 9 - (self.pos[1] // 100)):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0], self.pos[1] + (i * 100)]:
                        if piece.color == "white":
                            available_move_list.append(piece.pos)
                        piece_behind = True
                        break
                if piece_behind == False:
                    available_move_list.append([self.pos[0], self.pos[1] + (i * 100)])
                else:
                    break
            # search for pieces to right of rook
            for i in range(1, 8 - self.pos[0] // 100):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0] + (i * 100), self.pos[1]]:
                        if piece.color == "white":
                            available_move_list.append(piece.pos)
                        piece_to_right = True
                        break
                if piece_to_right == False:
                    available_move_list.append([self.pos[0] + (i * 100), self.pos[1]])
                else:
                    break
            # search for pieces to left of rook
            for i in range(1, (self.pos[0] // 100) + 1):
                for piece in game.piece_list:
                    if piece.pos == [self.pos[0] - (i * 100), self.pos[1]]:
                        if piece.color == "white":
                            available_move_list.append(piece.pos)
                        piece_to_left = True
                        break
                if piece_to_left == False:
                    available_move_list.append([self.pos[0] - (i * 100), self.pos[1]])
                else:
                    break
            return available_move_list

    def __str__(self):
        return f"{self.color} {__class__.__name__}"
    

class Pawn(Piece):
    def __init__(self, color, rank):
        super().__init__(color)
        self.rank = rank
        self.en_passant_available = False
        
        if self.rank == 'A' and self.color == "white":
            self.pos = [0, 700]        
        elif self.rank == 'B' and self.color == "white":
            self.pos = [100, 700]
        elif self.rank == 'C' and self.color == "white":
            self.pos = [200, 700]
        elif self.rank == 'D' and self.color == "white":
            self.pos = [300, 700]
        elif self.rank == 'E' and self.color == "white":
            self.pos = [400, 700]
        elif self.rank == 'F' and self.color == "white":
            self.pos = [500, 700]
        elif self.rank == 'G' and self.color == "white":
            self.pos = [600, 700]
        elif self.rank == 'H' and self.color == "white":
            self.pos = [700, 700]


        elif self.rank == 'A' and self.color == "black":
            self.pos = [0, 200]        
        elif self.rank == 'B' and self.color == "black":
            self.pos = [100, 200]
        elif self.rank == 'C' and self.color == "black":
            self.pos = [200, 200]
        elif self.rank == 'D' and self.color == "black":
            self.pos = [300, 200]
        elif self.rank == 'E' and self.color == "black":
            self.pos = [400, 200]
        elif self.rank == 'F' and self.color == "black":
            self.pos = [500, 200]
        elif self.rank == 'G' and self.color == "black":
            self.pos = [600, 200]
        else: # self.rank == 'F' and self.color == "black":
            self.pos = [700, 200]

        self.img = pygame.image.load("data/images/white-pawn.png") if self.color == "white" else pygame.image.load("data/images/black-pawn.png")
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.captured_img = pygame.transform.scale(self.img, (40, 40))
    
    def search_for_check(self, game):
        if self.color == "white":
            # looping over enemy piece to detect their presence
            for piece in game.piece_list:
                # checking if there is a king in front and to the left of pawn (aka capturable)
                if piece.color == "black" and piece.__str__().endswith("King") and piece.pos == [self.pos[0] - 100, self.pos[1] - 100]:
                    game.checked_squares_list.append(self.pos)
                    return True
                # checking if there is a king in front and to the right of pawn (aka capturable)
                if piece.color == "black" and piece.__str__().endswith("King") and piece.pos == [self.pos[0] + 100, self.pos[1] - 100]:
                    game.checked_squares_list.append(self.pos)
                    return True
            return False
                
        else: # self.color == "black":
            for piece in game.piece_list:
                # checking if there is a piece in front and to the left of pawn (aka capturable)
                if piece.color == "white" and piece.__str__().endswith("King") and piece.pos == [self.pos[0] + 100, self.pos[1] + 100]:
                    game.checked_squares_list.extend(self.pos)
                    return True
                # checking if there is a piece in front and to the right of pawn
                if piece.color == "white" and piece.__str__().endswith("King") and piece.pos == [self.pos[0] - 100, self.pos[1] + 100]:
                    game.checked_squares_list.extend(self.pos)
                    return True
            return False
                
    def available_moves_in_check(self, game):
        available_move_list = []
        if game.double_check == True:
            return available_move_list
        else:
            for move in self.available_move(game):
                if move in game.checked_squares_list:
                    available_move_list.append(move)
            return available_move_list
    
    def available_move(self, game):
        available_move_list = []
        piece_in_front = []
        if self.color == "white":
            # looping over enemy piece to detect their presence
            for piece in game.piece_list:
                # checking if there is a piece in front and to the left of pawn (aka capturable)
                if piece.color == "black" and piece.pos == [self.pos[0] - 100, self.pos[1] - 100]:
                    available_move_list.append(piece.pos)
                # checking if there is a piece in front and to the right of pawn (aka capturable)
                if piece.color == "black" and piece.pos == [self.pos[0] + 100, self.pos[1] - 100]:
                    available_move_list.append(piece.pos)
                # checking if enemy piece is directly infront of pawn... aka cannot move
                # adding that location to list piece_in_front so that we can check against 
                # that list when attempting to make a move forward move
                if piece.pos == [self.pos[0], self.pos[1] - 100]:
                    piece_in_front.append(piece.pos)
                # if there is a piece two squares in front of a starting pawn - you can't make the double opener
                if piece.pos == [self.pos[0], 500]:
                    piece_in_front.append(piece.pos)
                # checking for en_passant_available:
                if self.pos[1] == 400 and piece.__str__().endswith("Pawn") and piece.pos == [self.pos[0] - 100, 400] and piece.en_passant_available == True:
                    available_move_list.append([self.pos[0] - 100, self.pos[1] - 100])
                if self.pos[1] == 400 and piece.__str__().endswith("Pawn") and piece.pos == [self.pos[0] + 100, 400] and piece.en_passant_available == True:
                    available_move_list.append([self.pos[0] + 100, self.pos[1] - 100])

            if self.pos[1] == 700:
                if [self.pos[0], self.pos[1] - 100] in piece_in_front:
                    return available_move_list
                elif [self.pos[0], self.pos[1] - 200] in piece_in_front:
                    available_move_list.append([self.pos[0], self.pos[1] - 100])
                    return available_move_list
                else: # if no piece infront of you and no piece two squares away while you're on opening square
                    available_move_list.append([self.pos[0], self.pos[1] - 100])
                    available_move_list.append([self.pos[0], self.pos[1] - 200])
                    return available_move_list
                #return [[self.pos[0], self.pos[1] - 100], [self.pos[0], self.pos[1] - 200]]
            else:
                if [self.pos[0], self.pos[1] - 100] in piece_in_front:
                    return available_move_list
                else: # if no piece infront of you
                    available_move_list.append([self.pos[0], self.pos[1] - 100])
                    return available_move_list
        if self.color == "black":
            for piece in game.piece_list:
                # checking if there is a piece in front and to the left of pawn (aka capturable)
                if piece.color == "white" and piece.pos == [self.pos[0] + 100, self.pos[1] + 100]:
                    available_move_list.append(piece.pos)
                # checking if there is a piece in front and to the right of pawn
                if piece.color == "white" and piece.pos == [self.pos[0] - 100, self.pos[1] + 100]:
                    available_move_list.append(piece.pos)
                # now checking if an enemy piece is directly in front... if so cannot more forward
                if piece.pos == [self.pos[0], self.pos[1] + 100]:
                    piece_in_front.append(piece.pos)
                # now checking if there is an enemy piece 2 squares away from a opening pawn
                if piece.pos == [self.pos[0], 400]:
                    piece_in_front.append(piece.pos)
                # checking for en_passant_available:
                if self.pos[1] == 500 and piece.__str__().endswith("Pawn") and piece.pos == [self.pos[0] - 100, 500] and piece.en_passant_available == True:
                    available_move_list.append([self.pos[0] - 100, self.pos[1] + 100])
                if self.pos[1] == 500 and piece.__str__().endswith("Pawn") and piece.pos == [self.pos[0] + 100, 500] and piece.en_passant_available == True:
                    available_move_list.append([self.pos[0] + 100, self.pos[1] + 100])

            if self.pos[1] == 200:
                # returning move list - firstly checking if piece in front of pawn, if so can not add any forward moves to list
                if [self.pos[0], self.pos[1] + 100] in piece_in_front:
                    return available_move_list
                # checks if there is a piece two squares away from opener.. therfore can only add 1 single square jump to move list
                elif [self.pos[0], self.pos[1] + 200] in piece_in_front:
                    available_move_list.append([self.pos[0], self.pos[1] + 100])
                    return available_move_list
                else: # if no piece infront and no piece two squares away from opener can add one square jump or two
                    available_move_list.append([self.pos[0], self.pos[1] + 100])
                    available_move_list.append([self.pos[0], self.pos[1] + 200])
                    return available_move_list
            else: # if not on opening square, can only move one square no matter what
                if [self.pos[0], self.pos[1] + 100] in piece_in_front:
                    return available_move_list
                else: # if no piece infront of you
                    available_move_list.append([self.pos[0], self.pos[1] + 100])
                    return available_move_list

    
    def pawn_promotion(self, piece_list):
        if self.color == "white" and self.pos[1] == 100:
            new_piece_pos = self.pos

            piece_list.remove(self)
            new_queen = Queen("white")
            new_queen.pos = new_piece_pos
            piece_list.append(new_queen)

        if self.color == "black" and self.pos[1] == 800:
            new_piece_pos = self.pos

            piece_list.remove(self)
            new_queen = Queen("black")
            new_queen.pos = new_piece_pos
            piece_list.append(new_queen)


    def __str__(self):
        return f"{self.color} {self.rank} {__class__.__name__}"
    
    
