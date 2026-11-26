# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        toRet=None
        curr1=list1
        curr2=list2

        if not list1:
            return list2
        if not list2:
            return list1
        
        if curr2.val<=curr1.val:
            toRet=curr2
            curr2=curr2.next
        else:
            toRet=curr1
            curr1=curr1.next

        curr=toRet
        while curr1 and curr2:
            if curr2.val<=curr1.val:
                curr.next=curr2
                curr2=curr2.next
            else:
                curr.next=curr1
                curr1=curr1.next
            curr=curr.next
        
        if curr1:
            curr.next=curr1
        
        if curr2:
            curr.next=curr2
        
        return toRet
        