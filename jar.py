# Program to implement a cookie jar to store cookies


class Jar:
    def __init__(self, capacity=12):
        # Check if user is inputting a value less than zero
        if capacity < 0:
            raise ValueError("Wrong capacity input")
        # Max amount of cookies to fit in jar
        self._capacity = capacity
        # Size refers to the amount of cookies actually in jar
        self._size = 0

    def __str__(self):
        # Number of cookies in jar = cookie emojis returned
        return self.size * "🍪"

    def deposit(self, n):
        # Checking if the number of cookies being deposited exceeds the jar capacity
        if n > self.capacity:
            raise ValueError("Exceeds cookie capacity")
        # Checking to see if the sum of whats being added and what was already in jar exceeds capacity
        if self.size + n > self.capacity:
            raise ValueError("Exceeds cookie capacity")
        # Otherwise, update value of current amt of cookies according to n
        self._size += n

    def withdraw(self, n):
        # Check to see if whats being withdrawn exceeds what is currently in jar
        if self.size < n:
            raise ValueError("Insufficient cookies to withdraw")
        # Otherwise, remove n cookies from jar
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size