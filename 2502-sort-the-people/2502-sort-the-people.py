class Solution(object):
    def sortPeople(self, names, heights):
        

        pair = list(zip(heights, names))  # height first
        pair.sort(reverse=True)           # sort by height
        return [name for h, name in pair]
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        