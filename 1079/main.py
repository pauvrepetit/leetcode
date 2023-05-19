#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#

# @lc code=start
class Solution:
    def com(self, num: int) -> int:
        res = 1
        for i in range(1, num + 1):
            res *= i
        return res


    def numTilePossibilities(self, tiles: str) -> int:
        count = 0
        all_tile = []
        for i in range(1, 2 ** len(tiles)):
            bin_i = bin(i)[2:]
            bin_i = '0' * (len(tiles)-len(bin_i)) + bin_i
            char_count = dict()
            char_all = 0
            tile = []
            for j in range(len(tiles)):
                if bin_i[j] == '1':
                    char_all += 1
                    tile.append(tiles[j])
                    if tiles[j] in char_count.keys():
                        char_count[tiles[j]] += 1
                    else:
                        char_count[tiles[j]] = 1
            tile.sort()
            tile_str = ""
            for ii in tile:
                tile_str += ii
            if tile_str in all_tile:
                continue
            all_tile.append(tile_str)
            local_count = self.com(char_all)
            for v in char_count.values():
                local_count //= self.com(v)
            count += local_count
        return count

# @lc code=end

print(Solution().numTilePossibilities("AAABBC"))
