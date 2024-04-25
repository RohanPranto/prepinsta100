// Greatest Common Divisor
#include <iostream>
using namespace std;

// Function to find the GCD (Greatest Common Divisor) of two numbers
int gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    else
    {
        return gcd(b, a % b);
    }
}
int main(){
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout<<"GCD is "<<gcd(a,b);
} 