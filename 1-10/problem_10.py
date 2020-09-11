from math import sqrt

class PrimeSummation:
    """
    Was finally able to incorporate the
    "square root" method of defining
    whether a natural number is
    prime or not.

    Computation time is incredibly short
    in comparison and works very well.
    """
    def __init__(self, limit):
        self.limit = limit

    def getPrimeSum(self):
        number = 3
        prime_sum = 2

        while self.limit > number:
            if self.isPrime(number):
                prime_sum += number

            number += 2
            """Prime numbers greater than two will always be odd."""

        return prime_sum

    def isPrime(self, value):
        for n in range(2, int(sqrt(value) + 1)):
            """We need to add one to the check value as range will be value-1."""
            if 0 == value % n:
                return False

        return True

print(PrimeSummation(2000000).getPrimeSum())