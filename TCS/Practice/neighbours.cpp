#include <iostream>

using namespace std;

int main() {
    const int maxSize = 100;
    int array[maxSize];
    int n;

    cout << "Enter the number of elements in the array: ";
    cin >> n;

    if (n <= 0) {
        cout << "No peak element found" << endl;
        return 0;
    }

    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; ++i) {
        cin >> array[i];
    }

    // Check the first element
    if (array[0] >= array[1]) {
        cout << "Peak element: " << array[0] << endl;
        return 0;
    }

    // Check the last element
    if (array[n - 1] >= array[n - 2]) {
        cout << "Peak element: " << array[n - 1] << endl;
        return 0;
    }

    // Check the middle elements
    for (int i = 1; i < n - 1; ++i) {
        if (array[i] >= array[i - 1] && array[i] >= array[i + 1]) {
            cout << "Peak element: " << array[i] << endl;
            return 0;
        }
    }

    cout << "No peak element found" << endl;
    return 0;
}
