class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        x_rev = 0

        min_sign = True if x < 0 else False
        x = abs(x)
    
        while x > 0:
            if x_rev > INT_MAX // 10 or (x_rev == INT_MAX // 10 and x % 10 > 7):
                return 0
            x_rev = x_rev * 10 + x % 10
            x //= 10

        x_rev = -x_rev if min_sign else x_rev

        return x_rev



a = Solution()
res = a.reverse(-123332)
print(res)