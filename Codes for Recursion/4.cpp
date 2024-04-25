//cpp code to Smallest element in an array

#include <bits/stdc++.h>
using namespace std;

int main(){
    int arr[100], n; // Maximum size of array is 100

    cout << "Number of elements: ";
    cin >> n;

    cout << "Enter elements of the array: ";

    for(int i=0;i<n;i++){
        cin >> arr[i];
    }

    int min = arr[0];

    for (int i = 0;i < n; i++)
    {
        if (arr[i] <= min)
        {
            min = arr[i];
        }
    }
    cout << "The smallest number in the array is: " << min << endl;
    
}