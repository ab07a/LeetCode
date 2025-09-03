# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        temp = head
        while temp != None and temp.next!=None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        if head != None and head.val == val:
            return head.next
        return head
        