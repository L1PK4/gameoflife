import pygame
import numpy as np
from random import choice

cell_a = 2
cell_x, cell_y = 100, 100
w, h = cell_x * cell_a, cell_y * cell_a

bg = (255, 255, 255)
cell_clr = (0, 0, 0) 

pygame.init()
screen = pygame.display.set_mode((w, h))

temp = [[choice([True, False]) for _ in range(cell_y)] for _ in range(cell_x)]

cells = np.array(temp, dtype=bool)

run = True
while run:
	screen.fill(bg)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	tcells = np.copy(cells)

	for i in range(cell_y):
		for j in range(cell_x):
			s = 0
			for i1 in range(-1, 2):
				for j1 in range(-1, 2):
					if 0 <= i + i1 < cell_y and  0 <= j + j1 < cell_x: 
						s += int(tcells[i + i1][j + j1])
			if not tcells[i][j] and s == 3:
				cells[i][j] = True
			elif tcells[i][j] and (s == 2 or s == 3):
				pass
			else:
				cells[i][j] = False
	
	for i in range(cell_y):
		for j in range(cell_x):
			if cells[i][j]:
				pygame.draw.rect(screen,cell_clr, pygame.Rect(j * cell_a, i * cell_a, cell_a, cell_a))
	pygame.display.flip()