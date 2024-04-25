// give me cpp code to convert decimal to binary

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Enter a decimal number: ";
    cin >> n;
    string ans = "";
    while (n > 0) {
        ans = to_string(n % 2) + ans;
        n /= 2;
    }
    cout << ans << endl;
    return 0;
}
