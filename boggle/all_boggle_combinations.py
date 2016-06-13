"""
Write a program that instead of solving Boggle, goes through each word in the dictionary and sees which words can actually
 be made using the official boggle cubes. What’s the longest word in the dictionary that can be made?
"""

import logging

logging.basicConfig(level=logging.INFO)


def get_dictionary():
    """Return a list of words in the dictionary"""
    dictionary = []
    with open('words.txt') as f:
        for word in f:
            word = word.strip().upper()
            dictionary.append(word)
    return dictionary


def get_dice():
    # return ['CSOAHP', 'ABBOJO', 'ENSIUE', 'FSKFAP','EGAENE', 'YIDSTT', 'ATTOWO', 'TOESIS', 'RHTVWE', 'HLNNRZ', 'MTIOUC', 'NEEHGW', 'DIXRLE', 'YLDERV', 'QHMUNI', 'RETTYL']
    return ['CSOAHP', 'ABBOJO', 'ENSIUE']

"""
iterate over words in dictionary
for each word:
    choose the first position on the first block that has the letter in the first position of the word
    choose the first position on the first block that has the letter in the second position of the word
    ....
    if we end up with the word, great! success!
    if we don't end up with the word, back up one level, try to find another position on the same block
    otherwise, try the next block in the list until there are no more positions on blocks

    and so on and so forth


    inside the checking function:
    if out of letters, i.e. word is found:
        return success
    if letter found:
        call again for next position  # have to look at this return value to decide what to do next
    if letter not found:
        return failure
"""


def search(count, letters):
    for d in dice[count]:
        letters += d
        item = len(dice) - 1
        if count < item:
            search(count + 1, letters)
        else:
            if len(letters) == len(dice):
                words.append(letters)
                return


def get_combos():
    count = 0
    letters = ''
    search(count, letters)
    return words


words = []
dice = get_dice()
print get_combos()
