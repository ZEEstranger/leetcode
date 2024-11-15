# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:

        sum_num = []
        num_1 = 0
        num_2 = 0

        for i in range(len(l1) - 1, -1, -1):
            num_1 += l1[i] * pow(10, i)

        for i in range(len(l2) - 1, -1, -1):
            num_2 += l1[i] * pow(10, i)

        sum = num_1 + num_2
        
        while sum > 0:
            sum_num.append(sum % 10)
            sum = sum // 10           




a = Solution()
a.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])