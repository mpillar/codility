import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[1, 2, 3], 0, [1, 2, 3]],
        [[1, 2, 3], 1, [3, 1, 2]],
        [[1, 2, 3], 2, [2, 3, 1]],
        [[], 0, []],
        [[1], 0, [1]],
        [[1], 99, [1]]
    ]

    def test(self):
        for A, K, expected_result in Test.test_cases:
            actual_result = solution(A, K)
            self.assertItemsEqual(actual_result, expected_result)


def solution(A, K):
    result = [None] * len(A)
    counter = 0
    for element in A:
        result[(counter + K) % len(A)] = element
        counter += 1
    return result


if __name__ == '__main__':
    unittest.main()
