# https://leetcode.com/problems/valid-arrangement-of-pairs/description/?envType=daily-question&envId=2024-12-02

from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = {}
        for u, v in pairs:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]

        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for u in graph:
            out_degree[u] += len(graph[u])
            for v in graph[u]:
                in_degree[v] += 1

        start, end = None, None
        for vertex in set(in_degree.keys()).union(out_degree.keys()):
            out_diff = out_degree[vertex] - in_degree[vertex]
            if out_diff == 1:
                start = vertex
            elif out_diff == -1:
                end = vertex

        if start is None and end is None:
            start = next((v for v in graph if out_degree[v] > 0), None)

        graph_copy = defaultdict(list, {u: graph[u][:] for u in graph})
        path = []
        stack = [start]
        while stack:
            u = stack[-1]
            if graph_copy[u]:
                v = graph_copy[u].pop()
                stack.append(v)
            else:
                v = stack.pop()
                if len(stack) > 0:
                    path.append([stack[-1], v])

        path.reverse()
        return path
