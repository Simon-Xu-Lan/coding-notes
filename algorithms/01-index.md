# 双指针， double cursor
lintcode 170, Rotate List
```py
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    # Set window width as k % length, the window is defined by two cursors, then move two cursors together
    # 用两个指针定义一个窗口， 设置窗口区间为 k % length， 然后两个指针一起移动
    def rotateRight(self, head, k):
        
        # Due to k % length, the lenght can't be zero below
        if head is None:
            return None

        dummy = ListNode(None)
        dummy.next = head
        
        
        # Get the length of the linked list
        length = self.get_length(head)
        
        # Move the end cursor k steps
        end = dummy
        k = k % length
        steps = 0
        for _ in range(k):
            end = end.next


        # Move two cursors together till end cursor to the end of list
        start = dummy
        while end.next:
            start = start.next
            end = end.next

        # Rotate the sub linked list
        end.next = dummy.next
        dummy.next = start.next
        start.next = None
        

        return dummy.next

    def get_length(self, head):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return length

    # Two cursors move seperatedly, 两个指针各自移动
    def rotateRight2(self, head, k):
        if head is None:
            return None

        dummy = ListNode(None)
        dummy.next = head
        start = dummy
        end = dummy
        
        # Move end to the end of linked list and calculate the length of linked list
        length = 0
        while end.next:
            length += 1
            end = end.next

        # Move start to the start of sub linked list
        steps = 0
        while start.next and steps < (length - k % length):
            start = start.next
            steps += 1

        # Rotate the sub linked list
        end.next = dummy.next
        dummy.next = start.next
        start.next = None
        

        return dummy.next


```