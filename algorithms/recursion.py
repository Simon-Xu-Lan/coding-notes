class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # The condition to stop recursion
        if n == 1:
            return 0
        if n == 2:
            return 1

        # build the relationship between nth lever and before nth lever
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


    def binarySearch(self, nums, start, end, target):
        """
        @param nums: a sorted array
        @
        @param target: a number
        @return: the position th
        """
        if start > end :
            return -1

        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            return self.binarySearch(nums, start, middle - 1, target)
        if nums[middle] < target:
            return self.binarySearch(nums, middle + 1, len(nums) - 1, target)