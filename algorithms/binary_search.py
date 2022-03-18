class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    # Find any position of a target number in a sorted array. Return -1 if target does not exist.
    def findPosition(self, nums, target):
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            if nums[mid] < target:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1

    # Find the last position of a target number in a sorted array. Return -1 if target does not exist.
    def lastPosition(self, nums, target):
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                start = mid
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
        
        if nums[end] == target:
            return end
        
        if nums[start] == target:
            return start
       
        return -1


      # For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
      # If the target number does not exist in the array, return -1
    def firstPosition(self, nums, target):
        if not nums:
              return -1
          
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                end = mid
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
        
        if nums[start] == target:
            return start   
        
        if nums[end] == target:
            return end
        
        return -1

    # Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.
    def mountainSequence(self, nums):
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[mid] < nums[mid - 1] :
                end = mid
            else:
              return nums[mid]
            
        
        if nums[start] > nums[end]:
            return nums[start]  
        
        if nums[start] <= nums[end]:
            return nums[end]
        
        return -1
       