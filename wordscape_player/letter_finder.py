import os
import string
from typing import Dict, List, Tuple

import pyautogui as pg
import pyscreeze

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def find_letter(letter: str) -> List[pyscreeze.Box]:
    locations = []
    letter_dir = os.path.join(CURRENT_DIR, 'letter_pictures')
    for letter_png in os.listdir(letter_dir):
        if not letter_png.startswith(letter):
            continue
        confidence = 0.90 if letter in ('c', 'e', 'f', 'g', 'o', 'q') else 0.85
        locations.extend(list(pg.locateAllOnScreen(os.path.join(
            letter_dir, letter_png), grayscale=True, confidence=confidence)))
    return locations


def _filter_overlapping_boxes(boxes: List[pyscreeze.Box]):
    """
    This is required because lower confidences generate lots of duplicates
    """
    filtered_boxes: List[pyscreeze.Box] = []
    for box in boxes:
        should_add = True
        current_left = box.left
        current_top = box.top
        for filtered_box in filtered_boxes:
            left = filtered_box.left
            top = filtered_box.top
            width_half = filtered_box.width // 4
            height_half = filtered_box.height // 4
            width_range = range(left - width_half, left + width_half)
            height_range = range(top - height_half, + top + height_half)
            if current_left in width_range and current_top in height_range:
                should_add = False
                break
        if should_add:
            filtered_boxes.append(box)
    return filtered_boxes


def _determine_letter_point(letter: str) -> Tuple[str, List[pyscreeze.Point]]:
    possible_letters = find_letter(letter)
    points = []
    filtered_overlapping_boxes = _filter_overlapping_boxes(
        possible_letters)
    if filtered_overlapping_boxes:
        points = [pg.center(box) for box in filtered_overlapping_boxes]
    return letter, points


def determine_letter_points() -> Dict[str, List[pyscreeze.Point]]:
    letter_boxes = {}
    for letter in string.ascii_lowercase[:26]:
        _, points = _determine_letter_point(letter)
        if points:
            letter_boxes[letter] = points
    return letter_boxes


def letter_points_to_word(letter_boxes: Dict[str, List[pyscreeze.Point]]) -> str:
    word_letters = []
    for letter, points in letter_boxes.items():
        for _ in range(len(points)):
            word_letters.append(letter)
    return ''.join(word_letters)
