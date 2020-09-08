class LargestPrimeFactor:
    """
    A very crude way of calculating prime
    numbers. While checking factors is 
    a single operation, I feel there 
    is a simpler more 'mathematical' 
    way of doing this.

    Execution time increases exponentially
    as the passed number increases in
    size.
    """
    def __init__(self, number):
        self.number = number
        self.largest = 0

    def isPrime(self, value):
        for n in range(2, value-1):
            if 0 == value % n:
                return False

        return True

    def isFactor(self, value):
        if 0 == self.number % value:
            return True
        else:
            return False

    def largestPrime(self):
        """
        Attempted to reduce execution time by halving 
        the number to check prime factors for as we 
        can assume we will find no factors larger 
        than itself/2.

        The number needs to be cast as an integer
        as division returns a float but the
        range function only accepts
        integer values.
        """
        for n in range(3, int(self.number/2)):
            if 0 != n % 2:
                if self.isFactor(n):
                    if self.isPrime(n):
                        self.largest = n

        return self.largest

print(LargestPrimeFactor(600851475143).largestPrime())