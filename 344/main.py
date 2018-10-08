class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        slist.reverse()
        return "".join(slist)
