#  Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pair


class Solution:
  """
  @param numbers: An array of Integer
  @param target: target = numbers[index1] + numbers[index2]
  @return: an integer, the number of pair
  """

  # return numbers
  def two_sum(self, numbers, target):
    if not numbers:
      return 0
    
    numbers.sort()

    result = 0
    left, right = 0, len(numbers) - 1
    while left < right:
      if numbers[left] + numbers[right] <= target:
        result += right - left
        left += 1
      else:
        right -= 1
    
    return result

  

  
