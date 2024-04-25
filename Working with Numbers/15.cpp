// cpp code to addition of two fractions. Suppose, First fraction consist of 1 as numerator and 3 as denominator, and Second fraction consist of 3 as numerator and 9 as denominator.
//  (1 / 3) + (3 / 9) = (6 / 9) = (2 / 3)

#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    int num1 = 1, den1 = 3;
    int num2 = 3, den2 = 9;

    // Find the common denominator
    int den3 = den1 * den2 / gcd(den1, den2);

    // Add the fractions
    int num3 = (num1 * (den3 / den1)) + (num2 * (den3 / den2));

    // Simplify the fraction
    int common_factor = gcd(num3, den3);
    num3 /= common_factor;
    den3 /= common_factor;

    // Output the result
    cout << num3 << " / " << den3 << endl;

    return 0;
}
