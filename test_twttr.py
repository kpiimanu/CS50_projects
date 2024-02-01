# Test module for twttr.py

from twttr import shorten

def main():
    test_letters()
    test_numbers()
    test_punctuation()

# Function to test letters
def test_letters():
    assert shorten("twitter") == "twttr"
    assert shorten("Aloha") == "lh"

# Function to test numbers
def test_numbers():
    assert shorten("2023") == "2023"

# Function to test punctuation
def test_punctuation():
    assert shorten("???!!!...") == "???!!!..."

if __name__ == "__main__":
    main()