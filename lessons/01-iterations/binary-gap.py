import unittest


class Test(unittest.TestCase):
    test_cases = [
        [1041, 5]
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEquals(actual_result, expected_result)


def solution(A):
    zeros = bin(A)[2:].split('1')
    if A % 2 == 0:
        # Ends in zero; remove last zero element.
        zeros = zeros[:-1]
    return len(max(zeros, key=len))


if __name__ == '__main__':
    unittest.main()
