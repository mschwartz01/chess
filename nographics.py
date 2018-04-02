from pieces import *


def opponent(player):
	"""Return the opponent of the player ('white' or 'black')."""
	return 'black' if player == 'white' else 'white'


def can_move(player, board):
	"""
	Return if player has a valid move it can make.

	Args:
		player: 'white' or 'black'.
		board: chessboard.

	Returns:
		A boolean representing if there is a valid move player can make in the input board.
	"""
	pieces = [piece for piece in board.values() if piece != 'empty' and piece.color == player]
	for piece in pieces:
		for move in piece.get_moves():
			if piece.valid_move(move):
				return True
	return False


def starting_board():
	"""Return chessboard with all pieces in their starting positions."""
	board = {}
	for column in range(ord('a'), ord('h') + 1):
		for row in range(1, 9):
			board[chr(column) + str(row)] = 'empty'
	board['a1'] = Rook('white', 'a1', board)
	board['b1'] = Knight('white', 'b1', board)
	board['c1'] = Bishop('white', 'c1', board)
	board['d1'] = Queen('white', 'd1', board)
	board['e1'] = King('white', 'e1', board)
	board['f1'] = Bishop('white', 'f1', board)
	board['g1'] = Knight('white', 'g1', board)
	board['h1'] = Rook('white', 'h1', board)
	for column in range(ord('a'), ord('h') + 1):
		board[chr(column) + '2'] = Pawn('white', chr(column) + '2', board)
	for column in range(ord('a'), ord('h') + 1):
		board[chr(column) + '7'] = Pawn('black', chr(column) + '7', board)
	board['a8'] = Rook('black', 'a8', board)
	board['b8'] = Knight('black', 'b8', board)
	board['c8'] = Bishop('black', 'c8', board)
	board['d8'] = Queen('black', 'd8', board)
	board['e8'] = King('black', 'e8', board)
	board['f8'] = Bishop('black', 'f8', board)
	board['g8'] = Knight('black', 'g8', board)
	board['h8'] = Rook('black', 'h8', board)
	return board


def promote(board, piece, player, position):
	"""
	(Mutating) Mutate board to promote pawn to new piece.

	Args:
		board: chessboard.
		piece: one of the following: 'Queen', 'Rook', 'Bishop', or 'Knight'.
		player: 'white' or 'black'.
		position: the location of the pawn to be promoted.
	"""
	if piece == 'Queen':
		board[position] = Queen(player, position, board)
	if piece == 'Rook':
		board[position] = Rook(player, position, board, True)
	if piece == 'Bishop':
		board[position] = Bishop(player, position, board)
	if piece == 'Knight':
		board[position] = Knight(player, position, board)
