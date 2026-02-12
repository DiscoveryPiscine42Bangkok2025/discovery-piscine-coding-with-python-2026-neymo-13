def checkmate(board_string):
	lines = board_string.strip().split()
	board = [list(line) for line in lines]
	size = len(board)

	if not is_square_board(board):
		print("Error")
		return

	king_pos = None
	king_count = 0
	enemy_pieces = []

	for row in range(size):
		for col in range(size):
			cell = board[row][col]

			# non-piece characters จะถือว่าเป็นช่องว่าง
			if cell not in "KPBRQ":
				continue
			if cell == 'K':
				king_count += 1
				king_pos = (row, col)
			else:
				enemy_pieces.append((cell, (row, col)))

	if king_count != 1:
		print("Error")
		return

	for piece, enemy_pos in enemy_pieces:
		if can_attack_king(piece, enemy_pos, king_pos, board):
			print("Success")
			return

	print("Fail")

def is_square_board(board):
	size = len(board)
	for row in board:
		if len(row) != size:
			return False
	return True

def can_attack_king(piece, ene_pos, king_pos, board):
	if piece == 'P':
		return check_pawn(ene_pos, king_pos)
	if piece in ('R', 'Q'):
		if check_line(ene_pos, king_pos, board, rook_like=True):
			return True
	if piece in ('B', 'Q'):
		if check_line(ene_pos, king_pos, board, rook_like=False):
			return True
	return False

def check_pawn(pos, king_pos):
	er, ec = pos
	return (er - 1, ec - 1) == king_pos or \
		   (er - 1, ec + 1) == king_pos

def get_step(from_pos, to_pos):
	if from_pos == to_pos:
		return 0
	elif to_pos > from_pos:
		return 1
	else:
		return -1

def check_line(ene_pos, king_pos, board, rook_like):
	"""
	rook_like = True แนวตรง (Rook)
	rook_like = False แนวทแยง (Bishop)
	"""
	kr, kc = king_pos
	er, ec = ene_pos
	n = len(board)

	if rook_like:
		# ต้องอยู่แนวเดียวกัน
		if er != kr and ec != kc:
			return False
	else:
		# ต้องอยู่แนวทแยงเดียวกัน
		if abs(er - kr) != abs(ec - kc):
			return False

	step_row = get_step(er, kr)
	step_col = get_step(ec, kc)

	r = er + step_row
	c = ec + step_col

	while 0 <= r < n and 0 <= c < n:
		if (r, c) == (kr, kc):
			return True
		if board[r][c] in "PBRQ":
			break
		r += step_row
		c += step_col

	return False
