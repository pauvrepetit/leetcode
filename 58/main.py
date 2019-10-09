class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        wordList = s.split(' ')
        try:
            lastWord = wordList[-1]
            return len(lastWord)
        except IndexError:
            return 0

sol = Solution()
print(sol.lengthOfLastWord("hello world"))
