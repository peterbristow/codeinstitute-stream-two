from random import choice, randrange
from string import ascii_uppercase  # choice(ascii_uppercase)
import logging

import time

logging.basicConfig(level=logging.INFO)


def timeit(method):
    def timed(*args, **kw):
        """time the get_words function"""
        t1 = time.time()
        result = method(*args, **kw)
        print '%r %2.2f sec' % (method.__name__, time.time() - t1)
        return result

    return timed


# def get_grid():
#     # dictionary comprehension
#     # return {(x, y): choice(ascii_uppercase) for x in range(X) for y in range(Y)}
#
#     # use actual boggle dice letters
#     dice = ['CSOAHP', 'ABBOJO', 'ENSIUE', 'FSKFAP','EGAENE', 'YIDSTT', 'ATTOWO', 'TOESIS', 'RHTVWE', 'HLNNRZ', 'MTIOUC', 'NEEHGW', 'DIXRLE', 'YLDERV', 'QHMUNI', 'RETTYL']
#     g = {}
#     count = 0
#     for y in range(Y):
#         for x in range(X):
#             num = randrange(1,7)
#             start = 0
#             if num > 0:
#                 start = num - 1
#             letter = dice[count][start:num]
#             if letter == 'Q':
#                 letter = 'QU'
#             g[(x, y)] = letter
#             count += 1
#     return g

def get_grid():
    letters = raw_input('Enter 16 letter to start the game: ')
    letters = letters.replace(" ", "").upper()
    g = {}
    count = 0
    for y in range(Y):
        for x in range(X):
            g[(x, y)] = letters[count]
            count += 1
    return g


def get_neighbours():
    neighbours = {}

    for position in grid:
        x, y = position
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                     (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        # list comprehension
        neighbours[position] = [p for p in positions if 0 <= p[0] < X and 0 <= p[1] < Y]
    return neighbours


def path_to_word(path):
    """Convert a list of grid positions to a word"""
    return ''.join([grid[p] for p in path])


def search(path):
    """Recursively search the grid for words"""
    word = path_to_word(path)
    logging.debug('%s: %s' % (path, word))
    if word not in stems:
        return
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])
        else:
            logging.debug('%s: skipping %s because in path' % (path, grid[next_pos]))


@timeit
def get_dictionary():
    """Return a list of uppercase english words, including word stems"""
    stems, dictionary = set(), set()

    with open('words.txt') as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)  # set of words: dictionary

            # set of unique stems for each word in the dictionary
            for i in range(len(word)):
                stems.add(word[:i + 1])
    return dictionary, stems


@timeit
def get_words():
    """Search each grid position and return all the words found"""
    for position in grid:
        logging.info('searching %s' % str(position))
        search([position])
    return [path_to_word(p) for p in paths]


def print_grid(grid):
    """Print the grid as a readable string"""
    s = ''
    for y in range(Y):
        for x in range(X):
            s += grid[x, y] + ' '
        s += '\n'
    print s


size = X, Y = 4, 4
grid = get_grid()
print_grid(grid)

neighbours = get_neighbours()
# dictionary = get_dictionary()
dictionary, stems = get_dictionary()
paths = []

words = get_words()
print words
