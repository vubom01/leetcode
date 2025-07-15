"""
https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
"""

"""
- Trie
- Insert the words while counting occurrences of each prefix
- Loop through all nodes, adding up the counts of prefix nodes along the path to obtain the final result
- TC: O(n * L)
- SC: O(n * L)
"""

from typing import List


class Solution:
    class TrieNode:
        def __init__(self):
            self.count = 0
            self.children = {}

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        head = self.TrieNode()
        result = []

        for word in words:
            node = head
            for c in word:
                if c not in node.children:
                    node.children[c] = self.TrieNode()
                node = node.children[c]
                node.count += 1

        for word in words:
            node = head
            total = 0
            for c in word:
                node = node.children[c]
                total += node.count
            result.append(total)

        return result


sol = Solution()
print(sol.sumPrefixScores(["abcd"]))
