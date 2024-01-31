# Test module for project.py

from project import star_check
from project import hawaiian_trans
from project import read_star_data

import pytest


def main():
    test_star_check()
    test_valid_star_name()
    test_read_star_data()


def test_star_check():
    # Test an error is raised if nothing is input
    try:
        star_check("")
    except ValueError as e:
        assert str(e) == "You must enter a star name"


def test_valid_star_name():
    # Test with a valid star name
    star_name = "Polaris"
    expected_translation = "The Hawaiian star name for 'Polaris' is called Hōkūpaʻa."
    translation = hawaiian_trans(star_name)
    assert translation == expected_translation


def test_read_star_data():
    # Call the function to read the data
    stars = read_star_data()

    # Assert that the returned dictionary is not empty
    assert stars != {}


if __name__ == "__main__":
    main()