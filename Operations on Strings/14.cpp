//Capitalize the first and last character to each word of a sentence

#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cout << "Enter a sentence: ";
    getline(cin, s);

    for (int i = 0; i < s.length(); i++) {
        if (i == 0 || s[i - 1] == ' ') {
            s[i] = toupper(s[i]);
        } else if (i == s.length() - 1 || s[i + 1] == ' ') {
            s[i] = toupper(s[i]);
        }
    }

    cout << "Capitalized sentence: " << s << endl;

    return 0;
}