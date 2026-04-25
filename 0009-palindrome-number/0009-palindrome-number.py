class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        temp=x
        while temp:
            rev=rev*10+temp%10
            temp//=10
        return rev==x