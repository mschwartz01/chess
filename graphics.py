from nographics import *
import pygame
import sys
import os


SIZE = 600
SQUARE_SIZE = SIZE / 8
BLACK = 0, 0, 0
WHITE = 255, 255, 255
LIGHT = 210, 180, 140
DARK = 139, 69, 19
YELLOW = 255, 215, 0
GREEN = 154, 205, 50
TAN = 245, 222, 179

pygame.init()

# images found at:
# https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent

white_pawn = pygame.image.load(os.path.join('images', 'WP.png'))
white_rook = pygame.image.load(os.path.join('images', 'WR.png'))
white_knight = pygame.image.load(os.path.join('images', 'WN.png'))
white_bishop = pygame.image.load(os.path.join('images', 'WB.png'))
white_queen = pygame.image.load(os.path.join('images', 'WQ.png'))
white_king = pygame.image.load(os.path.join('images', 'WK.png'))
black_pawn = pygame.image.load(os.path.join('images', 'BP.png'))
black_rook = pygame.image.load(os.path.join('images', 'BR.png'))
black_knight = pygame.image.load(os.path.join('images', 'BN.png'))
black_bishop = pygame.image.load(os.path.join('images', 'BB.png'))
black_queen = pygame.image.load(os.path.join('images', 'BQ.png'))
black_king = pygame.image.load(os.path.join('images', 'BK.png'))

screen = pygame.display.set_mode((SIZE, SIZE))


def display_board(board, pending=False, clicked_location=None, size=SIZE):
	"""
	Display board in the Pygame window.

	Args:
		pending: boolean representing if the user has chosen a piece to move, but hasn't chosen its new location yet.
		clicked_location: if pending, the location of the piece the user has chosen.
		size: size of the Pygame window.
	"""
	square_size = size / 8
	border = square_size/15
	c = 0
	for column in range(8):
		r = 0
		for row in range(8):
			if (column + row) % 2 == 0:
				pygame.draw.rect(screen, LIGHT, [c, r, square_size, square_size])
			else:
				pygame.draw.rect(screen, DARK, [c, r, square_size, square_size])
			if pending and clicked_location == chr(ord('a') + column) + str(8 - row):
				pygame.draw.rect(screen, YELLOW, [c + border, r + border, square_size - 2 * border, square_size - 2 * border])
			if pending and board[clicked_location].valid_move(chr(ord('a') + column) + str(8 - row)):
				pygame.draw.rect(screen, GREEN, [c + border, r + border, square_size - 2 * border, square_size - 2 * border])
			r += square_size
		c += square_size

	c = (square_size - 60) / 2
	for column in range(ord('a'), ord('h') + 1):
		r = (square_size - 60) / 2
		for row in range(8, 0, -1):
			position = chr(column) + str(row)
			if type(board[position]) == Pawn and board[position].color == 'white':
				screen.blit(white_pawn, (c, r))
			if type(board[position]) == Rook and board[position].color == 'white':
				screen.blit(white_rook, (c, r))
			if type(board[position]) == Knight and board[position].color == 'white':
				screen.blit(white_knight, (c, r))
			if type(board[position]) == Bishop and board[position].color == 'white':
				screen.blit(white_bishop, (c, r))
			if type(board[position]) == Queen and board[position].color == 'white':
				screen.blit(white_queen, (c, r))
			if type(board[position]) == King and board[position].color == 'white':
				screen.blit(white_king, (c, r))
			if type(board[position]) == Pawn and board[position].color == 'black':
				screen.blit(black_pawn, (c, r))
			if type(board[position]) == Rook and board[position].color == 'black':
				screen.blit(black_rook, (c, r))
			if type(board[position]) == Knight and board[position].color == 'black':
				screen.blit(black_knight, (c, r))
			if type(board[position]) == Bishop and board[position].color == 'black':
				screen.blit(black_bishop, (c, r))
			if type(board[position]) == Queen and board[position].color == 'black':
				screen.blit(black_queen, (c, r))
			if type(board[position]) == King and board[position].color == 'black':
				screen.blit(black_king, (c, r))
			r += square_size
		c += square_size


def display_promotion(player, size=SIZE):
	"""
	Display choices for pawn promotion, wait for user to choose, and return user's choice.

	Args:
		player: 'white' or 'black'.
		size: size of the Pygame window.

	Returns:
		The user's choice: 'Queen', 'Rook', 'Bishop', or 'Knight'.
	"""
	left_edge = (size - 375) / 2
	top_edge = (size - 75) / 2
	pygame.draw.rect(screen, TAN, [left_edge, top_edge, 375, 75])
	if player == 'white':
		screen.blit(white_queen, (left_edge + 27 + (87 * 0), top_edge + 7.5))
		screen.blit(white_rook, (left_edge + 27 + (87 * 1), top_edge + 7.5))
		screen.blit(white_bishop, (left_edge + 27 + (87 * 2), top_edge + 7.5))
		screen.blit(white_knight, (left_edge + 27 + (87 * 3), top_edge + 7.5))
	else:
		screen.blit(black_queen, (left_edge + 27 + (87 * 0), top_edge + 7.5))
		screen.blit(black_rook, (left_edge + 27 + (87 * 1), top_edge + 7.5))
		screen.blit(black_bishop, (left_edge + 27 + (87 * 2), top_edge + 7.5))
		screen.blit(black_knight, (left_edge + 27 + (87 * 3), top_edge + 7.5))
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				x, y = pygame.mouse.get_pos()
				if top_edge < y and y < top_edge + 75:
					if left_edge < x and x < left_edge + 100.5:
						return 'Queen'
					if left_edge + 100.5 < x and x < left_edge + 375 / 2:
						return 'Rook'
					if left_edge + 375 / 2 < x and x < left_edge + 375 - 100.5:
						return 'Bishop'
					if left_edge + 375 - 100.5 < x and x < left_edge + 375:
						return 'Knight'


BOARD = starting_board()
display_board(BOARD)
pygame.display.flip()

pending = False
player = 'white'
pygame.display.set_caption("White's turn")
start = None
game_over = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			if game_over:
				continue
			x, y = pygame.mouse.get_pos()
			column = chr(ord('a') + int(x // SQUARE_SIZE))
			row = 8 - (y // SQUARE_SIZE)
			position = column + str(int(row))
			if not pending and BOARD[position] != 'empty' and BOARD[position].color == player:
				start = position
				pending = True
			elif pending:
				piece = BOARD[start]
				if piece != 'empty' and BOARD[start].valid_move(position):
					piece.make_move(position)
					if type(piece) == Pawn and piece.promoted:
						display_board(BOARD)
						promote(BOARD, display_promotion(player), player, position)
					if not can_move(opponent(player), BOARD):
						for position in BOARD.keys():
							if type(BOARD[position]) == King and BOARD[position].color == opponent(player):
								if BOARD[position].check(position):
									pygame.display.set_caption('Checkmate!  ' + player.title() + ' wins!')
								else:
									pygame.display.set_caption('Stalemate!')
								break
						display_board(BOARD)
						pygame.display.flip()
						pending = False
						game_over = True
						break
					player = opponent(player)
					pygame.display.set_caption(player.title() + "'s turn")
				pending = False
			display_board(BOARD, pending, start)
			pygame.display.flip()
