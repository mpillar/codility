import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[0, 1, 0, 1, 1], 5],
        [[], 0],
        [[0, 1], 1],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEquals(actual_result, expected_result)


def solution(A):
    N = len(A)
    if N == 0:
        return 0
    prefix_sum_ones = [1 if A[0] == 1 else 0] * N
    for i in xrange(1, N):
        prefix_sum_ones[i] = prefix_sum_ones[i-1] + (1 if A[i] == 1 else 0)
    ones_count = A.count(1)
    result = 0
    for i in xrange(N):
        if A[i] == 0:
            result += (ones_count - prefix_sum_ones[i])
    if result > 1000000000:
        return -1
    return result


if __name__ == '__main__':
    unittest.main()
