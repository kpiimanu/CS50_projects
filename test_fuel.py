# Module to test fuel.py program

from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()


def test_convert():
    # Test for correct input
    assert convert("1/2") == 50, "Expected 50"

    # Test for invalid input: numerator > denominator
    try:
        convert("5/4")
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError"

    # Test for invalid input: denominator == 0
    try:
        convert("2/0")
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected a ZeroDivisionError"

    # Test for invalid input: non-integer value returned
    assert isinstance(convert("1/3"), int), "Expected an integer"

    # Test for invalid input: non-integer value returned
    assert isinstance(convert("2/3"), int), "Expected an integer"

    # Test for invalid input: invalid format
    try:
        convert("cat/4")
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError"


def test_gauge():
    # Test for "F" when at 100%
    assert gauge(100) == "F"
    # Test for "E" when at 1% or less
    assert gauge(1) == "E"
    # Test that any other percentage is displayed
    assert gauge(50) == "50%"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()