class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        alen = len(A)
        list1 = []
        list2 = []
        for i in range(alen):
            if A[i] % 2 == 0:
                list1.append(A[i])
            else:
                list2.append(A[i])
        return list1 + list2
