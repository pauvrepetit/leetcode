class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

print(Solution().replaceSpace("We are happy."))
