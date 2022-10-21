import os
import string
from typing import Dict, Iterable, List

import pyautogui as pg
import pyscreeze

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def find_letter(letter: str) -> List[pyscreeze.Box]:
    letter_path = os.path.join(CURRENT_DIR, 'letter_pictures', letter + '.png')
    if not os.path.exists(letter_path):
        print(f"Missing letter {letter}")
        return []
    return list(pg.locateAllOnScreen(letter_path, grayscale=True, confidence=0.85))


def _filter_overlapping_boxes(boxes: List[pyscreeze.Box]):
    """
    This is required because lower confidences generate lots of duplicates
    """
    filtered_boxes = []
    left_and_width = []
    for box in boxes:
        should_add = True
        current_left = box.left
        for left, width in left_and_width:
            if current_left in range(left - width, left + width):
                should_add = False
        if should_add:
            filtered_boxes.append(box)
            left_and_width.append((box.left, box.width))
    return filtered_boxes


def determine_letter_points() -> Dict[str, List[pyscreeze.Point]]:
    letter_boxes = {}
    for letter in string.ascii_lowercase[:26]:
        possible_letters = find_letter(letter)
        if not possible_letters:
            continue
        filtered_overlapping_boxes = _filter_overlapping_boxes(
            possible_letters)
        if filtered_overlapping_boxes:
            letter_boxes[letter] = [pg.center(box)
                                    for box in filtered_overlapping_boxes]
    return letter_boxes


def letter_points_to_word(letter_boxes: Dict[str, List[pyscreeze.Point]]) -> str:
    word_letters = []
    for letter, points in letter_boxes.items():
        for _ in range(len(points)):
            word_letters.append(letter)
    return ''.join(word_letters)
