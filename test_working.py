# Test module to check if functions are working for time conversion

from working import convert


def main():
    test_convert()
    test_syntax()


def test_convert():
    # Check for off-by-one error in hours
    assert convert("12:30 AM to 1:30 AM") == "00:30 to 01:30"
    # Check for minutes off by 5
    assert convert("1:00 PM to 6:10 PM") == "13:00 to 18:10"
    # Check for out of range in minutes
    try:
        convert("8:60 AM to 4:60 PM")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError was not raised")


def test_syntax():
    # Check for omitting 'to'
    try:
        convert("4:20 PM - 6:30 PM")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError was not raised")