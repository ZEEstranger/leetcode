from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"[val: {self.val}, next: {self.next}]"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sorted_list = ListNode()
        ind_sorted = sorted_list

        while list1 and list2:
            if list1.val > list2.val:
                ind_sorted.next = list2
                list2 = list2.next
            else:
                ind_sorted.next = list1
                list1 = list1.next

            ind_sorted = ind_sorted.next

        if list1:
            ind_sorted.next = list1
        else:
            ind_sorted.next = list2

        return sorted_list.next
        
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print(Solution().mergeTwoLists(list1, list2))