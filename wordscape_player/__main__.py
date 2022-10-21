import sys
from time import sleep

import pyautogui as pg

from . import (anagram_solver, dumb_solver, highlighter, letter_finder,
               level_finder, smart_solver)

if __name__ == "__main__":
    while True:
        try:
            image = level_finder.find_finished_image()
            if image:
                level_finder.click_finished_image(image)
            end_highlight = highlighter.highlight_letters()
            letter_points = letter_finder.determine_letter_points()
            end_highlight()
            print(letter_points)
            points = [point for points in letter_points.values()
                      for point in points]
            # dumb_solver.position_based_permute_solver(points)
            anagram_input = letter_finder.letter_points_to_word(letter_points)
            guesses = anagram_solver.get_guesses(anagram_input)
            for guess in guesses:
                print(guess)
                smart_solver.guess_to_movement(guess, letter_points)
        except pg.FailSafeException as e:
            print(e)
            sys.exit(1)
        except Exception as e:
            print(e)
            print("Waiting 1 second")
            sleep(1)
        # dumb_solver.position_based_permute_solver(center_positions)
