class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        """
        :type nums: List[int]
        :rtype: int
        """
            
        if len(nums)<3:
            
            return max(nums)
        nums.sort()
        return nums[-3]
        