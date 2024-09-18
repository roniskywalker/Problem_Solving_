# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        s, e = 0, len(nums)-1
        while s <= e:
            if nums[s] != nums[e]:
                return False
            s += 1
            e -= 1
        return True