from typing import List


class Solution:
    class TrieNode:
        def __init__(self, count=0, val='#', children=None):
            self.count = count
            self.val = val
            self.children = children

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        head = self.TrieNode()
        result = []

        for word in words:
            node = head
            for c in word:
                if node.children is None:
                    node.children = [self.TrieNode(count=1, val=c)]
                else:
                    isExist = False
                    for child in node.children:
                        if child.val == c:
                            child.count += 1
                            isExist = True
                    if isExist is False:
                        node.children.append(self.TrieNode(count=1, val=c))
                for child in node.children:
                    if child.val == c:
                        node = child
                        break

        for word in words:
            node = head
            total = 0

            for c in word:
                for child in node.children:
                    if child.val == c:
                        total += child.count
                        node = child
                        break
            result.append(total)

        return result

sol = Solution()
print(sol.sumPrefixScores(["abcd"]))
