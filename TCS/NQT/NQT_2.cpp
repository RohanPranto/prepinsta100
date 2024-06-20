#include <bits/stdc++.h>
using namespace std;

int main() {
    int m = 3, n = 7; // Example values
    
    vector<vector<int>> dp(m, vector<int>(n, -1));
    
    function<int(int, int)> f = [&](int i, int j) -> int {
        if (i == 0 && j == 0) return 1;
        if (i < 0 || j < 0) return 0;
        if (dp[i][j] != -1) return dp[i][j];

        int up = f(i-1, j);
        int left = f(i, j-1);
        return dp[i][j] = up + left;
    };

    int result = f(m-1, n-1);

    cout << "Number of unique paths from top-left to bottom-right is: " << result << endl;
    
    return 0;
}
