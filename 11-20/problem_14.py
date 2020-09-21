class CollatzSequence:
    """
    Some may say that there is a lot of
    bloat here for what it does but
    I think any abstractions
    would compromise the
    readability.

    I prefer to containerise any computations
    including getting the next item in the
    collatz sequence, finding whether
    the next item is valid for the
    next iteration and returning
    the final value.

    I feel optimisations could be made here
    as the computation time is around the
    30s mark.
    """
    def __init__(self):
        self.longest_chain = 0
        self.largest_start = 0

    def findChain(self, start, limit):
        for n in range(start, limit + 1):
            chain_items = 1
            chain_modifier = n
            """Originally tried to modify the loop parameter but needed to retain it for returning the 'best' starting value."""

            while 1 < chain_modifier:
                chain_modifier = self.nextChainItem(chain_modifier)
                chain_items += 1

            self.maybeLongestChain(chain_items, n)

        print(self.longestChain())

    def nextChainItem(self, value):
        if 0 == value % 2:
            return value // 2
        else:
            return (3 * value) + 1

    def maybeLongestChain(self, chain, sequence_start):
        """
        In the past, I've used the 'maybe' keyword
        to depict validation checks on whether
        a particular value or variable
        should be updated or not.

        While I feel it works well in the PHP and
        web development landscape with enterprise
        software and business logic, I'm not
        sure it fits here and is inherently
        Pythonic.
        """
        if self.longest_chain < chain:
            self.longest_chain = chain
            self.largest_start = sequence_start

    def longestChain(self):
        """
        I've always liked to use functions to field
        returning of variables but is it really
        necessary going forward and does it
        add anything to the logic?
        """
        return self.largest_start

CollatzSequence().findChain(14, 1000000)