import unittest

"""
Your function takes an array of integers (arr), and an integer (x). You need to find the position in
arr that splits the array in two, where one side has as many occurrences of x as the other side has
occurrences of any number but x (there was some additional info about edge cases, but that's the
gist of it). So, given an array like this: [5, 5, 2, 3, 5, 1, 6] and x being "5", the function
should return "4" (Position 4, holding the number "3" above is the point where you have 2 5's on
the one side, and two "not fives" on the other.
"""


class Test(unittest.TestCase):
    test_cases = [
        [[5, 5, 2, 3, 5, 1, 6], 5, 4],
        [[1, 1, 1], 2, 2],
        [[], 1, -1],
    ]

    def test(self):
        for a, x, expected_result in Test.test_cases:
            actual_result = solution(a, x)
            self.assertEquals(actual_result, expected_result)


def solution(a, x):
    x_count = 0
    for i in xrange(len(a)):
        if x_count == len(a)-i-1:
            return i
        if a[i] == x:
            x_count += 1
    return -1


if __name__ == '__main__':
    unittest.main()
