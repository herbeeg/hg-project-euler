import os

class LargeSum:
    """
    A rather simple solution in comparison to
    previous problems but I get the feeling
    that with particular integer length
    constraints, this would be far
    more difficult.

    I did think about how you could work out
    the first set of digits of a sum of
    values. 
    
    One possibilty could surround taking sums 
    of the numbers at the start and adding
    tenths and working your way backwards
    but I'm not sure how this could be
    achieved.

    It's possible there is a calculation you
    could make mathematically to give you
    a set of assumptions to base those
    calculations on but I'm unaware
    at this stage.
    """
    def __init__(self, directory):
        self.numbers = self.loadFile(directory)

    def loadFile(self, directory):
        numbers = []

        with open(os.getcwd() + directory, 'r') as file:
            for line in file:
                numbers.append(line)

        return numbers

    def getDigits(self):
        value = 0

        for row in self.numbers:
            value += int(row)

        return str(value)[:10]

print(LargeSum('/11-20/problem_13.txt').getDigits())