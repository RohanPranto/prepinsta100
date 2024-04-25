#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Enter a line: ";
    getline(cin, s);

    int ans = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= '0' && s[i] <= '9') { // Check if the character is a digit
            ans += s[i] - '0'; // Convert the character to its integer value and add to sum
        }
    }

    cout << "Sum of numbers in the string: " << ans << endl;

    return 0;
}
