import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[], []],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertItemsEqual(actual_result, expected_result)


def solution(A):
    # TODO finish this
    return A


if __name__ == '__main__':
    unittest.main()
