//cpp code to Remove brackets from an algebraic expression

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    cout << "Enter an algebraic expression: ";
    getline(cin, s);
    string ans = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != '(' && s[i] != ')' && s[i] != '[' && s[i] != ']' && s[i] != '{' && s[i] != '}')
        { // check if the character is not a bracket
            ans += s[i]; // only add characters
        }
    }
    cout << ans << endl;
}
