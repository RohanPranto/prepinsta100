//cpp code to find Maximum number of handshakes
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of people: ";
    cin >> n;
    cout << n * (n - 1) / 2;
    return 0;
}

