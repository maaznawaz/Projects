import player
import pygame, piece
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Chess")
        self.width = 1200
        self.height = 1000
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.light_brown = (193, 190, 148)
        self.dark_brown = (127, 124, 95)
        self.rank_file_font = pygame.font.Font("freesansbold.ttf", 10)
        self.game_text_font = pygame.font.Font("freesansbold.ttf", 30)
        self.piece_list = []
        self.checked_squares_list = []
        self.checked_king_moves = []
        self.checked_moves_list = []
        self.captured_list = []
        self.selection = None # setting this up as None for now... will create a function to update)
        self.moving = [False, False]
        self.turn = "white"
        self.turn_step = 0
        self.counter = 0
        self.double_check = False
        self.winner = None
        self.game_over = False


    def initialize_pieces(self):
        self.black_rook_ks = piece.Rook("black", "KS")
        self.piece_list.append(self.black_rook_ks)

        self.black_knight_ks = piece.Knight("black", "KS")
        self.piece_list.append(self.black_knight_ks)

        self.black_bishop_ks = piece.Bishop("black", "KS")
        self.piece_list.append(self.black_bishop_ks)
        
        self.black_king = piece.King("black")
        self.piece_list.append(self.black_king)

        self.black_queen = piece.Queen("black")
        self.piece_list.append(self.black_queen)

        self.black_bishop_qs = piece.Bishop("black", "QS")
        self.piece_list.append(self.black_bishop_qs)

        self.black_knight_qs = piece.Knight("black", "QS")
        self.piece_list.append(self.black_knight_qs)

        self.black_rook_qs = piece.Rook("black", "QS")
        self.piece_list.append(self.black_rook_qs)

        self.black_pawn_A = piece.Pawn("black", "A")
        self.piece_list.append(self.black_pawn_A)

        self.black_pawn_B = piece.Pawn("black", "B")
        self.piece_list.append(self.black_pawn_B)

        self.black_pawn_C = piece.Pawn("black", "C")
        self.piece_list.append(self.black_pawn_C)

        self.black_pawn_D = piece.Pawn("black", "D")
        self.piece_list.append(self.black_pawn_D)

        self.black_pawn_E = piece.Pawn("black", "E")
        self.piece_list.append(self.black_pawn_E)

        self.black_pawn_F = piece.Pawn("black", "F")
        self.piece_list.append(self.black_pawn_F)

        self.black_pawn_G = piece.Pawn("black", "G")
        self.piece_list.append(self.black_pawn_G)

        self.black_pawn_H = piece.Pawn("black", "H")
        self.piece_list.append(self.black_pawn_H)
        

        

        self.white_rook_ks = piece.Rook("white", "KS")
        self.piece_list.append(self.white_rook_ks)

        self.white_knight_ks = piece.Knight("white", "KS")
        self.piece_list.append(self.white_knight_ks)

        self.white_bishop_ks = piece.Bishop("white", "KS")
        self.piece_list.append(self.white_bishop_ks)

        self.white_king = piece.King("white")
        self.piece_list.append(self.white_king)

        self.white_queen = piece.Queen("white")
        self.piece_list.append(self.white_queen)

        self.white_bishop_qs = piece.Bishop("white", "QS")
        self.piece_list.append(self.white_bishop_qs)

        self.white_knight_qs = piece.Knight("white", "QS")
        self.piece_list.append(self.white_knight_qs)

        self.white_rook_qs = piece.Rook("white", "QS")
        self.piece_list.append(self.white_rook_qs)

        self.white_pawn_A = piece.Pawn("white", "A")
        self.piece_list.append(self.white_pawn_A)

        self.white_pawn_B = piece.Pawn("white", "B")
        self.piece_list.append(self.white_pawn_B)

        self.white_pawn_C = piece.Pawn("white", "C")
        self.piece_list.append(self.white_pawn_C)

        self.white_pawn_D = piece.Pawn("white", "D")
        self.piece_list.append(self.white_pawn_D)

        self.white_pawn_E = piece.Pawn("white", "E")
        self.piece_list.append(self.white_pawn_E)

        self.white_pawn_F = piece.Pawn("white", "F")
        self.piece_list.append(self.white_pawn_F)

        self.white_pawn_G = piece.Pawn("white", "G")
        self.piece_list.append(self.white_pawn_G)

        self.white_pawn_H = piece.Pawn("white", "H")
        self.piece_list.append(self.white_pawn_H)
        
    def draw_board(self):
        chess_file = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        chess_rank = ['8', '7', '6', '5', '4', '3', '2', '1']
        for horz in range(0, 8):
            for vert in range(0, 8):
                if horz % 2 == vert % 2:
                    pygame.draw.rect(self.screen, self.light_brown, [horz*100, vert*100 + 100, 100, 100])
                else:
                    pygame.draw.rect(self.screen, self.dark_brown, [horz*100, vert*100 + 100, 100, 100])
                
                if horz == 0:
                    self.screen.blit(self.rank_file_font.render(chess_rank[vert], False, (40, 40, 40)),(5, vert*100 + 105))
                if vert == 7:
                    self.screen.blit(self.rank_file_font.render(chess_file[horz], False, (48, 48, 48)),(horz*100 + 85, vert*100 + 185))
        # border around the game board
        pygame.draw.rect(self.screen, 'grey', (0, 100, 800, 800), 3)
        
    def draw_pieces(self):
        white_captured_loc = [860, 200]
        black_captured_loc = [860, 800]
        for p in self.piece_list:
            if p.__str__().endswith("Pawn"):
                p.pawn_promotion(self.piece_list)
            self.screen.blit(p.img, p.pos)
        for p in self.captured_list:
            if p.color == "white":
                self.screen.blit(p.captured_img, white_captured_loc)
                white_captured_loc[0] += 40
                if white_captured_loc[0] > 1140:
                    white_captured_loc[0] -= 320
                    white_captured_loc[1] += 50
            else: # if p.color == "black"
                self.screen.blit(p.captured_img, black_captured_loc)
                black_captured_loc[0] += 40
                if black_captured_loc[0] > 1140:
                    black_captured_loc[0] -= 320
                    black_captured_loc[1] += 50

    def scan_for_checkmate(self):
        if self.turn == "white":
            if self.double_check == True:
                for piece in self.piece_list:
                    if piece.color == "white" and piece.__str__().endswith("King"):
                        for move in piece.available_move(game):
                            if move in self.checked_squares_list:
                                pass
                            else:
                                self.checked_king_moves.append(move)
                        if not self.checked_king_moves:
                            return True
                        else:
                            return False
            else: # not double check
                for piece in self.piece_list:
                    if piece.color == "white":
                        if piece.__str__().endswith("King"):
                            for move in piece.available_move(game):
                                if move in self.checked_squares_list:
                                    pass
                                else:
                                    self.checked_king_moves.append(move)
                        else: #any white piece that isn't a king
                            for move in piece.available_move(game):
                                if move in self.checked_squares_list:
                                    self.checked_moves_list.append(move)
            if self.checked_moves_list == [] and self.checked_king_moves == []:
                return True
            else: 
                return False
        if self.turn == "black":
            if self.double_check:
                for piece in self.piece_list:
                    if piece.color == "black" and piece.__str__().endswith("King"):
                        for move in piece.available_move(game):
                            if move in self.checked_squares_list:
                                pass
                            else:
                                self.checked_king_moves.append(move)
                        if not self.checked_king_moves:
                            return True
                        else:
                            return False
            else: # not double check
                for piece in self.piece_list:
                    if piece.color == "black":
                        if piece.__str__().endswith("King"):
                            for move in piece.available_move(game):
                                if move in self.checked_squares_list:
                                    pass
                                else:
                                    self.checked_king_moves.append(move)
                        else: #any white piece that isn't a king
                            for move in piece.available_move(game):
                                if move in self.checked_squares_list:
                                    self.checked_moves_list.append(move)
            if self.checked_moves_list == [] and self.checked_king_moves == []:
                return True
            else: 
                return False
    
    def scan_for_checks(self):
        num_of_checks = 0 # to keep track of whether we have a single check, double check or no checks
        if self.turn == "white":
            for piece in self.piece_list:
                if piece.color == "white":
                    num_of_checks+= piece.search_for_check(game)
            if num_of_checks == 0:
                black_player.in_check = False
                self.double_check = False
            elif num_of_checks == 1:
                black_player.in_check = True
                self.double_check = False
            elif num_of_checks == 2:
                black_player.in_check = True
                self.double_check = True

        else: # self.turn == "black"
            for piece in self.piece_list:
                if piece.color == "black":
                    num_of_checks+= piece.search_for_check(game)
            if num_of_checks == 0:
                white_player.in_check = False
                self.double_check = False
            elif num_of_checks == 1:
                white_player.in_check = True
                self.double_check = False
            elif num_of_checks == 2:
                white_player.in_check = True
                self.double_check = True

    def no_pins(self, coordinates):
        temp = game.selection.pos
        game.selection.pos = coordinates
        if self.turn == "white":
            for piece in self.piece_list:
                if piece.color == "black":
                    if piece.pos == coordinates:
                        pass
                    elif piece.search_for_check(game):
                        self.checked_squares_list.clear()
                        game.selection.pos = temp
                        return False
            game.selection.pos = temp
            return True
        else: # self.turn == "black"
            for piece in self.piece_list:
                if piece.color == "white":
                    if piece.pos == coordinates:
                        pass
                    elif piece.search_for_check(game):
                        self.checked_squares_list.clear()
                        game.selection.pos = temp
                        return False
            game.selection.pos = temp
            return True


    # game loop
    def run(self):
        while self.running:
            self.screen.fill((30, 30, 30))
            self.draw_board()
            self.draw_pieces()
            
            
            # poll for events
            # pygame.QUIT event means the user clicked X to close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.turn == "white" and white_player.__str__() == f"{self.turn} HumanPlayer":
                    x_coordinate = (event.pos[0] // 100) * 100
                    y_coordinate = (event.pos[1] // 100) * 100
                    click_coordinates = [x_coordinate, y_coordinate]
                    if self.turn_step < 2:
                        white_player.player_selection(click_coordinates, game)
                        if self.turn_step == 0:
                            self.turn_step = 1
                    if self.selection != None and self.turn_step == 1:
                        if white_player.in_check:
                            if self.scan_for_checkmate():
                                self.winner = "black"
                                self.game_over = True
                                print(self.winner)
                            if click_coordinates in self.selection.available_moves_in_check(game) and self.no_pins(click_coordinates):
                                white_player.make_move(game, click_coordinates)
                                # since we were able to make a move we can remove our check status
                                white_player.in_check = False
                                self.double_check = False # just making sure we remove double check statuses
                                # empty checked_moves_list and checked_king_moves list
                                self.checked_king_moves.clear()
                                self.checked_moves_list.clear()
                                self.checked_squares_list.clear()
                                # below we will scan to see if whites recent move caused a check
                                self.scan_for_checks()
                                self.turn = "black"
                                self.selection = None
                                self.turn_step = 0
                        else: # if white player not in check
                            if click_coordinates in self.selection.available_move(game) and self.no_pins(click_coordinates):
                                white_player.make_move(game, click_coordinates)
                                # here we will scan to see if whites recent move caused a check
                                self.scan_for_checks()
                                self.turn = "black"
                                self.selection = None
                                self.turn_step = 0
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.turn == "black" and black_player.__str__() == f"{self.turn} HumanPlayer":
                    x_coordinate = (pygame.mouse.get_pos()[0] // 100) * 100
                    y_coordinate = (pygame.mouse.get_pos()[1] // 100) * 100
                    click_coordinates = [x_coordinate, y_coordinate]
                    if self.turn_step < 2:
                        black_player.player_selection(click_coordinates, game)
                        if self.turn_step == 0:
                            self.turn_step = 1
                    if self.selection != None and self.turn_step == 1:
                        if black_player.in_check:
                            if self.scan_for_checkmate():
                                self.winner = "white"
                                self.game_over = True
                                print(self.winner)
                            if click_coordinates in self.selection.available_moves_in_check(game) and self.no_pins(click_coordinates):
                                black_player.make_move(game, click_coordinates)
                                black_player.in_check = False
                                self.double_check = False
                                # empty checked_moves_list and checked_king_moves list
                                self.checked_king_moves.clear()
                                self.checked_moves_list.clear()
                                self.checked_squares_list.clear()
                                self.scan_for_checks()
                                self.turn = "white"
                                self.selection = None
                                self.turn_step = 0
                                self.counter += 1
                        else: # if black player not in check:
                            if click_coordinates in self.selection.available_move(game) and self.no_pins(click_coordinates):
                                black_player.make_move(game, click_coordinates)
                                # here we will radar to see if blacks recent move caused a check
                                self.scan_for_checks()
                                self.turn = "white"
                                self.selection = None
                                self.turn_step = 0
                                self.counter += 1
            
            if white_player.__str__() == f"{self.turn} RandomComputerPlayer" or white_player.__str__() == f"{self.turn} SmartComputerPlayer":
                white_player.make_move()
            if black_player.__str__() == f"{self.turn} RandomComputerPlayer" or black_player.__str__() == f"{self.turn} SmartComputerPlayer":
                black_player.make_move()
            
            # RENDER YOUR GAME HERE
            # writes the piece that was selected at the bottom of the screen
            self.screen.blit(self.game_text_font.render(f"{self.selection}", False, (40, 40, 40)),(5, 900))
            
            # below draws a highlight around the selected piece
            if self.turn_step < 2 and self.selection != None and self.turn == "white":
                pygame.draw.rect(self.screen, "blue", [self.selection.pos, [100, 100]], 5)
            if self.turn_step < 2 and self.selection != None and self.turn == "black":
                pygame.draw.rect(self.screen, "red", [self.selection.pos, [100, 100]], 5)
            
            # printing each persons turn
            self.screen.blit(self.game_text_font.render(f"{self.turn}'s Turn", False, (100, 100, 100)), (900, 500))

            # printing the captured pieces
            self.screen.blit(self.game_text_font.render("Captured Pieces", False, (100, 100, 100)), (900, 170))
            self.screen.blit(self.game_text_font.render("Captured Pieces", False, (100, 100, 100)), (900, 770))
            #if white_player.in_check == True:
                #self.screen.blit(self.game_text_font.render("White is in check", False, (100, 100, 100)), (800, 450))
            #if black_player.in_check == True:
                #self.screen.blit(self.game_text_font.render("Black is in check", False, (100, 100, 100)), (800, 450))

            # flip() the display to put your work on screen
            # look into what flip() does
            # updates the screen similar to pygame.display.update()... 
            # diff being that flip updates entire screen, update can flip segment of screen
            # depending on which arguments we give it... for now we'll use flip
            pygame.display.flip()
            self.clock.tick(30) # limits FPS to 30

        
        
        pygame.quit()
        if self.game_over:
            print(self.winner)

game = Game()
white_player = player.HumanPlayer("white")
black_player = player.HumanPlayer("black")
game.initialize_pieces()
game.run()

            