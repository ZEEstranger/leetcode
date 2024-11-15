from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        add_flag = True
        for ind in range(len(digits)-1, -1, -1):
            if add_flag:
                digits[ind] += 1
                add_flag = False
            else:
                break
            if digits[ind] == 10:
                digits[ind] = 0
                add_flag = True
            
            if ind == 0 and add_flag:
                return [1] + digits
            
        return digits
            

print(Solution().plusOne([0]))