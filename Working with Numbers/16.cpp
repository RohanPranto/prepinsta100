// The concept is simple, find the digits of the integer. Compare each digit with 0 if the digit is equal to 0 then replace it with 1. Construct the new integer with the replaced digits.

#include <iostream>
using namespace std;

int main() {
    int num, num2 = 0;

    cout << "Enter number: ";
    cin >> num;

    if (num == 0) {
        num2 = 1;
    }

    // Replacing 0 with 1
    while (num > 0) {
        int rem = num % 10;
        if (rem == 0) {
            rem = 1;
        }
        num = num / 10;
        num2 = num2 * 10 + rem;
    }

    num = 0;

    while (num2 > 0) {
        int r = num2 % 10;
        num = num * 10 + r;
        num2 /= 10;
    }

    cout << "Converted number is: " << num;

    return 0;
}
