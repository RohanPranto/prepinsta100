#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

void bruteForce(vector<int>& arr, int n, int target) {
    for (int i = 0; i < n; i++) {
        int curSum = 0;
        for (int j = i; j < n; j++) {
            curSum += arr[j];
            if (curSum == target) {
                for (int k = i; k <= j; k++) {
                    cout << arr[k] << " ";
                }
                cout << endl;
            }
        }
    }
}


int main() {
    vector<int> arr = {3, 4, -7, 1, 3, 3, 1, -4};
    int N = arr.size();
    int target = 7;
    bruteForce(arr, N, target);
    return 0;
}