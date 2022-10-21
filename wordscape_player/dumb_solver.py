from itertools import permutations

import pyautogui as pg
from typing import List, Tuple
from pyscreeze import Point

LEFT_CHAR_POS = Point(360, 820)
TOP_CHAR_POS = Point(480, 695)
RIGHT_CHAR_POS = Point(605, 814)
BOTTOM_CHAR_POS = Point(483, 945)


def _gen_permutation(n: int):
    return _gen_permutation_for_list(
        [LEFT_CHAR_POS, RIGHT_CHAR_POS, TOP_CHAR_POS, BOTTOM_CHAR_POS], n)


def _gen_permutation_for_list(positions: List[Point[int]], n: int):
    return permutations(positions, n)


def _move_through_permutation(permutation: List[Tuple[str]]):
    for i, pos in enumerate(permutation):
        duration = 0.001
        pg.moveTo(x=pos[0], y=pos[1], duration=duration)
        if i == 0:
            pg.mouseDown()
    pg.mouseUp()


def position_based_permute_solver(positions: List[Point[int]]):
    for i in range(3, len(positions)+1):
        for permutation in _gen_permutation_for_list(positions, i):
            _move_through_permutation(permutation)


def four_char_permute_solver():
    for permutation in _gen_permutation(3):
        _move_through_permutation(permutation)
    for permutation in _gen_permutation(4):
        _move_through_permutation(permutation)
