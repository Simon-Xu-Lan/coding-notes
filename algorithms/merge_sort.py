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
    def sortIntegers(self, nums):
        if not nums:
            return
        start = 0
        end = len(nums) - 1
        temp = [0 for _ in range(len(nums))]
        self.mergeSort(nums, start, end, temp)


    def mergeSort(self, nums, start, end, temp):
        if start >= end:
            return

        middle = (start + end) // 2
        self.mergeSort(nums, start, middle, temp)
        self.mergeSort(nums, middle + 1, end, temp)
        self.merge(nums, start, end, temp)


    def merge(self, nums, start, end, temp):
        middle = (start + end) // 2
        left_index = start
        right_index = middle + 1
        index = left_index


        while left_index <= middle and right_index <= end:
            # 相等的时候先放左边的，这样才能保证相对顺序
            #  if nums[left_index] <= nums[right_index]:
            if nums[left_index] < nums[right_index]:
                temp[index] = nums[left_index]
                index += 1
                left_index += 1
            else:
                temp[index] = nums[right_index]
                index += 1
                right_index += 1

        while left_index <= middle:
            temp[index] = nums[left_index]
            index += 1
            left_index += 1

        while right_index <= end:
            temp[index] = nums[right_index]
            index += 1
            right_index += 1

        for i in range(start, end + 1):
            nums[i] = temp[i]




class Solution2:
    def mergesort(self, seq):
        """归并排序"""
        if len(seq) <= 1:
            return seq
        mid = len(seq) // 2  # 将列表分成更小的两个列表
        # 分别对左右两个列表进行处理，分别返回两个排序好的列表
        left = self.mergesort(seq[:mid])
        right = self.mergesort(seq[mid:])
        # 对排序好的两个列表合并，产生一个新的排序好的列表
        return self.merge(left, right)


    def merge(self, left, right):
        """合并两个已排序好的列表，产生一个新的已排序好的列表"""
        result = []  # 新的已排序好的列表
        i = 0  # 下标
        j = 0
        # 对两个列表中的元素 两两对比。
        # 将最小的元素，放到result中，并对当前列表下标加1
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

