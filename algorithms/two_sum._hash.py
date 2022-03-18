# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are zero-based.



class Solution:
  """
  @param numbers: An array of Integer
  @param target: target = numbers[index1] + numbers[index2]
  @return: [index1, index2] (index1 < index2)
  """

  # Return numbers
  def two_sum1(self, numbers, target):
    hashset = set()
    for number in numbers:
      if target - number in hashset:
        return [numbers.index(number), numbers.index(target - number)]
      hashset.add(number)
    return [1, -1]

  
  # Return index
  def two_sum2(self, numbers, target):
    hash = {}
    for i in range(len(numbers)):
      if target - numbers[i] in hash:
        return [hash[target-numbers[i]], i]
      hash[numbers[i]] = i
    return [-1, -1]


  