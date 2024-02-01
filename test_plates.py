# Test module to test plates.py

from plates import is_valid


def main():
    test_max_min()
    test_first_two_alpha()
    test_num_end()
    test_not_zero()
    test_alnum_only()


# Function to test if plates have max of 6 char & min of 2 char
def test_max_min():
    assert is_valid("hayn10") == True
    assert is_valid("hawaiian10") == False


# Function to test that first 2 char isalpha
def test_first_two_alpha():
    assert is_valid("bozo20") == True
    assert is_valid("18er") == False
    assert is_valid("a113") == False
    assert is_valid("5kea11") == False


# Function to test that num is not in middle - only at end
def test_num_end():
    assert is_valid("hit69") == True
    assert is_valid("ha67ki") == False


# Function to test and see that first number is not zero
def test_not_zero():
    assert is_valid("Love18") == True
    assert is_valid("Bo06") == False


# Function to test that no punctuation, spaces or periods are included
def test_alnum_only():
    assert is_valid("no23") == True
    assert is_valid("what?2") == False


if __name__ == "__main__":
    main()