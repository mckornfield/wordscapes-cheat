import os

from . import (anagram_solver, highlighter, letter_finder, level_finder,
               smart_solver)

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
if __name__ == "__main__":
    while True:
        # print(anagram_solver.get_guesses("abasdkjc"))
        image = level_finder.find_finished_image()
        if image:
            level_finder.click_finished_image(image)
        end_highlight = highlighter.highlight_letters()
        letter_points = letter_finder.determine_letter_points()
        end_highlight()
        print(letter_points)
        anagram_input = letter_finder.letter_points_to_word(letter_points)
        guesses = anagram_solver.get_guesses(anagram_input)
        for guess in guesses:
            print(guess)
            smart_solver.guess_to_movement(guess, letter_points)
        # dumb_solver.position_based_permute_solver(center_positions)
