class Solution:
    def isPalindrome(self, s: str) -> bool:
        # #Sol 1 : Convert into a string without special char and reverse
        # #Case insensitive : W = w
        # #Ignore all non-alphanumeric : not a number also not a char

        # str_ignore = "".join([ char for char in s if char.isalpha() or char.isdigit()])
        # reverse_str_ignore = str_ignore[::-1]
        # return True if reverse_str_ignore.lower() == str_ignore.lower() else False

        #Sol2 :Use two pointers , ignore special value by using ASCII value
        # ord(char) -> return its ascii value
        left = 0
        right = len(s) - 1
        while left < right :
            while left < right  and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def alphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or
        (ord('a') <= ord(c) <= ord('z')) or 
        (ord('0') <= ord(c) <= ord('9')))

            
        