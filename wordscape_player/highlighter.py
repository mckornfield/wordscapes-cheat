import os
from typing import Callable

import pyautogui as pg

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# 112, 191, back image ref
# 400, 692, top
# 500, 780, right
# 472, 920, bottom right
# 326, 920, bottom left
# 280, 780, left


def highlight_letters() -> Callable:
    # Caller must call returned lambda to reset
    back_arrow_png = os.path.join(
        CURRENT_DIR, 'reference_pictures', 'back_arrow.png')
    arrow_box = pg.locateOnScreen(back_arrow_png,
                                  grayscale=True, confidence=0.70)
    if not arrow_box:
        raise Exception("No arrow present on the screen")
    left_reference = arrow_box.left
    top_reference = arrow_box.top
    positions = [(300, 500), (400, 600), (400, 700), (200, 700), (200, 600)]
    for i, position in enumerate(positions):
        x = position[0] + left_reference
        y = position[1] + top_reference
        pg.moveTo(x, y, duration=0.1)
        if i == 0:
            pg.mouseDown()
    return lambda: pg.mouseUp()
