from functools import reduce

class TriangularDivisors:
    def __init__(self, limit):
        self.limit = limit
    
    def firstTriangle(self):
        value = 28
        index = 7

        while True:
            if self.limit > self.numberOfFactors(value):
                index += 1
                value = int((((index ** 2) + index) / 2))
            else:
                return value

    def numberOfFactors(self, value):
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