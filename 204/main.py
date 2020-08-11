# 204. 计数质数
#
# 20200811
# huao

from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primeList = [2]
        for i in range(3, n):
            for prime in primeList:
                if prime > sqrt(i):
                    primeList.append(i)
                    break
                if i % prime == 0:
                    break
            else:
                primeList.append(i)
        return len(primeList)


print(Solution().countPrimes(499979))
