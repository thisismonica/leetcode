# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        mid = head
        node = head
        while node:
            node = node.next
            if node:
                node = node.next
                mid = mid.next
        n1,n2 = None,mid
        while n2:
            n3 = n2.next
            n2.next = n1
            n1,n2 = n2,n3
        left,right = head,n1
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
