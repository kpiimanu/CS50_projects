# Testting validate function from numb3rs file

from numb3rs import validate


def main():
    test_validate()


def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("255.3.255.400") == False
    assert validate("apple.5.4.3") == False
    assert validate("$.7.5.3") == False