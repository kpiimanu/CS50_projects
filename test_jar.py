from jar import Jar


def test_init():
    cookie_jar = Jar()
    assert cookie_jar.capacity == 12
    cookie_jar2 = Jar(7)
    assert cookie_jar2.capacity == 7


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    cookie_jar = Jar()
    cookie_jar.deposit(2)
    assert cookie_jar.size == 2
    cookie_jar.deposit(5)
    assert cookie_jar.size == 7


def test_withdraw():
    cookie_jar = Jar()
    cookie_jar.deposit(2)
    cookie_jar.withdraw(1)
    assert cookie_jar.size == 1
    cookie_jar.withdraw(1)
    assert cookie_jar.size == 0