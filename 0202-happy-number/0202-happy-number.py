class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()  
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1
