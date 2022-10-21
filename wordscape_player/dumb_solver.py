from itertools import permutations

import pyautogui as pg
from typing import List, Tuple

LEFT_CHAR_POS = (360, 820)
TOP_CHAR_POS = (480, 695)
RIGHT_CHAR_POS = (605, 814)
BOTTOM_CHAR_POS = (483, 945)


def _gen_permutation(n: int):
    return permutations(
        [LEFT_CHAR_POS, RIGHT_CHAR_POS, TOP_CHAR_POS, BOTTOM_CHAR_POS], n)


def _move_through_permutation(permutation: List[Tuple[str]]):
    for i, pos in enumerate(permutation):
        duration = 0.01  # if i == 0 else 0.0
        pg.moveTo(x=pos[0], y=pos[1], duration=duration)
        if i == 0:
            pg.mouseDown()
    pg.mouseUp()


def four_char_permute_solver():
    for permutation in _gen_permutation(3):
        _move_through_permutation(permutation)
    for permutation in _gen_permutation(4):
        _move_through_permutation(permutation)
