//cpp code to find out Permutations in which n people can occupy r seats in a classroom

#include <bits/stdc++.h>
using namespace std;

int fact(int n)
{
    if (n == 0)
        return 1;
    return n * fact(n - 1);
}

int main()
{
    int n, r;
    cout << "Enter the number of people: ";
    cin >> n;
    cout << "Enter the number of seats: ";
    cin >> r;
    cout << "The number of permutations is "  << fact(n) / fact(n - r) << endl;
    return 0;
}

// Time Complexity: O(n)
// Space Complexity: O(1)

// Input: Enter the number of people: 5
//        Enter the number of seats: 3
// Output: The number of permutations in which 5 people can occupy 3 seats in a classroom is: 60

