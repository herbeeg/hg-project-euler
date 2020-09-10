import os

class LargestProduct:
    """
    Tried to separate out the file loader
    and parsing logic for readability.
    
    I decided to read each line of the input
    file individually as that is how the
    problem was displayed on the
    Project Euler site.

    You could move that into a local variable 
    but while this creates more code and
    work for the program, it fits the
    problem and reads better.
    """
    def __init__(self, directory):
        self.largest_product = 0
        self.pointer_start = 0
        self.pointer_end = 13
        """Some initial confusion over the scan indexes caused a lot of time loss."""

        digits = self.loadFile(directory)

        while self.pointer_end < len(digits):
            self.readNextGroup(digits)

            self.pointer_start += 1
            self.pointer_end += 1

    def loadFile(self, directory):
        """
        Some difficulty understanding the requirements
        for this one:
        
        1. Whether each row needs to be scanned as it's
        own container group.

        2. What to do with the newline characters.
        """
        digits = ''

        with open(os.getcwd() + directory, 'r') as file:
            for line in file:
                digits += line.rstrip()

        return digits

    def readNextGroup(self, series):
        group = list(series[self.pointer_start:self.pointer_end])
        """A nice way of being able to reference string 'pointers'."""
        product = 1

        if '0' not in group:
            """We can skip any groups that contain a zero as the product will always be zero."""
            for item in group:
                product *= int(item)

            if self.largest_product < product:
                self.largest_product = product

    def getProduct(self):
        return self.largest_product

print(LargestProduct('/1-10/problem_8.txt').getProduct())
"""Having to reference the file here could be an unnecessary parameter."""