class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        strr = ''.join(char for char in s if char.isalnum())

        return strr[::-1] == strr


        