import random


class WordFinder:
    """Machine for finding random words from a dictionary."""

    def __init__(self, path):
        """Read the dictionary file and report the number of words read."""
        with open(path) as dict_file:
            self.words = [word.strip() for word in dict_file]
        print(f"{len(self.words)} words read")

    def random(self):
        """Return a random word from the dictionary."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments."""

    def parse(self, dict_file):
        """Parse the dictionary file, skipping blanks and comments."""
        return [
            word.strip()
            for word in dict_file
            if word.strip() and not word.startswith("#")
        ]
