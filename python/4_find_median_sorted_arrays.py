"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

"""
- Approach 1: Create new array from nums1 and nums2, sort the new array and return result
  -- TC: O((n+m) log (n+m))
  -- SC: O(n+m)
- Approach 2: Using merge sort to merge 2 arrays
  -- TC: O(n+m)
  -- SC: O(n+m) -> can be optimize to O(1)
- Approach 3:
  -- To find the median, we need to divide the new array into 2 parts of equal length
  -- Part 1: [0...mid1] of nums1 and [0...mid2] of nums2
  -- Part 2: [mid1+1...n-1] of nums1 and [mid2+1...m-1] of nums2
  -- nums1[mid1] <= nums2[mid2+1] and nums2[mid2] <= nums1[mid1+1]
  -- mid2 = (n+m+1) // 2 - mid1
  -- We need to find mid1
  -- Use binary search to find mid1
  -- If nums1[mid1] > nums2[mid2+1], we need to decrease mid1 to increase mid2
  -- Otherwise, we need to increase mid1 to decrease mid2
  -- TC: O(log min(n,m))
  -- SC: O(1)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        low, high = 0, n
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (n + m + 1) // 2 - mid1

            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            r1 = nums1[mid1] if mid1 < n else float("inf")

            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            r2 = nums2[mid2] if mid2 < m else float("inf")

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)

            if l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
