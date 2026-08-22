using namespace std;
#include <cmath>
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<pair<int, int>, unordered_set<char>> hashGroup = {};
        unordered_map<int, unordered_set<char>> hashCol, hashRow = {};
        for (int r = 0; r < board.size(); r ++)
        {
            for (int c = 0; c < board[0].size(); c ++)
            {
                char currentLetter = board[r][c];
                if (currentLetter == '.') {
                    continue;
                };
                // Convert into 3x3 index
                int newR = floor(r / 3);
                int newC = floor(c / 3);
                // pair<int, int> newSquare = {newR, newC}
                if (hashGroup[{newR, newC}].count(currentLetter) || hashCol[c].count(currentLetter)
                    || hashRow[r].count(currentLetter))
                    {
                        return false;
                    }
                hashGroup[{newR, newC}].insert(currentLetter);
                hashCol[c].insert(currentLetter);
                hashRow[r].insert(currentLetter);
            };
        };
        return true;
    };
};
