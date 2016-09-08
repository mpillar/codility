import unittest

"""
Task 2 I don't fully remember this one, because I basically decided after the first sentence that
I'll leave this for last (and then never got to it). It was something along the lines of "In a
numeral system with Base -2, do some bit manipulation to find an integer that has a certain value"
or whatever. I kinda stopped reading after the first half of that sentence :)

For the purpose of practicing for the test here what I will do is create a function that converts
a number from one arbitrary base to another.
"""


class Test(unittest.TestCase):
    ten_to_negative_test_cases = [
        # n, r1, r2, expected_result
        ["0", 9, -11, "0"],
        ["A", 11, 10, "11"],
        ["F", 16, 10, "16"],
        ["146", 10, -3, "21102"],
        ["1234", 10, -8, "16462"],
        ["2369", 10, -10, "18449"],
    ]

    def test_ten_to_negative(self):
        for n, r1, r2, expected_result in Test.ten_to_negative_test_cases:
            actual_result = from_base_r1_to_base_r2(n, r1, r2)
            self.assertEquals(actual_result, expected_result)


def _from_base_r_to_base_10(n, r):
    if abs(r) > 16:
        raise Exception("Unsupported absolute base greater than 16")
    if not isinstance(n, str):
        raise Exception("Expected n to be a string")
    n = n.lower()
    result = 0
    for i in xrange(len(n)):
        if n[i].isdigit():
            value = int(n[i])
        else:
            value = {
                'a': 11,
                'b': 12,
                'c': 13,
                'd': 14,
                'e': 15,
                'f': 16,
            }[n[i]]
        result += value * pow(r, len(n)-1-i)
    return result


def from_base_r1_to_base_r2(n, r1, r2):
    """
    Convert n, an integer in base 10, to base -r, and return a string representation of the number.
    """
    if abs(r1) > 16 or abs(r2) > 16:
        raise Exception("Unsupported absolute base greater than 16")
    # Base r1 to base 10.
    if r1 == 10:
        n = int(n)
    else:
        n = _from_base_r_to_base_10(n, r1)
    # Base 10 to base r2.
    digits = []
    while True:
        n, remainder = divmod(n, r2)
        if remainder < 0:
            n, remainder = n + 1, remainder - r2
        digits.append(str(remainder))
        if n == 0:
            break
    digits.reverse()
    return "".join(digits)


if __name__ == '__main__':
    unittest.main()

