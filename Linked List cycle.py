# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 

        while fast and fast.next:
            slow = slow.next # movw slow by 1 step
            fast = fast.next.next #move fast by 2 steps

            if slow == fast: # slow and fast meet -> there is a cycle 
                return True # YEs, there is a cyle 

        return False # Fast reached the end of the lsit -> NO cycle 
        


