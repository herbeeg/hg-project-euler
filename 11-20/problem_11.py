import os

class LargestGridProduct:
    def __init__(self, directory):
        self.largest_product = 0
        self.digits = self.loadFile(directory)

        self.readHorizontal()

    def loadFile(self, directory):
        numbers = []

        with open(os.getcwd() + directory, 'r') as file:
            for line in file:
                numbers.append(line.split())

        return numbers

    def readHorizontal(self):
        for row in self.digits:
            index = 0

            while len(row) > (index+3):
                product = 1
                
                for item in row[index:index+4]:
                    product *= int(item)

                if self.largest_product < product:
                    self.largest_product = product

                index += 1

    def readVertical(self):
        return

    def getProduct(self):
        return self.largest_product


print(LargestGridProduct('/11-20/problem_11.txt').getProduct())