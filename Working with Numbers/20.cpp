// Find the prime numbers between 1 to 100 cpp code


#include <iostream>
using namespace std;

int main() {
    int n = 100;
    int prime[n+1];
    for(int i=0; i<=n; i++) {
        prime[i] = 1;
    }
    prime[0] = 0;
    prime[1] = 0;
    for(int i=2; i*i<=n; i++) {
        if(prime[i] == 1) {
            for(int j=i*i; j<=n; j+=i) {
                prime[j] = 0;
            }
        }
    }
    for(int i=0; i<=n; i++) {
        if(prime[i] == 1) {
            cout << i << " ";
        }
    }
    return 0;
}