class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Case insensitive : W = w
        #Ignore all non-alphanumeric : not a number also not a char

        str_ignore = "".join([ char for char in s if char.isalpha() or char.isdigit()])
        reverse_str_ignore = str_ignore[::-1]
        return True if reverse_str_ignore.lower() == str_ignore.lower() else False

        