# Test module for bank.py

from bank import value

def main():
    test_hello()
    test_h()
    test_other()

# Function to test for word: hello
def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0


# function to test for letter h
def test_h():
    assert value("Hey") == 20
    assert value("Ho ho ho") == 20
    assert value("Hui") == 20


# function to test for other
def test_other():
    assert value("Sup") == 100
    assert value("Aloha") == 100
    assert value("Yo") == 100


if __name__ == "__main__":
    main()