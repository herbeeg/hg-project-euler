class SquareDifference:
    """
    While it's quite a simple solution, I
    think optimisations can be made
    surrounding the similarities
    of the for loops.

    Possibly, the sum() function could be
    used on the range() results as the
    output is an Iterable object.
    However, I feel that could
    sacrifice readability.
    """
    def __init__(self, limit):
        self.limit = limit

        print(self.squareSum() - self.sumSquares())

    def sumSquares(self):
        value_sum = 0

        for n in range(1, self.limit + 1):
            value_sum += n ** 2

        return value_sum

    def squareSum(self):
        value_sum = 0

        for n in range(1, self.limit + 1):
            value_sum += n

        return value_sum ** 2

SquareDifference(100)