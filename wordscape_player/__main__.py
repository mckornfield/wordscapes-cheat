from . import dumb_solver, letter_finder, highlighter, level_finder

left_char = (360, 820)
top_char = (480, 695)
right_char = (605, 814)
if __name__ == "__main__":
    while True:

        image = level_finder.find_finished_image()
        if image:
            level_finder.click_finished_image(image)
        end_highlight = highlighter.highlight_letters()
        letter_boxes = letter_finder.determine_letter_boxes()
        print(letter_boxes)
        end_highlight()
        center_positions = letter_finder.get_box_centers(letter_boxes.values())
        dumb_solver.position_based_permute_solver(center_positions)
