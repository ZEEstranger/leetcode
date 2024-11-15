class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 10 and x != 0:
            return False
        
        x_reverse = 0

        while x > x_reverse: 
            x_reverse = x_reverse * 10 + x % 10
            x //= 10

        if x_reverse == x or x_reverse // 10 == x:
            return True
        return False
        

    

a = Solution()
print(a.isPalindrome(10))