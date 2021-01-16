# The worst time complexity is O(nlogn)
# The average time complexity is O(nlogn)
# Space complexity is O(n)
# Merge sort is stable sort method
# Stable sort is keep the original order it two numbers are the same
# Quick sort is not stable sort method


class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        result = []
        index_A = 0
        index_B = 0
        while index_A < len(A) and index_B < len(B):
            if A[index_A] <= B[index_B]:
                result.append(A[index_A])
                index_A += 1
            else:
                result.append(B[index_B])
                index_B += 1
        if index_A < len(A):
          for number in A[index_A:]:
            result.append(number)
        elif index_B < len(B):
          for number in B[index_B:]:
            result.append(number)

        return result