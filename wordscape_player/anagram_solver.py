from collections import Counter
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def is_match(word: str, guess_set: set, guess_counter: Counter):
    return set(word).issubset(guess_set) and not Counter(word) - guess_counter


def get_guesses(letters: str) -> set[str]:
    guess_letters = set(letters)
    guess_counter = Counter(letters)
    answers = []
    dictionary_file = os.path.join(CURRENT_DIR, 'dictionary', 'dictionary.txt')
    with open(dictionary_file, encoding='utf-8') as f:
        for line in f.read().splitlines():
            if is_match(line, guess_letters, guess_counter):
                answers.append(line)
    return answers
