#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    
    return true;
}

bool canExpressAsSumOfPrimes(int num) {
    for (int i = 2; i <= num / 2; ++i) {
        if (isPrime(i) && isPrime(num - i)) {
            return true;
        }
    }
    return false;
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    
    if (canExpressAsSumOfPrimes(number)) {
        cout << number << " can be expressed as the sum of two prime numbers.\n";
    } else {
        cout << number << " cannot be expressed as the sum of two prime numbers.\n";
    }
    
    return 0;
}
