# LCP 01. 猜数字
#
# 20200802
# huao
# 嗯嗯嗯？

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        length = len(guess)
        count = 0
        for i in range(length):
            if guess[i] == answer[i]:
                count += 1
        return count
