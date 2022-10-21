from . import dumb_solver, letter_finder

left_char = (360, 820)
top_char = (480, 695)
right_char = (605, 814)

if __name__ == "__main__":
    while True:
        letter_boxes = letter_finder.determine_letter_boxes()
        center_positions = letter_finder.get_box_centers(letter_boxes.values())
        dumb_solver.position_based_permute_solver(center_positions)
