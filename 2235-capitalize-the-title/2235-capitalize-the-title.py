class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        word=title.split()
        res=[]
        for i in word:
            if len(i)<=2:
                res.append(i.lower())
            else:
                res.append(i.capitalize())
        return " ".join(res)
        