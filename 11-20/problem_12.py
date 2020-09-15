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

    def nextTriangle(self):
        return

    def largestFactors(self, number):
        return

    def numberOfFactors(self, value):
        factors = 3

        for n in range(2, int(value/2)):
            if self.isFactor(value, n):
                factors += 1

        return factors

    def isFactor(self, number, factor):
        if 0 == number % factor:
            return True
        else:
            return False

print(TriangularDivisors(500).firstTriangle())