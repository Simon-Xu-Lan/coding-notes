class Solution:
  """
  @params: A string
  @return: Whether the string is a valid palindrom
  """
  def isPalingdrom(self, str):
    left, right = 0, len(str) - 1
    while left < right:
      while left < right and not self.is_valid(str[left]):
        left += 1
      while left < right and not self.is_valid(str[right]):
        right -= 1
      if left < right and str[left].lower() != str[right].lower():
        return False
      left += 1
      right -= 1
    return True

  def is_valid(self, char):
    return char.isdigit() or char.isalpha()

