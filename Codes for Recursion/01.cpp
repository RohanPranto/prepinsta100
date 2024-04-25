#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int base, exponent;
    cout << "Enter base and exponent: ";
    cin >> base >> exponent;

    double result = pow(base, exponent);

    cout << result;

    return 0;
}
