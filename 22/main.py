from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return_list = [[0, 0, '']]
        for i in range(n * 2):
            list1 = []
            for j in range(len(return_list)):
                num_a = return_list[j][0]
                num_b = return_list[j][1]
                string = return_list[j][2]
                if num_a == n:
                    list1.append([num_a, num_b + 1, string + ')'])
                elif num_a == num_b:
                    list1.append([num_a + 1, num_b, string + '('])
                else:
                    list1.append([num_a + 1, num_b, string + '('])
                    list1.append([num_a, num_b + 1, string + ')'])
            return_list = list1
        list1 = []
        for i in range(len(return_list)):
            list1.append(return_list[i][2])
        return list1


sol = Solution()
print(sol.generateParenthesis(3))
