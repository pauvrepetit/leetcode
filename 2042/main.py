class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        now_num = -1
        for token in tokens:
            if token[0] in ['0', '1', '2', '3', '4', '5', '5', '6', '7', '8', '9']:
                num_token = int(token)
                if now_num < num_token:
                    now_num = num_token
                else:
                    return False
        return True

print(Solution().areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(Solution().areNumbersAscending(s = "hello world 5 x 5"))
print(Solution().areNumbersAscending(s = "4 5 11 26"))
