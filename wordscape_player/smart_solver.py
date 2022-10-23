from collections import defaultdict
from typing import Dict, List

import pyscreeze
import pyautogui as pg


def guess_to_movement(guess: str, letter_points: Dict[str, List[pyscreeze.Point]]) -> None:
    letter_indices = defaultdict(lambda: 0)
    for i, letter in enumerate(guess):
        duration = 0.001
        point_index = letter_indices[letter]
        pos = letter_points[letter][point_index]
        letter_indices[letter] += 1
        pg.moveTo(x=pos[0], y=pos[1], duration=duration)
        if i == 0:
            pg.mouseDown()
    pg.mouseUp()
