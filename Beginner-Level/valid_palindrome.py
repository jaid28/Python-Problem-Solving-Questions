class Solution:
  def validPalindrome(self, s:str) ->bool:
    i, j = 0, len(s) - 1

    while i < j:
      if s[i] == s[j]:
        i+= 1
        j-= 1

      else:
        return self.validPalindromeUtil(s, i+1, j) or self.validPalindrome(s, i, j-1)
    return True

  def validPalindromeUtil(self, s, i, j):
    while i < j:
      if s[i] == s[j]:
        i+= 1
        j-= 1
      else:
        return False
    return True

# ------------------------------
#  USER INPUT PART
# ------------------------------
s = input("Enter String: ")
solution = Solution()
user = solution.validPalindrome(s)
print("Valid palindrome (after deleting at most 1 character):", user)
