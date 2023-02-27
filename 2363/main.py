from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # 这就是一个key-value的map的结构
        merged_items_map = {}
        for value, weight in items1 + items2:
            if value in merged_items_map.keys():
                merged_items_map[value] += weight
            else:
                merged_items_map[value] = weight
        merged_items = []
        for value in merged_items_map.keys():
            merged_items.append([value, merged_items_map[value]])
        return sorted(merged_items, key=lambda x : x[0])

print(Solution().mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))
print(Solution().mergeSimilarItems(items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]))
print(Solution().mergeSimilarItems(items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]))
