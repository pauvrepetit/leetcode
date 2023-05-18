#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        count_s = [0 for _ in range(10)]
        count_g = [0 for _ in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            count_s[int(secret[i])] += 1
            count_g[int(guess[i])] += 1
        for i in range(10):
            cows += min(count_s[i], count_g[i])
        cows -= bulls
        return "{}A{}B".format(bulls, cows)

# @lc code=end

