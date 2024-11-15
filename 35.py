class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        
        if n == 1:
            return x

        sign = False if n < 0 else True
        n = abs(n)
        
        if n % 2 == 1:
            mul = self.myPow(x, (n-1)//2)**2 * x
        else:
            mul = self.myPow(x, n//2)**2
        
        if not sign:
            return 1/mul
        return mul

print(Solution().myPow(2.0, 10))