import os
import string
from typing import Dict, Iterable, List, Tuple

import pyautogui as pg
import pyscreeze

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def find_finished_image() -> List[pyscreeze.Box]:
    dir_path = os.path.join(CURRENT_DIR, 'finished_pictures')
    finished_pictures = os.listdir(dir_path)
    for finished_picture in finished_pictures:
        images = list(pg.locateAllOnScreen(
            os.path.join(dir_path, finished_picture), grayscale=True, confidence=0.65))
        if images:
            print(images[0])
            return images[0]


def click_finished_image(image: pyscreeze.Box):
    px, py = pg.center(image)
    pg.click(px, py)
