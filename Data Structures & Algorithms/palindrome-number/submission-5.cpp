class Solution {
public:
    bool isPalindrome(int x) {
        // 1st : Convert into a string
        // string x_str = to_string(x);
        // int left = 0;
        // int right = x_str.size() - 1;
        // while (left <= right) {
        //     if (x_str[left] != x_str[right]) {
        //         return false;
        //     }
        //     left += 1;
        //     right -= 1;
        // }
        // return true;

        // 2nd : Not convert to a string
        if (x < 0) {
            return false;
        }
        long long division = 1;
        while (x >= 10 * division) {
            division *= 10;
        }

        // Get the left digit
        while (x > 0) {
            int left = x / division;
            int right = x % 10;
            if (left != right) {
                return false;
            }
            // Chop left and right from the number
            x = (x % division) / 10;
            division = division / 100;
        }
        return true;
    }
};