// cpp code to Length of the string without using strlen() function


#include <iostream>
using namespace std;

int main() {
    string str;
    cout << "Enter a string: ";
    cin >> str;
    int length = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        length++;
    }
    cout << "Length of the string is: " << length << endl;
    return 0;
}