import unittest


class Test(unittest.TestCase):
    test_cases = [
        [[3, 2, 3, 4, 3, 3, 3, -1], 0],
        [[], -1],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEquals(actual_result, expected_result)


def find_leader(A):
    """
    Find the leader for a given array if it exists. Copied from the lessons.
    """
    n = len(A)
    size = 0
    value = None
    for k in xrange(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for k in xrange(n):
        if A[k] == candidate:
            count += 1
    if count > n // 2:
        leader = candidate
    return leader


def solution(A):
    l = find_leader(A)
    if l == -1:
        return -1
    return A.index(l)


if __name__ == '__main__':
    unittest.main()
