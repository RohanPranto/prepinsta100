// largest element in an array
#include <iostream>
using namespace std;

int main() {
    int arr[100], n; // Maximum size of array is 100
    cout << "Enter the number of elements in the array: ";
    cin >> n;

    cout << "Enter elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Assuming first element as maximum
    int max = arr[0];

    // Finding the maximum element
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    cout << "The largest number in the array is: " << max << endl;

    return 0;
}
