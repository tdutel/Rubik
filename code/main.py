from rubik import RubiksCube

def main():
	cube = RubiksCube()
	print("Rubik's cube created successfully!")
	# cube.display_in_term()
	# cube.display_visual3D()
	# cube.Up()
	# cube.Up()
	# cube.display_in_term()
	# cube.Down()
	# cube.Down()

	# cube.display_in_term()
	cube.Right()
	# cube.Right()
	# cube.display_in_term()
	cube.Up()
	# cube.display_in_term()
	cube.Left()
	# cube.Left()
	# cube.Front()
	# cube.Front()
	cube.Back()
	# cube.display_in_term()
if __name__ == "__main__":
	main()
