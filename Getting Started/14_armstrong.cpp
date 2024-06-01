#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    
    int temp = n;
    int sum = 0;
    int digits = 0;

    // Find the number of digits in the number
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    
    temp = n; // Reset temp to the original number

    while (temp > 0) {
        int last_digit = temp % 10;
        int power = 1;
        
        // Calculate last_digit^digits
        for (int i = 0; i < digits; ++i) {
            power *= last_digit;
        }
        
        sum += power;
        temp /= 10;
    }

    if (sum == n) {
        cout << "Armstrong Number" << endl;
    } else {
        cout << "Not an Armstrong Number" << endl;
    }

    return 0;
}
