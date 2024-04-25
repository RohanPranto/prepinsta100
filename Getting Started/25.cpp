// An Automorphic number is a special number whose square ends with the same digits as the number itself

#include <iostream>
using namespace std;
int main()
{
    int a, i = 1;
    cout << "Enter a number ";
    cin >> a;
    int sqr = a * a;
    while (i < a)
    {
        i = i * 10;
    }
    if (sqr % i == a)
    {
        cout << a << " is automorphic";
    }
    else
    {
        cout << a << " is not automorphic";
    }
    return 0;
}