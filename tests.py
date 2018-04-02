from nographics import *
import unittest


class TestPawn(unittest.TestCase):

	def test_pawn(self):
		board = starting_board()

		white_pawn = board['a2']
		self.assertEqual(type(white_pawn), Pawn)
		self.assertEqual(white_pawn.get_column(), 'a')
		self.assertEqual(white_pawn.get_row(), '2')
		self.assertEqual(white_pawn.king_position(), 'e1')
		self.assertFalse(white_pawn.has_moved())
		self.assertEqual(set(white_pawn.get_moves()), set(['a3', 'a4']))
		self.assertFalse(white_pawn.valid_move('b3'))
		self.assertTrue(white_pawn.valid_move('a4'))

		black_pawn = board['b7']
		self.assertEqual(type(black_pawn), Pawn)
		self.assertEqual(black_pawn.get_column(), 'b')
		self.assertEqual(black_pawn.get_row(), '7')
		self.assertEqual(black_pawn.king_position(), 'e8')
		self.assertFalse(black_pawn.has_moved())
		self.assertEqual(set(black_pawn.get_moves()), set(['b6', 'b5']))
		self.assertFalse(black_pawn.valid_move('a6'))
		self.assertTrue(black_pawn.valid_move('b5'))

		white_pawn.make_move('a4')
		self.assertFalse(white_pawn.valid_move('b5'))
		black_pawn.make_move('b5')
		self.assertTrue(white_pawn.valid_move('b5'))


class TestRook(unittest.TestCase):

	def test_rook(self):
		board = starting_board()

		rook = board['a1']
		self.assertEqual(type(rook), Rook)
		self.assertEqual(rook.get_column(), 'a')
		self.assertEqual(rook.get_row(), '1')
		self.assertEqual(rook.king_position(), 'e1')
		self.assertEqual(set(rook.get_moves()), set())

		board['a2'].make_move('a4')
		board['b7'].make_move('b6')
		self.assertEqual(set(rook.get_moves()), set(['a2', 'a3']))
		self.assertFalse(rook.valid_move('a4'))
		self.assertTrue(rook.valid_move('a3'))
		self.assertFalse(rook.has_moved())
		rook.make_move('a2')
		board['b6'].make_move('b5')
		rook.make_move('a1')
		self.assertTrue(rook.has_moved())
		board['b5'].make_move('a4')
		self.assertEqual(set(rook.get_moves()), set(['a2', 'a3', 'a4']))


class TestKnight(unittest.TestCase):

	def test_knight(self):
		board = starting_board()

		white_knight = board['b1']
		self.assertEqual(type(white_knight), Knight)
		self.assertEqual(white_knight.get_column(), 'b')
		self.assertEqual(white_knight.get_row(), '1')
		self.assertEqual(white_knight.king_position(), 'e1')
		self.assertEqual(set(white_knight.get_moves()), set(['a3', 'c3']))
		self.assertFalse(white_knight.valid_move('d2'))
		self.assertTrue(white_knight.valid_move('a3'))

		black_knight = board['g8']
		self.assertEqual(type(black_knight), Knight)
		self.assertEqual(black_knight.get_column(), 'g')
		self.assertEqual(black_knight.get_row(), '8')
		self.assertEqual(black_knight.king_position(), 'e8')
		self.assertEqual(set(black_knight.get_moves()), set(['f6', 'h6']))
		self.assertFalse(black_knight.valid_move('e7'))
		self.assertTrue(black_knight.valid_move('h6'))

		white_knight.make_move('c3')
		black_knight.make_move('f6')
		self.assertEqual(set(black_knight.get_moves()), set(['g8', 'd5', 'h5', 'e4', 'g4']))
		white_knight.make_move('e4')
		self.assertEqual(set(black_knight.get_moves()), set(['g8', 'd5', 'h5', 'e4', 'g4']))


class TestBishop(unittest.TestCase):

	def test_bishop(self):
		board = starting_board()

		white_bishop = board['f1']
		self.assertEqual(type(white_bishop), Bishop)
		self.assertEqual(white_bishop.get_column(), 'f')
		self.assertEqual(white_bishop.get_row(), '1')
		self.assertEqual(white_bishop.king_position(), 'e1')
		self.assertEqual(set(white_bishop.get_moves()), set())
		self.assertFalse(white_bishop.valid_move('g2'))

		black_bishop = board['c8']
		self.assertEqual(type(black_bishop), Bishop)
		self.assertEqual(black_bishop.get_column(), 'c')
		self.assertEqual(black_bishop.get_row(), '8')
		self.assertEqual(black_bishop.king_position(), 'e8')
		self.assertEqual(set(black_bishop.get_moves()), set())
		self.assertFalse(black_bishop.valid_move('b7'))

		board['g2'].make_move('g3')
		board['b7'].make_move('b6')
		self.assertTrue(white_bishop.valid_move('g2'))
		white_bishop.make_move('g2')
		self.assertEqual(set(white_bishop.get_moves()), set(['f1', 'h3', 'f3', 'e4', 'd5', 'c6', 'b7', 'a8']))
		self.assertTrue(black_bishop.valid_move('b7'))
		black_bishop.make_move('b7')
		self.assertEqual(set(white_bishop.get_moves()), set(['f1', 'h3', 'f3', 'e4', 'd5', 'c6', 'b7']))


class TestQueen(unittest.TestCase):

	def test_queen(self):
		board = starting_board()

		queen = board['d1']
		self.assertEqual(type(queen), Queen)
		self.assertEqual(queen.get_column(), 'd')
		self.assertEqual(queen.get_row(), '1')
		self.assertEqual(queen.king_position(), 'e1')
		self.assertEqual(set(queen.get_moves()), set())

		self.assertFalse(queen.valid_move('f3'))
		board['e2'].make_move('e3')
		board['h7'].make_move('h5')
		self.assertTrue(queen.valid_move('f3'))
		self.assertEqual(set(queen.get_moves()), set(['e2', 'f3', 'g4', 'h5']))
		queen.make_move('f3')
		board['f7'].make_move('f5')
		self.assertEqual(set(queen.get_moves()), set(['b7', 'c6', 'd5', 'e4', 'd1', 'e2', 'g4', 'h5', 'g3', 'h3', 'f4', 'f5']))


class TestKing(unittest.TestCase):

	def test_king(self):
		board = starting_board()

		king = board['e1']
		self.assertEqual(type(king), King)
		self.assertEqual(king.get_column(), 'e')
		self.assertEqual(king.get_row(), '1')
		self.assertEqual(king.king_position(), 'e1')
		self.assertFalse(king.has_moved())
		self.assertEqual(set(king.get_moves()), set())

		board['e2'].make_move('e4')
		board['e7'].make_move('e5')
		board['f2'].make_move('f4')
		board['d8'].make_move('f6')
		board['f1'].make_move('d3')
		board['f6'].make_move('f4')
		board['g1'].make_move('h3')
		board['f8'].make_move('c5')

		self.assertEqual(set(king.get_moves()), set(['e2', 'f1', 'f2']))
		self.assertTrue(king.valid_move('e2'))
		self.assertFalse(king.valid_move('f1'))
		self.assertFalse(king.valid_move('f2'))
		self.assertFalse(king.check('e2'))
		self.assertTrue(king.check('f1'))
		self.assertTrue(king.check('f2'))

		board['h3'].make_move('f4')

		self.assertEqual(set(king.get_moves()), set(['e2', 'f1', 'f2']))
		self.assertTrue(king.valid_move('e2'))
		self.assertTrue(king.valid_move('f1'))
		self.assertFalse(king.valid_move('f2'))
		self.assertFalse(king.check('e2'))
		self.assertFalse(king.check('f1'))
		self.assertTrue(king.check('f2'))

		board['c5'].make_move('b4')

		self.assertEqual(set(king.get_moves()), set(['e2', 'f1', 'f2', 'g1']))
		self.assertTrue(king.valid_move('e2'))
		self.assertTrue(king.valid_move('f1'))
		self.assertTrue(king.valid_move('f2'))
		self.assertTrue(king.valid_move('g1'))
		self.assertFalse(king.check('e2'))
		self.assertFalse(king.check('f1'))
		self.assertFalse(king.check('f2'))
		self.assertFalse(king.check('g1'))

		king.make_move('e2')
		board['g8'].make_move('f6')
		king.make_move('e1')

		self.assertTrue(king.has_moved())
		self.assertEqual(set(king.get_moves()), set(['e2', 'f1', 'f2']))
		self.assertTrue(king.valid_move('e2'))
		self.assertTrue(king.valid_move('f1'))
		self.assertTrue(king.valid_move('f2'))
		self.assertFalse(king.valid_move('g1'))
		self.assertFalse(king.check('e2'))
		self.assertFalse(king.check('f1'))
		self.assertFalse(king.check('f2'))
		self.assertFalse(king.check('g1'))


class TestCastle(unittest.TestCase):

	def test_castle_kingside(self):
		board = starting_board()

		board['e2'].make_move('e4')
		board['e7'].make_move('e5')
		board['g1'].make_move('f3')
		board['g8'].make_move('f6')
		board['f1'].make_move('c4')
		board['f8'].make_move('c5')

		self.assertFalse(board['e1'].has_moved())
		self.assertFalse(board['h1'].has_moved())
		self.assertTrue(board['e1'].valid_move('g1'))
		board['e1'].make_move('g1')
		self.assertEqual(type(board['g1']), King)
		self.assertEqual(type(board['f1']), Rook)
		self.assertEqual(board['e1'], 'empty')
		self.assertEqual(board['h1'], 'empty')
		self.assertTrue(board['g1'].has_moved())
		self.assertTrue(board['f1'].has_moved())

		self.assertFalse(board['e8'].has_moved())
		self.assertFalse(board['h8'].has_moved())
		self.assertTrue(board['e8'].valid_move('g8'))
		board['e8'].make_move('g8')
		self.assertEqual(type(board['g8']), King)
		self.assertEqual(type(board['f8']), Rook)
		self.assertEqual(board['e8'], 'empty')
		self.assertEqual(board['h8'], 'empty')
		self.assertTrue(board['g8'].has_moved())
		self.assertTrue(board['f8'].has_moved())

	def test_castle_queenside(self):
		board = starting_board()

		board['e2'].make_move('e4')
		board['e7'].make_move('e5')
		board['d2'].make_move('d4')
		board['d7'].make_move('d5')
		board['d1'].make_move('f3')
		board['d8'].make_move('f6')
		board['c1'].make_move('f4')
		board['c8'].make_move('f5')
		board['b1'].make_move('c3')
		board['b8'].make_move('c6')

		self.assertFalse(board['e1'].has_moved())
		self.assertFalse(board['a1'].has_moved())
		self.assertTrue(board['e1'].valid_move('c1'))
		board['e1'].make_move('c1')
		self.assertEqual(type(board['c1']), King)
		self.assertEqual(type(board['d1']), Rook)
		self.assertEqual(board['a1'], 'empty')
		self.assertEqual(board['b1'], 'empty')
		self.assertEqual(board['e1'], 'empty')
		self.assertTrue(board['c1'].has_moved())
		self.assertTrue(board['d1'].has_moved())

		self.assertFalse(board['e8'].has_moved())
		self.assertFalse(board['a8'].has_moved())
		self.assertTrue(board['e8'].valid_move('c8'))
		board['e8'].make_move('c8')
		self.assertEqual(type(board['c8']), King)
		self.assertEqual(type(board['d8']), Rook)
		self.assertEqual(board['a8'], 'empty')
		self.assertEqual(board['b8'], 'empty')
		self.assertEqual(board['e8'], 'empty')
		self.assertTrue(board['c8'].has_moved())
		self.assertTrue(board['d8'].has_moved())


class TestPromotion(unittest.TestCase):

	def test_promotion_queen(self):
		board = starting_board()

		white_pawn = board['c2']
		black_pawn = board['a7']

		white_pawn.make_move('c4')
		black_pawn.make_move('a5')
		white_pawn.make_move('c5')
		black_pawn.make_move('a4')
		white_pawn.make_move('c6')
		black_pawn.make_move('a3')
		white_pawn.make_move('b7')
		black_pawn.make_move('b2')

		self.assertFalse(white_pawn.promoted)
		white_pawn.make_move('a8')
		self.assertTrue(white_pawn.promoted)
		promote(board, 'Queen', 'white', 'a8')
		self.assertEqual(type(board['a8']), Queen)

		self.assertFalse(black_pawn.promoted)
		black_pawn.make_move('c1')
		self.assertTrue(black_pawn.promoted)
		promote(board, 'Queen', 'black', 'c1')
		self.assertEqual(type(board['c1']), Queen)

	def test_promotion_rook(self):
		board = starting_board()

		white_pawn = board['a2']
		black_pawn = board['c7']

		white_pawn.make_move('a4')
		black_pawn.make_move('c5')
		white_pawn.make_move('a5')
		black_pawn.make_move('c4')
		white_pawn.make_move('a6')
		black_pawn.make_move('c3')
		white_pawn.make_move('b7')
		black_pawn.make_move('b2')

		self.assertFalse(white_pawn.promoted)
		white_pawn.make_move('c8')
		self.assertTrue(white_pawn.promoted)
		promote(board, 'Rook', 'white', 'c8')
		self.assertEqual(type(board['c8']), Rook)

		self.assertFalse(black_pawn.promoted)
		black_pawn.make_move('a1')
		self.assertTrue(black_pawn.promoted)
		promote(board, 'Rook', 'black', 'a1')
		self.assertEqual(type(board['a1']), Rook)

	def test_promotion_bishop(self):
		board = starting_board()

		white_pawn = board['f2']
		black_pawn = board['h7']

		white_pawn.make_move('f4')
		black_pawn.make_move('h5')
		white_pawn.make_move('f5')
		black_pawn.make_move('h4')
		white_pawn.make_move('f6')
		black_pawn.make_move('h3')
		white_pawn.make_move('g7')
		black_pawn.make_move('g2')

		self.assertFalse(white_pawn.promoted)
		white_pawn.make_move('f8')
		self.assertTrue(white_pawn.promoted)
		promote(board, 'Bishop', 'white', 'f8')
		self.assertEqual(type(board['f8']), Bishop)

		self.assertFalse(black_pawn.promoted)
		black_pawn.make_move('h1')
		self.assertTrue(black_pawn.promoted)
		promote(board, 'Bishop', 'black', 'h1')
		self.assertEqual(type(board['h1']), Bishop)

	def test_promotion_knight(self):
		board = starting_board()

		white_pawn = board['h2']
		black_pawn = board['f7']

		white_pawn.make_move('h4')
		black_pawn.make_move('f5')
		white_pawn.make_move('h5')
		black_pawn.make_move('f4')
		white_pawn.make_move('h6')
		black_pawn.make_move('f3')
		white_pawn.make_move('g7')
		black_pawn.make_move('g2')

		self.assertFalse(white_pawn.promoted)
		white_pawn.make_move('h8')
		self.assertTrue(white_pawn.promoted)
		promote(board, 'Knight', 'white', 'h8')
		self.assertEqual(type(board['h8']), Knight)

		self.assertFalse(black_pawn.promoted)
		black_pawn.make_move('f1')
		self.assertTrue(black_pawn.promoted)
		promote(board, 'Knight', 'black', 'f1')
		self.assertEqual(type(board['f1']), Knight)


class TestEnPassant(unittest.TestCase):

	def test_en_passant(self):
		board = starting_board()

		pawn = board['e2']
		pawn.make_move('e4')
		board['e7'].make_move('e6')
		pawn.make_move('e5')
		board['d7'].make_move('d5')
		self.assertTrue(pawn.en_passant_left)
		self.assertFalse(pawn.en_passant_right)
		self.assertTrue(pawn.valid_move('d6'))
		self.assertFalse(pawn.valid_move('f6'))
		board['g1'].make_move('f3')
		board['f7'].make_move('f5')
		self.assertFalse(pawn.en_passant_left)
		self.assertTrue(pawn.en_passant_right)
		self.assertFalse(pawn.valid_move('d6'))
		self.assertTrue(pawn.valid_move('f6'))
		board['f3'].make_move('g1')
		board['g8'].make_move('f6')
		self.assertFalse(pawn.en_passant_left)
		self.assertFalse(pawn.en_passant_right)
		self.assertFalse(pawn.valid_move('d6'))
		self.assertTrue(pawn.valid_move('f6'))


if __name__ == '__main__':
	unittest.main()
