from PIL import Image
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def main():
    dir_path = os.path.join(
        CURRENT_DIR, '..', 'wordscape_player', 'letter_pictures')
    for image in os.listdir(dir_path):
        img = Image.open(os.path.join(dir_path, image)).convert('L')
        img.save(os.path.join(dir_path, image))


if __name__ == '__main__':
    main()
