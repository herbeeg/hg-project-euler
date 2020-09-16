from functools import reduce

class TriangularDivisors:
    """
    Most difficult problem yet, due to the
    increasing mathematical requirements
    to solve any problems within the
    recommended 60 second limit.
    """
    def __init__(self, limit):
        self.limit = limit
    
    def firstTriangle(self):
        """
        These values are available as information
        when starting the problem, although
        it doesn't actually save that
        much computation time.

        Triangle numbers can be found by taking
        the square of the nth number, adding
        it to itself and then dividing
        by two.
        """
        value = 28
        index = 7

        while True:
            if self.limit > self.numberOfFactors(value):
                index += 1
                value = int((((index ** 2) + index) / 2))
            else:
                return value

    def numberOfFactors(self, value):
        """
        This was by far the hardest element of
        the problem for me to understand,
        even now but getting there.

        Methods of finding all factors of a number
        that I'd used previously may have been
        viable then but were not usable here.
        A crude approach had to be avoided
        to keep within a reasonable
        execution time.

        We use the proof of contradiction again to
        get the 'lower' factors but we want to
        get ALL the factors this time,
        including one and itself for
        any value.

        This time, we get pairs of factors and
        use the set() function to ensure we
        do not store any duplicate factors.

        A very good explanation here:

        https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
        """
        return len(set(
            factor for n in range(1, int(value ** .5) + 1) if self.isFactor(value, n)
            for factor in (n, value//n)
        ))

    def isFactor(self, number, factor):
        if 0 == number % factor:
            return True
        else:
            return False

print(TriangularDivisors(500).firstTriangle())