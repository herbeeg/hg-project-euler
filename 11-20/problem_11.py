import os

class LargestGridProduct:
    """
    Decided to scan the 20x20 grid by reading
    the horizontal, vertical and diagonal
    subsets separately as I felt it
    was better for understanding
    what is going on.

    Kept the grid of numbers in a separate
    file in a similar vein to that of
    problem 8, as I felt it was
    unnecessary to put that
    in a variable.

    Yes, you could probably combine all of the
    looping elements in one function and
    prevent re-scanning of the grid
    I think you would sacrifice
    too much readability for
    a small gain.
    """
    def __init__(self, directory):
        self.largest_product = 0
        self.digits = self.loadFile(directory)

        self.readHorizontal()
        self.readVertical()
        self.readDiagonal()

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
                self.checkProduct(row[index:index+4])

                index += 1

    def readVertical(self):
        v_index = 0
        h_index = 0

        while 20 > h_index:
            while 20 > (v_index+3):
                subset = [
                    self.digits[v_index][h_index],
                    self.digits[v_index+1][h_index],
                    self.digits[v_index+2][h_index],
                    self.digits[v_index+3][h_index]
                ]

                self.checkProduct(subset)

                v_index += 1
            h_index += 1
            v_index = 0

    def readDiagonal(self):
        """
        A rethink of the variable naming
        convention could be beneficial
        here to promote understanding
        of the problem. I think it
        obfuscates some elements
        of the grid scanning.
        """
        v_index = 0
        h_index = 0

        while 20 > (v_index+3):
            """Left-to-right diagonal scanning."""
            while 20 > (h_index+3):
                subset = [
                    self.digits[v_index][h_index],
                    self.digits[v_index+1][h_index+1],
                    self.digits[v_index+2][h_index+2],
                    self.digits[v_index+3][h_index+3]
                ]

                self.checkProduct(subset)
            
                h_index += 1
            v_index += 1
            h_index = 0

        v_index = 0
        h_index = 19

        while 0 <= (h_index-3):
            """Right-to-left diagonal scanning."""
            while 20 > (v_index+3):
                subset = [
                    self.digits[v_index][h_index],
                    self.digits[v_index+1][h_index-1],
                    self.digits[v_index+2][h_index-2],
                    self.digits[v_index+3][h_index-3]
                ]

                self.checkProduct(subset)
            
                v_index += 1
            h_index -= 1
            v_index = 0

    def checkProduct(self, subset):
        """
        Avoided code duplication by creating
        separate function when checking
        the product of grid subsets.
        """
        product = 1

        for item in subset:
            product *= int(item)

        if self.largest_product < product:
            self.largest_product = product

    def getProduct(self):
        return self.largest_product


print(LargestGridProduct('/11-20/problem_11.txt').getProduct())