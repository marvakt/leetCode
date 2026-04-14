class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={'}':'{',']':'[',')':'('}
        for i in s:
            if i in pairs.values():
                stack.append(i)
            elif i in pairs:
                if not stack or stack.pop()!=pairs[i]:
                    return False
        return not stack
        