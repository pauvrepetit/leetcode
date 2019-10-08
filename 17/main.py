from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return_list = ['']
        for num in digits:
            if num == '2':
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 'a'
                    list2[i] = list2[i] + 'b'
                    list3[i] = list3[i] + 'c'
                return_list = list1 + list2 + list3
            elif num == '3':
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 'd'
                    list2[i] = list2[i] + 'e'
                    list3[i] = list3[i] + 'f'
                return_list = list1 + list2 + list3
            elif num == '4':
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 'g'
                    list2[i] = list2[i] + 'h'
                    list3[i] = list3[i] + 'i'
                return_list = list1 + list2 + list3
            elif num == '5':
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 'j'
                    list2[i] = list2[i] + 'k'
                    list3[i] = list3[i] + 'l'
                return_list = list1 + list2 + list3
            elif num == '6':
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 'm'
                    list2[i] = list2[i] + 'n'
                    list3[i] = list3[i] + 'o'
                return_list = list1 + list2 + list3
            elif num == '7':
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                list4 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 'p'
                    list2[i] = list2[i] + 'q'
                    list3[i] = list3[i] + 'r'
                    list4[i] = list4[i] + 's'
                return_list = list1 + list2 + list3 + list4
            elif num == '8':
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 't'
                    list2[i] = list2[i] + 'u'
                    list3[i] = list3[i] + 'v'
                return_list = list1 + list2 + list3
            else:
                list1 = return_list[:]
                list2 = return_list[:]
                list3 = return_list[:]
                list4 = return_list[:]
                for i in range(len(list1)):
                    list1[i] = list1[i] + 'w'
                    list2[i] = list2[i] + 'x'
                    list3[i] = list3[i] + 'y'
                    list4[i] = list4[i] + 'z'
                return_list = list1 + list2 + list3 + list4
        return return_list
        
sol = Solution()
print(sol.letterCombinations('23'))
