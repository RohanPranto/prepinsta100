// cpp code to Toggle each character in a string, use toUpperCase and toLowerCase functions

#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cout << "Enter a string: ";
    cin >> str;
    for (int i = 0; i < str.length(); i++) {
        if (isupper(str[i])) {
            str[i] = tolower(str[i]);
        } else {
            str[i] = toupper(str[i]);
        }
    }
    cout << "Toggled string is: " << str << endl;
    return 0;
}

