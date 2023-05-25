from typing import List
#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x : [len(x), x])
        words = sentence.split(" ")
        root_sentence = ""
        for word in words:
            for root in dictionary:
                if root == word[:len(root)]:
                    root_sentence += root
                    break
            else:
                root_sentence += word
            root_sentence += " "
        return root_sentence[:-1]
# @lc code=end

print(Solution().replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
