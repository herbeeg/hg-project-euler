class SmallestMultiple:
    """
    Originally attempted to have a single recursive
    function that housed all of the logic but
    hit Python's recursion limits so
    decided to change the structure
    to a simpler while loop.

    I'm not 100% sure on the readability of having
    the function return call as part of the
    initial while loop statement but I
    think it works fine overall.
    """
    def __init__(self, multiple):
        self.multiple = multiple
        self.isEvenlyDivisible(self.multiple)
        
    def isEvenlyDivisible(self, number):
        while not self.validFactors(number):
            """Due to Python's recursive limit of 1000 operations, the logic was moved to a separate function."""
            number += 1
        
        print(number)

    def validFactors(self, number):
        if 0 != number % 20:
            """We can assume that the multiple must evenly divisible by the largest value."""
            return False

        for n in range(2, 20):
            """We can ignore 1 and 20 from the factors check as these have already been validated."""
            if 0 != number % n:
                return False

        return True

SmallestMultiple(20)