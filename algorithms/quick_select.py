# Quick Select average Time Complexity is O(n)

class Solution:
    """
        @K: An integer
        @param nums: An array of nums
        @return: return
    """

    def kthlargestElement(self, k, nums):
        if not nums:
            return

        self.quickSelect(nums, 0, len(nums) - 1, k)


    def quickSelect(self, nums, start, end, k):
        middle = (start + end) // 2
        pivot = nums[(start + end) // 2]
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # left_length = right + 1
        right_length = len(nums) - left

        if k <= right_length:
            quickSelect(nums, left, len(nums) - 1, k)
        else:
            self.quickSelect(nums, o, right, k - right_length)


    def quickSelectJZ(self, nums, start, end, k):
        if start == end:
            return nums[start]

        # middle = (start + end) // 2
        pivot = nums[(start + end) // 2]
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # left_length = right + 1
        right_length = len(nums) - left

        if start + k - 1 < right:
            quickSelect(nums, start, right, k)
        if start + k - 1 >= left:
            self.quickSelect(nums, left, end, k - (left - start))
        return nums[right + 1]

    # 快速选择算法的Partition的实质：
    # 快速选择 / 快速排序中的partition是可左可右的partition，也就是说，对于nums[i] == pivot时，这个数字既可以放在左边，也可以放在右边。
    #
    # 为什么这样划分数组呢？原因是为了避免出现类似[1, 1, 1, 1, 1, 1]的数组中的元素，全部被分到一边的情况。
    # 我们让nums[i] == pivot的情况既不属于左边也不属于右边，这样就能够让partition之后的结果稍微平衡一些。
    # 如果 quickselect / quicksort写成了nums[i] < pivot在左侧，nums[i] >= pivot在右侧这种形式，
    # 就会导致划分不平均，从而导致错误或者超时。

    # 简单的说就是，quick select 和 quick sort 的 partition
    # 目标不是将数组严格的按照 nums[i] < pivot 和nums[i] >= pivot 去拆分开，
    # 而是只要能够让左半部分 <= 右半部分即可。这样子 nums[i] == pivot 放在哪儿都无所谓，两边都可以放
