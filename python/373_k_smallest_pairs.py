"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
"""

"""
- The smallest sum is formed by index i of nums1 and index j of nums2
- The next smaller sum will be either from (i + 1, j) and (i, j + 1)
- Use a heap to keep track of the smallest sums
- TC: O(n log n)
- SC: O(n)
"""

import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        pq = []
        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
        isExist = {}
        while len(res) < k:
            _, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            if i < len(nums1) - 1 and (i + 1, j) not in isExist:
                isExist[(i + 1, j)] = True
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
            if j < len(nums2) - 1 and (i, j + 1) not in isExist:
                isExist[(i, j + 1)] = True
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))

        return res


s = Solution()
print(s.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 20))
