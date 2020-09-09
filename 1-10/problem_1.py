class Multiples:
    """
    A better way to calculate the multiples would be
    to use a for loop using the range() function
    as it does not require a while loop plus
    an iterator.
    """
    def __init__(self, limit):
        self.limit = limit
        self.sum = 0
    
    def calculateMultiples(self):
        i = 3

        while self.limit > i:
            if 0 == i % 3 or 0 == i % 5:
                self.sum += i
            i += 1

        return self.sum

print(Multiples(1000).calculateMultiples())