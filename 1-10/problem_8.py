import os

class LargestProduct:
    def __init__(self, directory):
        self.largest_product = 0
        self.pointer_start = 0
        self.pointer_end = 12

        digits = self.loadFile(directory)

    def loadFile(self, directory):
        digits = ''

        with open(os.getcwd() + directory + 'problem_8.txt', 'r') as file:
            for line in file:
                while self.pointer_end <= len(line):
                    self.readNextGroup(line)

                    self.pointer_start += 1
                    self.pointer_end += 1

                self.resetPointers()

        return digits

    def readNextGroup(self, series):
        group = list(series[self.pointer_start:self.pointer_end])
        product = 1

        if '\n' not in group:
            for item in group:
                product *= int(item)

            if self.largest_product < product:
                self.largest_product = product

    def resetPointers(self):
        self.pointer_start = 0
        self.pointer_end = 12

    def getProduct(self):
        return self.largest_product

print(LargestProduct('/1-10/').getProduct())