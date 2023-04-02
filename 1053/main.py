from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1)[::-1]:
            if arr[i] > arr[i+1]:
                # arr[i]的后面有比arr[i]更小的值，找后面比arr[i]小的值中，最大的那个
                max_idx = len(arr) - 1
                for j in range(i+1, len(arr)):
                    if arr[i] <= arr[j]:
                        max_idx = j - 1
                        break
                for j in range(i+1, len(arr)):
                    if arr[j] == arr[max_idx]:
                        max_idx = j
                        break
                return arr[:i] + arr[max_idx:max_idx+1] + arr[i+1:max_idx] + arr[i:i+1] + arr[max_idx+1:]
        return arr

print(Solution().prevPermOpt1(arr = [3,2,1]))
print(Solution().prevPermOpt1(arr = [1,1,5]))
print(Solution().prevPermOpt1(arr = [1,9,4,6,7]))
print(Solution().prevPermOpt1(arr = [3,1,1,3]))
