// c++ code to  Calculate the number of digits in an integer

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int count = 0;
    while(n != 0) {
        n /= 10;
        count++;
    }
    cout << count;
    return 0;
}
