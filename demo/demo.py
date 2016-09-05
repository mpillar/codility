import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[-1, 3, -4, 5, 1, -6, 2, 1], 1],  # or 3, or 7
        [[1, 0, 1], 1],
        [[1, -1], -1],
        [[0, 1, -1], 0],
        [[], -1],
        [[1], 0]
    ]

    def test(self):
        for test_input, test_output in Test.test_cases:
            result = solution(test_input)
            self.assertEqual(result, test_output)


def solution(array):
    if len(array) == 0:
        return -1
    # Pass through the array once to compute the running sum.
    sums = [array[0]] * len(array)
    for i in range(1, len(array)):
        sums[i] = sums[i-1] + array[i]
    # Pass through a second time to find the first equilibrium index, if it exists.
    for p in range(0, len(array)):
        tmp = sums[-1] - array[p] - 2 * (0 if p == 0 else sums[p-1])
        if tmp == 0:
            return p
    return -1


if __name__ == '__main__':
    unittest.main()


