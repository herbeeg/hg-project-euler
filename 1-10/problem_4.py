from math import floor

class Palindrome:
    """
    Made a conscious effort to reduce the amount
    of unnecessary computations by avoiding
    the checking of reverse products.

    For example, if 150 x 999 does not produce a
    palindrome, then we don't need to check
    whether 999 x 150 produces one either.

    By doing this. I'm not sure whether I've sacrificed
    readability as the loop parameters are not
    obvious initially which means I may
    have taken the optimisations too
    far.
    """
    def __init__(self):
        self.limit = 999
        self.first_multiplier = 100
        self.second_multiplier = self.limit
        self.largest_palindrome = 0

    def findPalindrome(self):
        while self.second_multiplier > floor(self.limit/2):
            for n in range(self.first_multiplier, self.second_multiplier):
                if self.isPalindrome(str(n * self.second_multiplier)) and self.largest_palindrome < (n * self.second_multiplier):
                    self.largest_palindrome = n * self.second_multiplier

            self.second_multiplier -= 1

        return self.largest_palindrome

    def isPalindrome(self, number_string):
        if number_string[::-1] == number_string:
            return True
        else:
            return False

print(Palindrome().findPalindrome())