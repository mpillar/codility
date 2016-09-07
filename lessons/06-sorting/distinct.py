import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[], 0],
        [[3, 3, 1, 2], 3],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEquals(actual_result, expected_result)


def solution(A):
    if len(A) == 0:
        return 0
    A.sort()
    result = 1
    for i in xrange(1, len(A)):
        if A[i-1] != A[i]:
            result += 1
    return result


if __name__ == '__main__':
    unittest.main()
