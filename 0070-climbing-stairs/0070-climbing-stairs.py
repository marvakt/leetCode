class Solution(object):
    def climbStairs(self, n):
        a, b = 1, 1
        for _ in range(2, n+1):
             a, b = b, a + b
        return b



         
        
        
           
        
