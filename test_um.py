# Test module for um.py

from um import count


def main():
    test_case()
    test_in_word()
    test_count()


# Check for case sensitivity of um
def test_case():
    assert count("Um, hi?") == 1
    assert count("um, are you sure? um...") == 2


# Check that um in a word isnt counted
def test_in_word():
    assert count("Yummy!") == 0


# Check correct count
def test_count():
    assert count("Um, hey...um, can we talk? um...") == 3