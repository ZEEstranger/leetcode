from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        ind = 0
        

        while len(nums) > 0:
            point = len(nums) // 2
            print(point)
            if nums[point] == target:
                return ind + point
            elif nums[point] > target:
                nums = nums[:point]
            elif nums[point] < target:
                nums = nums[point + 1:]
                ind += point + 1
        return 0   
                
            

a = Solution()
res = a.searchInsert([1,3,5,6], target = 2)
print(res)