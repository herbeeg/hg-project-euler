class SpecificPrimeNumber:
    """
    While being unable to apply a solution
    using the proof of contradiction
    method to find prime numbers,
    the computation time was
    not that bad here.
    """
    def __init__(self, position):
        self.position = position

    def getPrime(self):
        """
        There is probably a better way of
        handling the final prime
        number output.
        """
        count = 0
        number = 2

        while self.position > count:
            if self.isPrime(number):
                count += 1
            
            if count != self.position:
                """Required for the last pass to avoid final increment before printing."""
                number += 1

        return number

    def isPrime(self, value):
        for n in range(2, value):
            if 0 == value % n:
                return False

        return True

print(SpecificPrimeNumber(10001).getPrime())