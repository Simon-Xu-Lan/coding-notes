# The worst time complexity is O(n^2)
# The average time complexity is O(nlogn)
# Space complexity is O(1)
# Merge sort is stable sort method
# Stable sort is keep the original order it two numbers are the same
# Quick sort is not stable sort method
# Quick sort is in-place sort
# QuickSelect算法是On的复杂度，递归深度logn级别，乘起来就是nlogn
# 稳定排序就是指，排序前2个相等的数其在序列的前后位置顺序和排序后它们两个的前后位置顺序相同。
# Insertion Sort, Bubble Sort就属于稳定排序；Quick Sort, Heap Sort就属于不稳定排序。
# Quick short 先整体有序，后局部有序
# Merge sort 先局部有序， 后整体有序
class Solution:
    """
    @param nums: An integer array
    @return: return none
    """
    def sortIntegers(self, nums):
        if not nums:
            return

        self.quickSort(nums, 0, len(nums) - 1)


    def quickSort(self, nums, start, end):
        if start >= end:
            return

        left = start
        right = end
        pivot = nums[(start + end) // 2]
        # All must be left <= right at while line
        while left <= right:
            # Must be nums[left] < pivot. or nums[right] > pivot:
            # if nums[left] <= pivot, left would keep on increase at the circumstance nums[left]=pivot,
            # it would cause unbalance partition

            # To find the number that is greater than pivot.
            # In other words, to find the number that should not stay in left side
            # To find number >= pivot,
            # If number < pivot, keep on increase left by one
            while left <= right and nums[left] < pivot:
                left += 1

            # To find a number that is less than pivot, that should not stay in right side
            while left <= right and nums[right] > pivot:
                right -= 1

            # After the two above while loop finished
            # Fina two number on each side,
            # Then exchange the two number
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)


