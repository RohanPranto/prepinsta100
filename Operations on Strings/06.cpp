// Count the number of vowels

#include <iostream>
#include <string>
using namespace std;

int main()
{

    string str;
    cout << "enter a string: ";
    cin >> str;
    int count = 0;
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'u' || str[i] == 'o' || str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U'){
            count++;
        }
    }

    cout<<count;
}
