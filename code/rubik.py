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

		face = self.faces
		facecpy = self._deep_copy_faces()

		face[face_name][0][0] = facecpy[face_name][2][0]
		face[face_name][0][1] = facecpy[face_name][1][0]
		face[face_name][0][2] = facecpy[face_name][0][0]

		face[face_name][1][0] = facecpy[face_name][2][1]
		face[face_name][1][2] = facecpy[face_name][0][1]
		
		face[face_name][2][0] = facecpy[face_name][2][2]
		face[face_name][2][1] = facecpy[face_name][1][2]
		face[face_name][2][2] = facecpy[face_name][0][2]

		return face, facecpy

	def Up(self):
		"""Rotate the upper face clockwise"""
		
		# Rotate the U face clockwise
		face, facecpy = self.rotate_face_cw('U')

		# Cycle the edges (L, F, R, B faces)
		face['L'][0] = facecpy['F'][0]
		face['F'][0] = facecpy['R'][0]
		face['R'][0] = facecpy['B'][0]
		face['B'][0] = facecpy['L'][0]

		print("U")


	def Down(self):
		"""Rotate the down face clockwise"""

		# Rotate the D face clockwise
		face, facecpy = self.rotate_face_cw('D')

		# Cycle the edges (L, F, R, B faces)
		face['L'][2] = facecpy['B'][2]
		face['F'][2] = facecpy['L'][2]
		face['R'][2] = facecpy['F'][2]
		face['B'][2] = facecpy['R'][2]

		print("D")


	def Right(self):
		"""Rotate the right face clockwise"""

		# Rotate the R face clockwise
		face, facecpy = self.rotate_face_cw('R')

		# Cycle the edges (U, F, D, B faces)
		for i in range(3):
			face['U'][i][2] = facecpy['F'][i][2]
			face['F'][i][2] = facecpy['D'][i][2]
			face['D'][i][2] = facecpy['B'][2 - i][0]
			face['B'][i][0] = facecpy['U'][2 - i][2]

		print("R")


	def Left(self):
		"""Rotate the left face clockwise"""

		# Rotate the L face clockwise
		face, facecpy = self.rotate_face_cw('L')
		
		# Cycle the edges (U, F, D, B faces)
		for i in range(3):
			face['U'][i][0] = facecpy['B'][2 - i][2]
			face['F'][i][0] = facecpy['U'][i][0]
			face['D'][i][0] = facecpy['F'][i][0]
			face['B'][i][2] = facecpy['D'][2 - i][0]

		print("L")


	def Front(self):
		"""Rotate the upper face clockwise"""
		
		# Rotate the F face clockwise
		face, facecpy = self.rotate_face_cw('F')

		# Cycle the edges (L, D, R, U faces)
		for i in range(3):
			face['L'][i][2] = facecpy['D'][0][i]
			face['D'][0][i] = facecpy['R'][2 - i][0]
			face['R'][i][0] = facecpy['U'][2][i]
			face['U'][2][i] = facecpy['L'][2 - i][2]

		print("F")


	def Back(self):
		"""Rotate the back face clockwise"""

		# Rotate the B face clockwise
		face, facecpy = self.rotate_face_cw('B')
		
		# Cycle the edges (U, R, D, L faces)
		for i in range(3):
			face['U'][0][i] = facecpy['R'][i][2]
			face['R'][i][2] = facecpy['D'][2][2 - i]
			face['D'][2][i] = facecpy['L'][i][0]
			face['L'][i][0] = facecpy['U'][0][2 - i]

		print("B")



	# def display(self):
	# 	"""Display the cube state"""
	# 	for face_name, face in self.faces.items():
	# 		print(f"\n{face_name} face:")
	# 		for row in face:
	# 			print(' '.join(row))
	
	# def rotate_face_cw(self, face_name):
	# 	"""Rotate a face clockwise"""
	# 	face = self.faces[face_name]
	# 	# Transpose and reverse to rotate clockwise
	# 	for i in range(3):
	# 		for j in range(i, 3):
	# 			face[i][j], face[j][i] = face[j][i], face[i][j]
	# 	for row in face:
	# 		row.reverse()
	
	# def rotate_U(self):
	# 	"""Rotate upper face"""
	# 	self.rotate_face_cw('U')
	# 	# Cycle edges
	# 	temp = [row[0:3] for row in [self.faces['F'][0]]]
	# 	self.faces['F'][0] = self.faces['R'][0]
	# 	self.faces['R'][0] = self.faces['B'][0]
	# 	self.faces['B'][0] = self.faces['L'][0]
	# 	self.faces['L'][0] = temp[0]

# Main program
if __name__ == "__main__":
	print("=== Rubik ===")
	cube = RubiksCube()
	cube.display_in_term()
