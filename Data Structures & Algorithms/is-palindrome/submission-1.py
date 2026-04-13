class Solution:
    def isPalindrome(self, s: str) -> bool:
        strr = ''.join(char for char in s if char.isalnum()).replace(' ', '').lower()

        return strr[::-1] == strr


        