class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    # Solution Simon
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return 0
        
        letter_frequency = self.letterFrequency(s)
        
        no_odd_frequency = True
        longest_palindrome = 0
        for letter in letter_frequency:
            if letter_frequency[letter] % 2 == 0:
                longest_palindrome += letter_frequency[letter]
            if letter_frequency[letter] % 2 != 0:
                longest_palindrome += letter_frequency[letter] - 1
                no_odd_frequency = False
        
        if no_odd_frequency:
            return longest_palindrome
        return longest_palindrome + 1
    
        

    def letterFrequency(self, s):
        result = {}
        for letter in s:
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
        return result

    
    # Solution Linghu
    def longestPalindrome2(self, s):
      hash = {}

      for letter in s:
        if letter in hash:
          del hash[letter]
        else:
          hash[letter] = True

      print(hash)

      remove = len(hash)

      if remove > 0:
        remove -= 1
      
      return len(s) - remove
