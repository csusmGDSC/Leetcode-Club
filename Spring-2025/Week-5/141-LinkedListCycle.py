# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # O(n) Time, O(1) Space.
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        slow = head
        fast = head

        while head or head.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True

        return False
      
class Solution: # O(n) Time, O(n) Space.
  def hasCycle(self, head: Optional[ListNode]) -> bool:
      seen = set()
  
      current = head
      while current:
          if current in seen:
              return True
          seen.add(current)
          current = current.next
  
      return False
