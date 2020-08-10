# 374. 猜数字大小
#
# 20200810
# huao
# 二分

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        begin = 1
        end = n
        mid = (begin + end) // 2
        result = guess(mid)
        while result != 0:
            if result == 1:
                begin = mid
                mid = (begin + end) // 2
            else:
                end = mid
                mid = (begin + end) // 2
            if begin + 1 == end:
                if guess(end) == 0:
                    return end
            result = guess(mid)
        return mid