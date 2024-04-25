// We are given an array Arr with N distinct coins and a target T. We have an infinite supply of each coin denomination. We need to find the number of ways we sum up the coin values to give us the target.

// Each coin can be used any number of times.

// Sample Input 
// 3 4
// 1 2 3
// Sample Output 
// 4

#include <iostream>
#include <vector>
using namespace std;

int coinChangeWays(vector<int>& coins, int target) {
    int n = coins.size();
    vector<vector<int>> dp(n + 1, vector<int>(target + 1, 0));
    
    // If the target is 0, there's only one way - by not selecting any coin
    for (int i = 0; i <= n; ++i)
        dp[i][0] = 1;
    
    // Dynamic programming approach to fill up the dp array
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= target; ++j) {
            if (coins[i - 1] <= j)
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]];
            else
                dp[i][j] = dp[i - 1][j];
        }
    }
    
    return dp[n][target];
}

int main() {
    int N, T;
    cin >> N >> T;
    vector<int> Arr(N);
    for (int i = 0; i < N; ++i)
        cin >> Arr[i];
    
    int ways = coinChangeWays(Arr, T);
    cout << ways << endl;
    
    return 0;
}
