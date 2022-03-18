 Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are zero-based.



class Solution:
  """
  @param numbers: An array of Integer
  @param target: target = numbers[index1] + numbers[index2]
  @return: [index1, index2] (index1 < index2)
  """

  # return numbers
  def two_sum1(self, numbers, target):
    if not numbers:
      return [-1, -1]

    nums = [ (number, index) for index, number in numbers]
    numbers.sort()

    left, right = 0, len(numbers) - 1
    while left < right:
      if numbers[left] + numbers[right] < target:
        left += 1
      elif numbers[left] + numbers[right] > target:
        right -= 1
      else: 
        return numbers[left], numbers[right]
    
    return [-1, -1]

  # return index
  def two_sum2(self, numbers, target):
    if not numbers:
      return [-1, -1]

    nums = [(number, index) for index, number in numbers]
    numbers.sort()

    left, right = 0, len(numbers) - 1
    while left < right:
      if numbers[left][0] + numbers[right][0] < target:
        left += 1
      elif numbers[left][0] + numbers[right][0] > target:
        right -= 1
      else: 
        return numbers[left][1], numbers[right][1]
    
    return [-1, -1]


  
