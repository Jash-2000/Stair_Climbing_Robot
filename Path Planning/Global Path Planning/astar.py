import math
import pygame
from queue import PriorityQueue

"""
	This is the Heuristic Function that measures the Manhattan distance of 2 points.
	Essentially, in our case the distance would be between the next node and the final point.
"""
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

"""
	
"""
def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

"""
	The main function of the entire algorithm, that contains an inner loop for runnin through all the 
	required nodes. Astar is an informed search algorithm, hence, it will definately not run through
	all the nodes in the graph.
"""
def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))				# f, count, node
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}		# Dictionary
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}					# To check the contents of Priority Queue.

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1			# Assumed that each step is 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False