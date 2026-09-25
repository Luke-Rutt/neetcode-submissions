# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2

        list3 = ListNode(0)
        curr3 = list3

        while curr1 or curr2:
            if curr1 is None:
                curr3.next = curr2
                break

            elif curr2 is None:
                curr3.next = curr1
                break
            
            elif curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            
            curr3 = curr3.next
                
        return list3.next

