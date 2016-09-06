"""
FIXME this isn't scoring 100% yet.
"""

import unittest
import collections
import sys


class Test(unittest.TestCase):
    test_cases = [
        [[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], 3],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0], -1],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEquals(actual_result, expected_result)


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(set)

    def connect(self, a, b):
        for node in [a, b]:
            if node not in self.nodes:
                self.nodes.add(node)
        self.edges[a].add(b)
        self.edges[b].add(a)

    def shortest_path(self, a, b):
        """
        Find the shortest path from node A to node B. Use Dijkstra's algorithm.
        """
        distances = collections.defaultdict(lambda: sys.maxint)
        queue = []
        visited = set()
        for connected in self.edges[a]:
            distances[connected] = 1
            queue.append(connected)
        while len(queue) > 0:
            node = queue.pop()
            if node in visited:
                continue
            visited.add(node)
            for connected in self.edges[node]:
                if connected not in visited: queue.append(connected)
                distances[connected] = min(distances[connected], distances[node]+1)
        return -1 if distances[b] == sys.maxint else distances[b]


def fibonacci(n):
    """
    Generate a list of fibonacci numbers up to and including n.
    """
    result = [1, 1]
    if n <= 2:
        return result[0:n]
    counter = 2
    while True:
        next_fib = result[counter-2] + result[counter-1]
        if next_fib > n:
            break
        result.append(next_fib)
        counter += 1
    return result


def solution(A):
    N = len(A)
    # Landing pad. This simplifies the algorithm.
    A += [1]
    # Plus two to account for the start and end positions.
    f = fibonacci(N+2)
    g = Graph()
    for i in xrange(-1, N):
        if 0 <= i < len(A) and A[i] != 1:
            continue
        # Look for all nodes that we can hop to from here. Add these edges to the graph.
        for hop_distance in f:
            low = i - hop_distance
            high = i + hop_distance
            for d in [low, high]:
                if 0 <= d < len(A) and A[d] == 1:
                    g.connect(i, d)
    return g.shortest_path(-1, N)


if __name__ == '__main__':
    unittest.main()
