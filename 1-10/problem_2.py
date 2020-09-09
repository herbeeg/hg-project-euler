class Fibonacci:
    """
    There might be a better way to handle the pointer
    but I think storing the sequence in a list and
    then iterating over it afterward to produce
    the desired result reads rather well.
    """
    def __init__(self, limit):
        self.limit = limit
        self.sequence = [1,2]
        self.pointer = 1

    def evenFibonacci(self):
        while self.limit >= self.sequence[self.pointer]:
            self.sequence.append(self.sequence[self.pointer] + self.sequence[self.pointer - 1])

            self.pointer += 1

        return sum([x for x in self.sequence if 0 == x % 2])

print(Fibonacci(4000000).evenFibonacci())