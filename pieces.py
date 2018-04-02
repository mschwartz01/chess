from copy import deepcopy


class Piece:
	"""Base class, representing a chess piece."""

	def __init__(self, color, location, board):
		"""
		color: 'white' or 'black'.
		location: location of piece in the board.
		board: the chessboard that contains the piece.
		"""
		self.color = color
		self.location = location
		self.board = board

	def get_column(self):
		"""Return the column the piece is located in."""
		return self.location[0]

	def get_row(self):
		"""Return the row the piece is located in."""
		return self.location[1]

	def _left_moves(self):
		"""Return possible moves to the left (decreasing column values) of the piece's location."""
		column = chr(ord(self.get_column()) - 1)
		row = self.get_row()
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			column = chr(ord(column) - 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def _right_moves(self):
		"""Return possible moves to the right (increasing column values) of the piece's location."""
		column = chr(ord(self.get_column()) + 1)
		row = self.get_row()
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			column = chr(ord(column) + 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def _up_moves(self):
		"""Return possible moves up (increasing row values) from the piece's location."""
		column = self.get_column()
		row = str(int(self.get_row()) + 1)
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			row = str(int(row) + 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def _down_moves(self):
		"""Return possible moves down (decreasing row values) from the piece's location."""
		column = self.get_column()
		row = str(int(self.get_row()) - 1)
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			row = str(int(row) - 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def _left_up_moves(self):
		"""Return possible moves diagonal (decreasing column, increasing row) from the piece's location."""
		column = chr(ord(self.get_column()) - 1)
		row = str(int(self.get_row()) + 1)
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			column = chr(ord(column) - 1)
			row = str(int(row) + 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def _right_up_moves(self):
		"""Return possible moves diagonal (increasing column, increasing row) from the piece's location."""
		column = chr(ord(self.get_column()) + 1)
		row = str(int(self.get_row()) + 1)
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			column = chr(ord(column) + 1)
			row = str(int(row) + 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def _left_down_moves(self):
		"""Return possible moves diagonal (decreasing column, decreasing row) from the piece's location."""
		column = chr(ord(self.get_column()) - 1)
		row = str(int(self.get_row()) - 1)
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			column = chr(ord(column) - 1)
			row = str(int(row) - 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def _right_down_moves(self):
		"""Return possible moves diagonal (increasing column, decreasing row) from the piece's location."""
		column = chr(ord(self.get_column()) + 1)
		row = str(int(self.get_row()) - 1)
		move = column + row
		moves = []
		while move in self.board and self.board[move] == 'empty':
			moves.append(move)
			column = chr(ord(column) + 1)
			row = str(int(row) - 1)
			move = column + row
		if move in self.board and self.board[move].color != self.color:
			moves.append(move)
		return moves

	def king_position(self):
		"""Return the location of the king in the piece's board with the piece's color."""
		for position in self.board.keys():
			if type(self.board[position]) == King and self.board[position].color == self.color:
				return position

	def valid_move(self, end):
		"""Return if it is legal to move the piece to end."""
		if end not in self.get_moves():
			return False
		copy = deepcopy(self.board)
		piece = copy[self.location]
		copy[self.location] = 'empty'
		copy[end] = piece
		piece.location = end
		king_position = piece.king_position()
		if copy[king_position].check(king_position):
			return False
		return True

	def make_move(self, end):
		"""(Mutating) Move the piece to end."""
		assert self.valid_move(end), 'cannot make invalid move'

		self.board[self.location] = 'empty'
		self.board[end] = self
		self.location = end

		pawns = [pawn for pawn in self.board.values() if pawn != 'empty' and pawn.color == self.color and type(pawn) == Pawn]
		for pawn in pawns:
			pawn.en_passant_left = False
			pawn.en_passant_right = False


class Pawn(Piece):

	def __init__(self, color, location, board, en_passant_left=False, en_passant_right=False, promoted=False):
		"""
		color: 'white' or 'black'.
		location: location of piece in the board.
		board: the chessboard that contains the piece.
		en_passant_left: boolean representing if the pawn may capture en passant to the left.
		en_passant_left: boolean representing if the pawn may capture en passant to the right.
		promoted: boolean representing if the pawn has reached the end of the board.
		"""
		self.color = color
		self.location = location
		self.board = board
		self.en_passant_left = en_passant_left
		self.en_passant_right = en_passant_right
		self.promoted = promoted

	def has_moved(self):
		"""Return if the pawn has made any moves."""
		if self.color == 'white':
			return self.get_row() != '2'
		else:
			return self.get_row() != '7'

	def get_moves(self):
		"""Return possible moves the pawn may make."""
		if self.color == 'white':
			forward = self.get_column() + str(int(self.get_row()) + 1)
			forward2 = self.get_column() + '4'
			left_diagonal = chr(ord(self.get_column()) - 1) + str(int(self.get_row()) + 1)
			right_diagonal = chr(ord(self.get_column()) + 1) + str(int(self.get_row()) + 1)
		else:
			forward = self.get_column() + str(int(self.get_row()) - 1)
			forward2 = self.get_column() + '5'
			left_diagonal = chr(ord(self.get_column()) - 1) + str(int(self.get_row()) - 1)
			right_diagonal = chr(ord(self.get_column()) + 1) + str(int(self.get_row()) - 1)

		moves = []
		if forward in self.board and self.board[forward] == 'empty':
			moves.append(forward)
		if forward2 in self.board and self.board[forward2] == 'empty' and not self.has_moved():
			moves.append(forward2)
		if left_diagonal in self.board and self.board[left_diagonal] != 'empty' and self.board[left_diagonal].color != self.color:
			moves.append(left_diagonal)
		if right_diagonal in self.board and self.board[right_diagonal] != 'empty' and self.board[right_diagonal].color != self.color:
			moves.append(right_diagonal)
		if self.en_passant_left:
			moves.append(left_diagonal)
		if self.en_passant_right:
			moves.append(right_diagonal)
		return moves

	def make_move(self, end):
		"""(Mutating) Move the pawn to end."""
		start = self.location
		old_end = self.board[end]
		Piece.make_move(self, end)
		if (self.color == 'white' and self.get_row() == '8') or (self.color == 'black' and self.get_row() == '1'):
			self.promoted = True
		if (self.color == 'white' and start[1] == '2' and end[1] == '4') or (self.color == 'black' and start[1] == '7' and end[1] == '5'):
			left = chr(ord(end[0]) - 1) + end[1]
			right = chr(ord(end[0]) + 1) + end[1]
			if left in self.board and type(self.board[left]) == Pawn and self.board[left].color != self.color:
				self.board[left].en_passant_right = True
			if right in self.board and type(self.board[right]) == Pawn and self.board[right].color != self.color:
				self.board[right].en_passant_left = True
		if start[0] != end[0] and old_end == 'empty':
			self.board[end[0] + start[1]] = 'empty'


class Rook(Piece):

	def __init__(self, color, location, board, moved=False):
		"""
		color: 'white' or 'black'.
		location: location of piece in the board.
		board: the chessboard that contains the piece.
		moved: boolean, representing if the rook has made any moves.
		"""
		self.color = color
		self.location = location
		self.board = board
		self.moved = moved

	def has_moved(self):
		"""Return if the rook has made any moves."""
		return self.moved

	def get_moves(self):
		"""Return possible moves the rook may make."""
		return self._left_moves() + self._right_moves() + self._up_moves() + self._down_moves()

	def make_move(self, end):
		"""(Mutating) Move the rook to end."""
		Piece.make_move(self, end)
		self.moved = True


class Knight(Piece):

	def get_moves(self):
		"""Return possible moves the knight may make."""
		moves = [
		chr(ord(self.get_column()) + 2) + str(int(self.get_row()) - 1),
		chr(ord(self.get_column()) + 2) + str(int(self.get_row()) + 1),
		chr(ord(self.get_column()) - 2) + str(int(self.get_row()) + 1),
		chr(ord(self.get_column()) - 2) + str(int(self.get_row()) - 1),
		chr(ord(self.get_column()) + 1) + str(int(self.get_row()) - 2),
		chr(ord(self.get_column()) + 1) + str(int(self.get_row()) + 2),
		chr(ord(self.get_column()) - 1) + str(int(self.get_row()) - 2),
		chr(ord(self.get_column()) - 1) + str(int(self.get_row()) + 2),
		]
		return [move for move in moves if (move in self.board and (self.board[move] == 'empty' or self.board[move].color != self.color))]


class Bishop(Piece):

	def get_moves(self):
		"""Return possible moves the bishop may make."""
		return self._left_up_moves() + self._right_up_moves() + self._left_down_moves() + self._right_down_moves()


class Queen(Piece):

	def get_moves(self):
		"""Return possible moves the queen may make."""
		return self._left_moves() + self._right_moves() + self._up_moves() + self._down_moves() + self._left_up_moves() + self._right_up_moves() + self._left_down_moves() + self._right_down_moves()


class King(Piece):

	def __init__(self, color, location, board, moved=False):
		"""
		color: 'white' or 'black'.
		location: location of piece in the board.
		board: the chessboard that contains the piece.
		moved: boolean, representing if the rook has made any moves.
		"""
		self.color = color
		self.location = location
		self.board = board
		self.moved = moved

	def has_moved(self):
		"""Return if the king has made any moves."""
		return self.moved

	def check(self, location):
		"""Return if the king would be in check at location."""
		copy = deepcopy(self.board)
		copy[location] = King(self.color, location, copy)
		opponent_pieces = [opponent for opponent in copy.values() if opponent != 'empty' and opponent.color != self.color]
		for opponent in opponent_pieces:
			if type(opponent) == King:
				if location in opponent.standard_moves():
					return True
			elif location in opponent.get_moves():
				return True
		return False

	def _castle(self):
		"""Return the legal castling moves the king may make."""
		moves = []
		if self.color == 'white':
			if not self.has_moved() and type(self.board['a1']) == Rook and not self.board['a1'].has_moved():
				if self.board['b1'] == 'empty' and self.board['c1'] == 'empty' and self.board['d1'] == 'empty':
					if not self.check(self.location) and not self.check('c1') and not self.check('d1'):
						moves.append('c1')
			if not self.has_moved() and type(self.board['h1']) == Rook and not self.board['h1'].has_moved():
				if self.board['f1'] == 'empty' and self.board['g1'] == 'empty':
					if not self.check(self.location) and not self.check('f1') and not self.check('g1'):
						moves.append('g1')
		else:
			if not self.has_moved() and type(self.board['a8']) == Rook and not self.board['a8'].has_moved():
				if self.board['b8'] == 'empty' and self.board['c8'] == 'empty' and self.board['d8'] == 'empty':
					if not self.check(self.location) and not self.check('c8') and not self.check('d8'):
						moves.append('c8')
			if not self.has_moved() and type(self.board['h8']) == Rook and not self.board['h8'].has_moved():
				if self.board['f8'] == 'empty' and self.board['g8'] == 'empty':
					if not self.check(self.location) and not self.check('f8') and not self.check('g8'):
						moves.append('g8')
		return moves

	def standard_moves(self):
		"""Return possible moves the king may make, excluding castling moves."""
		moves = [
		chr(ord(self.get_column()) - 1) + str(int(self.get_row()) - 1),
		chr(ord(self.get_column()) - 1) + self.get_row(),
		chr(ord(self.get_column()) - 1) + str(int(self.get_row()) + 1),
		self.get_column() + str(int(self.get_row()) - 1),
		self.get_column() + str(int(self.get_row()) + 1),
		chr(ord(self.get_column()) + 1) + str(int(self.get_row()) -1),
		chr(ord(self.get_column()) + 1) + self.get_row(),
		chr(ord(self.get_column()) + 1) + str(int(self.get_row()) + 1),
		]
		return [move for move in moves if (move in self.board and (self.board[move] == 'empty' or self.board[move].color != self.color))]

	def get_moves(self):
		"""Return possible moves the king may make."""
		return self.standard_moves() + self._castle()

	def make_move(self, end):
		"""(Mutating) Move the king to end."""
		Piece.make_move(self, end)

		if not self.moved and end == 'c1':
			self.board['a1'] = 'empty'
			self.board['d1'] = Rook('white', 'd1', self.board, True)
		if not self.moved and end == 'g1':
			self.board['h1'] = 'empty'
			self.board['f1'] = Rook('white', 'f1', self.board, True)
		if not self.moved and end == 'c8':
			self.board['a8'] = 'empty'
			self.board['d8'] = Rook('black', 'd8', self.board, True)
		if not self.moved and end == 'g8':
			self.board['h8'] = 'empty'
			self.board['f8'] = Rook('black', 'f8', self.board, True)
		self.moved = True
