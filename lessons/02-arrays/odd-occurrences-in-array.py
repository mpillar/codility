import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[9, 3, 9, 3, 9, 7, 9], 7],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEquals(actual_result, expected_result)


def solution(A):
    result = 0
    for element in A:
        result ^= element
    return result


if __name__ == '__main__':
    unittest.main()
