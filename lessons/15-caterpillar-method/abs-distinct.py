import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[-5, -3, -1, 0, 3, 6], 5],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEqual(actual_result, expected_result)


def solution(A):
    return len(set([abs(x) for x in A]))


if __name__ == '__main__':
    unittest.main()
