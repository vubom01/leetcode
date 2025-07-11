# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/

"""
- Create a dummy node that points to the head of the linked list (head)
- Loop through each node of the linked list
- If current.val is in nums -> remove this node
- Otherwise, move to the next node
- TC: O(n)
- SC: O(n)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current:
            if current.val in nums_set:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next


sol = Solution()
print(sol.modifiedList(
    [1, 1, 2, 3],
    ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4,
                    next=ListNode(
                        val=5
                    )
                )
            )
        )
    ),
))
