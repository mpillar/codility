import unittest


class Test(unittest.TestCase):
    test_cases = [
        ["()()()", 1],
        ["", 1],
        ["(()", 0],
        ["()()(", 0],
        ["((()))(()())", 1],
    ]

    def test(self):
        for S, expected_result in Test.test_cases:
            actual_result = solution(S)
            self.assertEquals(actual_result, expected_result)


def solution(S):
    stack_size = 0
    for c in S:
        if c == '(':
            stack_size += 1
        else:
            if stack_size == 0:
                return 0
            stack_size -= 1
    if stack_size > 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    unittest.main()