import string


class RubiksCube:
	def __init__(self):
		# Initialize a solved cube (6 faces, each with 9 squares)
		self.faces = {
			'U': [['W'] * 3 for _ in range(3)],  # Up - White
			'D': [['Y'] * 3 for _ in range(3)],  # Down - Yellow
			'L': [['O'] * 3 for _ in range(3)],  # Left - Orange
			'R': [['R'] * 3 for _ in range(3)],  # Right - Red
			'F': [['G'] * 3 for _ in range(3)],  # Front - Green
			'B': [['B'] * 3 for _ in range(3)]   # Back - Blue
			# 'U': [['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']],  # Up - White
			# 'D': [['D1', 'D2', 'D3'], ['D4', 'D5', 'D6'], ['D7', 'D8', 'D9']],  # Down - Yellow
			# 'L': [['L1', 'L2', 'L3'], ['L4', 'L5', 'L6'], ['L7', 'L8', 'L9']],  # Left - Orange
			# 'R': [['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']],  # Right - Red
			# 'F': [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']],  # Front - Green
			# 'B': [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']]   # Back - Blue
		}

	def display_in_term(self):
		"""Display the cube state"""
		print("Current state of the Rubik's Cube:")
		for face_name, face in self.faces.items():
			print("\n" + face_name + " face:")
			for row in face:
				print(row)


	def display_visual3D(self):
		"""Placeholder for graphical display of the cube"""
		print("Graphical display not implemented yet.")



	def _deep_copy_faces(self):
		"""Create a deep copy of all faces"""
		copy = {}
		for face_name, face in self.faces.items():
			copy[face_name] = [row[:] for row in face]
		return copy

	# Additional methods for cube manipulation can be added here


	def rotate_face_cw(self, face_name):

		faces = self.faces
		facescpy = self._deep_copy_faces()

		faces[face_name][0][0] = facescpy[face_name][2][0]
		faces[face_name][0][1] = facescpy[face_name][1][0]
		faces[face_name][0][2] = facescpy[face_name][0][0]
		faces[face_name][1][0] = facescpy[face_name][2][1]
		faces[face_name][1][2] = facescpy[face_name][0][1]
		
		faces[face_name][2][0] = facescpy[face_name][2][2]
		faces[face_name][2][1] = facescpy[face_name][1][2]
		faces[face_name][2][2] = facescpy[face_name][0][2]

		return faces, facescpy

#################################
# BASIC MOVES
#################################

	def Up(self):
		"""Rotate the upper face clockwise"""
		
		# Rotate the U face clockwise
		faces, facescpy = self.rotate_face_cw('U')

		# Cycle the edges (L, F, R, B faces)
		faces['L'][0] = facescpy['F'][0]
		faces['F'][0] = facescpy['R'][0]
		faces['R'][0] = facescpy['B'][0]
		faces['B'][0] = facescpy['L'][0]



	def Down(self):
		"""Rotate the down face clockwise"""

		# Rotate the D face clockwise
		faces, facescpy = self.rotate_face_cw('D')

		# Cycle the edges (L, F, R, B faces)
		faces['L'][2] = facescpy['B'][2]
		faces['F'][2] = facescpy['L'][2]
		faces['R'][2] = facescpy['F'][2]
		faces['B'][2] = facescpy['R'][2]


	def Right(self):
		"""Rotate the right face clockwise"""

		# Rotate the R face clockwise
		faces, facescpy = self.rotate_face_cw('R')

		# Cycle the edges (U, F, D, B faces)
		for i in range(3):
			faces['U'][i][2] = facescpy['F'][i][2]
			faces['F'][i][2] = facescpy['D'][i][2]
			faces['D'][i][2] = facescpy['B'][2 - i][0]
			faces['B'][i][0] = facescpy['U'][2 - i][2]



	def Left(self):
		"""Rotate the left face clockwise"""

		# Rotate the L face clockwise
		faces, facescpy = self.rotate_face_cw('L')
		
		# Cycle the edges (U, F, D, B faces)
		for i in range(3):
			faces['U'][i][0] = facescpy['B'][2 - i][2]
			faces['F'][i][0] = facescpy['U'][i][0]
			faces['D'][i][0] = facescpy['F'][i][0]
			faces['B'][i][2] = facescpy['D'][2 - i][0]


	def Front(self):
		"""Rotate the upper face clockwise"""
		
		# Rotate the F face clockwise
		faces, facescpy = self.rotate_face_cw('F')

		# Cycle the edges (L, D, R, U faces)
		for i in range(3):
			faces['L'][i][2] = facescpy['D'][0][i]
			faces['D'][0][i] = facescpy['R'][2 - i][0]
			faces['R'][i][0] = facescpy['U'][2][i]
			faces['U'][2][i] = facescpy['L'][2 - i][2]


	def Back(self):
		"""Rotate the back face clockwise"""

		# Rotate the B face clockwise
		faces, facescpy = self.rotate_face_cw('B')
		
		# Cycle the edges (U, R, D, L faces)
		for i in range(3):
			faces['U'][0][i] = facescpy['R'][i][2]
			faces['R'][i][2] = facescpy['D'][2][2 - i]
			faces['D'][2][i] = facescpy['L'][i][0]
			faces['L'][i][0] = facescpy['U'][0][2 - i]


	def apply_move(self, move):
		"""Apply a move to the cube"""
		if move == "U":
			self.Up()
			print("U")
		elif move == "U'":
			self.Up()
			self.Up()
			self.Up()
			print("U'")
	
		elif move == "D":
			self.Down()
			print("D")
		elif move == "D'":
			self.Down()
			self.Down()
			self.Down()
			print("D'")
	
		elif move == "R":
			self.Right()
			print("R")
		elif move == "R'":
			self.Right()
			self.Right()
			self.Right()
			print("R'")
	
		elif move == "L":
			self.Left()
			print("L")
		elif move == "L'":
			self.Left()
			self.Left()
			self.Left()
			print("L'")
	
		elif move == "F":
			self.Front()
			print("F")
		elif move == "F'":
			self.Front()
			self.Front()
			self.Front()
			print("F'")
	
		elif move == "B":
			self.Back()
			print("B")
		elif move == "B'":
			self.Back()
			self.Back()
			self.Back()
			print("B'")
	
		else:
			print(f"Invalid move: {move}")


	def input_receiver(self, string):
		"""Parse a string of moves and apply them to the cube"""
		moves = string.split()
		print(" all moves: ", moves)
		for move in moves:
			self.apply_move(move)


# Main program
if __name__ == "__main__":
	print("=== Rubik ===")
	cube = RubiksCube()
	cube.display_in_term()
