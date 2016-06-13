import random
import sys

import pygame

from colours import dark_blue, green, black


def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))


def draw_cells():
    for (x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)


def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]


# def evolve():
#     for position, alive in cells.items():
#         live_neighbours = sum(get_neighbours(position))
#         if alive:
#             if live_neighbours < 2 or live_neighbours > 3:
#                 cells[position] = False
#         elif live_neighbours == 3:
#             cells[position] = True


def evolve():
    next_gen = {}
    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2 or live_neighbours > 3:
                next_gen[position] = False
        elif live_neighbours == 3:
            next_gen[position] = True
    for position, alive in next_gen.items():
        cells[position] = alive
    #cells = next_gen.deepcopy(cells)
    # cells.deepcopy(next_gen)


# def get_cells(density=0.2):
#     return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}


def get_cells():
    cells = {(c, r): False for c in range(columns) for r in range(rows)}
    cells[3,4]=True
    cells[4,5]=True
    cells[5,3]=True
    cells[5,4]=True
    cells[5,5]=True
    return cells


pygame.init()

columns, rows = 50, 50
cells = get_cells()

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_cells()
    evolve()
    draw_grid()
    pygame.display.update()