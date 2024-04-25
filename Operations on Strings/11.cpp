// cpp code to Remove spaces from a string

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    string ans = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != ' ')
        { // check if the character is not a space
            ans += s[i]; // only add characters
        }
    }
    cout << ans << endl;
}