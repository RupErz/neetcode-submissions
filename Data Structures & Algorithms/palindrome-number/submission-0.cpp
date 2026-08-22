class Solution {
public:
    bool isPalindrome(int x) {
        // 1st : Convert into a string
        string x_str = to_string(x);
        int left = 0;
        int right = x_str.size() - 1;
        while (left <= right) {
            if (x_str[left] != x_str[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
};