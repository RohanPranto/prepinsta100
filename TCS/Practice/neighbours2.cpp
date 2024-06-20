#include <iostream>

using namespace std;

int main() {
    const int maxSize = 100;
    int array[maxSize];
    int n;

    cout << "Enter the number of elements in the array: ";
    cin >> n;

    if (n == 0) {
        cout << "No peak element found" << endl;
        return 0;
    }

    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; ++i) {
        cin >> array[i];
    }

    int peak = array[0];
    int i = 1;

    while (i < n) {
        // If current element is greater than peak
        if (array[i] > peak) {
            peak = array[i];
            // If peak is greater than both its neighbors, then it's the peak
            if (i == n - 1 || peak > array[i + 1] && peak > array[i - 1]) {
                cout << "Peak element: " << peak << endl;
                return 0;
            }
        }
        else {
            i++;
        }
    }

    cout << "No peak element found" << endl;
    return 0;
}
