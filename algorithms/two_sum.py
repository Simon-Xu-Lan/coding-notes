class twoSum_hash_map(object):
    def __init__(self):
        # Initiate data structure here
        self.count = {}

        # Add the number to an internal data structure
        @param number: int
        @return: None
        def add(self, number):
            if number in self.count:
                self.count += 1
            else:
                self.count[number] = 1


        # Find if there exists any pair of numbers witch sum is equal to value
        # @param value int
        # @return: true if can be found or false
        def find(self, value):
            for num in self.count:
                if value - num in self.count and \
                        (value - num != num or self.count(num) > 1):
                    return True
            return False


class TwoSum_two_pointer:
    def __init__(self):
        self.nums = []

    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1
        while index > 0 and self.nums[index - 1] > self.nums[index]:
            self.nums[index], self.nums[index - 1] = self.nums[index - 1], self.nums[index]


    def find(self, value):
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else
                return True
        return false

# Three number sum
def threesum(self, nums):
    # First to sort the array
    nums = sorted(nums)

    results = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        self.find_two_sum(nums, i + 1, len(nums) -1, -nums[i], results)

    return results

def find_two_sum(self, nums, left, right, target, results):
    last_pair = None
    while left < right:
        if nums[left] + nums[right] == target:
            if (nums[left], nums[right]) != last_pair:
                results.append([-target, nums[left], nums[right]])
            last_pair = nums[left], nums[right]
            right -= 1
            left -= 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1

triangle count