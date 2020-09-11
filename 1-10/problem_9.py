class PythagoreanTriplet:
    """
    Initially tried to brute force the
    problem extremely crudely with
    no results, due to a huge
    computation time.

    Attempted to clean things up by making
    assumptions such as the value of c
    and making validation checks if
    the values of b or c are not
    compatible.

    After some reading, Euclid's formula could
    be applied here to generate triples
    rather than iterating through
    manually. Info here:

    https://en.wikipedia.org/wiki/Pythagorean_triple
    """
    def __init__(self, goal_sum):
        self.goal_sum = goal_sum

        print(self.findTriplet())

    def findTriplet(self):
        """
        Preferred to work backwards through the
        sequence as I feel that made more
        sense than starting from [2,1,0].

        Could replace the while loop(s) with for
        loops instead to avoid using manual
        iterators but I think this reads
        better and makes more sense when 
        trying to get the problem down 
        in code.
        """
        a = 997
        b = 996

        while 4 < a:
            """Smallest triplet is [3,4,5]."""
            while 3 < b:
                c = self.goal_sum - a - b

                if b > c and 0 < c:
                    if self.isTriplet([a, b, c]):
                        return a * b * c
                b -= 1
            a -= 1
            b = a - 1

    def isTriplet(self, natural_numbers = []):
        if (natural_numbers[0] ** 2) == ((natural_numbers[1] ** 2) + natural_numbers[2] ** 2):
            return True

PythagoreanTriplet(1000)