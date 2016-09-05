import unittest
import sys


class Test(unittest.TestCase):
    test_cases = [
        [[1, 1], 0],
        [[3, 1, 2, 4, 3], 1]
    ]

    def test(self):
        for test_input, test_output in Test.test_cases:
            result = solution(test_input)
            self.assertEqual(result, test_output)


def solution(array):
    # Pass through the array once to compute the running sum.
    sums = [array[0]] * len(array)
    for i in range(1, len(array)):
        sums[i] = sums[i-1] + array[i]
    # Pass through a second time to find the minimum as described in the problem.
    result = sys.maxint
    for p in range(1, len(array)):
        tmp = abs(sums[-1] - 2 * sums[p-1])
        result = min(result, tmp)
    return result


if __name__ == '__main__':
    unittest.main()
