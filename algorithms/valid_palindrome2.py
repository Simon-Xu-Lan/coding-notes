# Given a non-empty string s, you may delete at most one character. 
# Judge whether you can make it a palindrome.
class Solution:
  def valid_palindrome(self, s):
    # abnormal check
    if s is None:
      return True
    
    # Find positions left right, if left >= right, means the string is palindrome
    left, right = self.find_difference(s, 0, len(s) -1)
    if left >= right:
      return True
    
    # Check string is palindrome if remove left char or right char
    return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)

  # check substring is palindrom or not, 
  def is_palindrome(self, s, left, right):
    left, right = self.find_difference(s, left, right)
    # not palindrom if left < right
    # is palindrom is left >= right
    return left >= right 

  def find_difference(self, s, left, right):
    while left < right:
      if s[left] != s[right]:
        return left, right
      left += 1
      right -= 1
    return left, right  # return tuple (left, right)
