from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)

        list_zeros_ind = []

        if len(nums) == 1:
            return True

        for i in range(len_nums-2, -1, -1):
            if nums[i] == 0:
                list_zeros_ind.append(i)
            elif list_zeros_ind:
                for j in range(len(list_zeros_ind)-1, -1, -1):
                    if list_zeros_ind[j]-i < nums[i]:
                        list_zeros_ind.pop(j)

        if not list_zeros_ind:
            return True
        return False


a = Solution()
res = a.canJump()
print(res)