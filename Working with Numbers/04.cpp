#include <iostream>
#include <cmath>
using namespace std;

// Function to convert binary to decimal
int binary_to_decimal(long long n) {
    int decimal = 0;
    int power = 0;

    while (n != 0) {
        int digit = n % 10;
        decimal += digit * pow(2, power);
        n /= 10;
        power++;
    }

    return decimal;
}

int main() {
    long long n;
    cout << "Enter a binary number: ";
    cin >> n;

    int decimal = binary_to_decimal(n);
    cout << "Decimal equivalent: " << decimal << endl;

    return 0;
}
