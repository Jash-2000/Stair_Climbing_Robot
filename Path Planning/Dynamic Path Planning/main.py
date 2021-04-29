from draw import *
from astar import *

import pygame
import math
from queue import PriorityQueue

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

def man(win, width):
	# ROWS = 50			# Can be changed by the user in case not using the image.
	# grid = make_grid(ROWS, width, img)

	grid = make_grid(ROWS, width, img)
	start = None
	end = None

	run = True			# If True, Pygame engine would work.
	while run:
		draw(win, grid, ROWS, width)			# Showing Colour of each node at every iteration.
		
		# Getting event type output from Pygame engine 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				# Comment the following elif conditions for not letting users add additional Obstacles.
				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_t:
					pass

				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_r:
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()

## Defining the Main menu that would be displayed.
input("Are you sure that you want to move forward with this?")
print("\n\n Pixelizing the image now. Press 't' to toggle between the robot's view and spectator's view.")
man(WIN, WIDTH)