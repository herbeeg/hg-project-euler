class TriangularDivisors:
    def __init__(self, limit):
        self.limit = limit
    
    def firstTriangle(self):
        value = 28
        index = 7

        while self.limit > self.numberOfFactors(value):
            index += 1
            value = int((((index ** 2) + index) / 2))

        print(value)

    def nextTriangle(self):
        return

    def largestFactors(self, number):
        return

    def numberOfFactors(self, value):
        factors = 2

        for n in range(2, int(value/2)):
            if self.isFactor(value, n):
                factors += 1

        return factors

    def isFactor(self, number, factor):
        if 0 == number % factor:
            return True
        else:
            return False

TriangularDivisors(200).firstTriangle()