// Hexadecimal to decimal.cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    string s;
    cout<<"Enter a hexadecimal number: ";
    cin >> s;
    int n = s.size();
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            ans += (s[i] - '0') * pow(16, n - i - 1);
        } else {
            ans += (s[i] - 'A' + 10) * pow(16, n - i - 1);
        }
    }
    cout << ans << endl;
    return 0;
}