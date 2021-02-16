from merge_sort import Solution
from random import randint

check = Solution()

# nums = [3,2,1,4,5]
nums = [randint(1, 100*1000) for i in range(100)]
print(nums)

check.sortIntegers(nums)

print(nums)