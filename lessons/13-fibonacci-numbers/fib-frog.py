"""
FIXME this isn't scoring 100% yet.
"""

import unittest
import collections


class Test(unittest.TestCase):
    test_cases = [
        # 0  1  2  3  4  5  6  7  8  9  10, and 11 is the landing pad. Start at -1.
        [[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], 3],
    ]

    def test(self):
        for A, expected_result in Test.test_cases:
            actual_result = solution(A)
            self.assertEquals(actual_result, expected_result)


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(set)

    def connect(self, node_a, node_b):
        for node in [node_a, node_b]:
            if node not in self.nodes:
                self.nodes.add(node)
        self.edges[node_a].add(node_b)
        self.edges[node_b].add(node_a)

    def shortest_path(self, node_a, node_b):
        """
        Find the shortest path from node A to node B. Use Dijkstra's algorithm.
        """
        distances = collections.defaultdict(int)
        queue = []
        visited = set()
        for connected in self.edges[node_a]:
            distances[connected] = 1
            queue.append(connected)
        while len(queue) > 0:
            node = queue.pop()
            if node in visited:
                continue
            visited.add(node)
            for connected in self.edges[node]:
                queue.append(connected)
                if distances[connected] == 0:
                    distances[connected] = distances[node]+1
                else:
                    distances[connected] = min(distances[connected], distances[node]+1)
        return -1 if distances[node_b] == 0 else distances[node_b]


def fibonacci(n):
    """
    Generate a list of fibonacci numbers up to and including n.
    """
    result = [1, 1]
    if n <= 2:
        return result[0:n]
    counter = 2
    while True:
        next = result[counter-2] + result[counter-1]
        if next > n:
            break
        result.append(next)
        counter += 1
    return result


def solution(A):
    N = len(A)
    A += [1] # Landing pad.
    f = fibonacci(N+1)
    g = Graph()
    for i in xrange(-1, N):
        if 0 <= i < len(A) and A[i] != 1:
            continue
        # Look for all nodes that we can hop to from here. Add these edges to the graph.
        for hop_distance in f:
            low = i - hop_distance
            if low >= 0 and A[low] == 1:
                g.connect(i, low)
            high = i + hop_distance
            if high < len(A) and A[high] == 1:
                g.connect(i, high)
    return g.shortest_path(-1, N)


if __name__ == '__main__':
    unittest.main()
